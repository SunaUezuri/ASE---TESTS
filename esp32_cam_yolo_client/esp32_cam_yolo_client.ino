#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
 
// ================= CONFIGURAÇÕES =================
const char* ssid = "********";
const char* password = "********";
const char* apiUrl = "http://192.168.164.61:5000/detect-bin";
 
// ================= PINOS CAMERA (AI-THINKER) ===================
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM     0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27
#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM       5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22
 
// ================= VARIÁVEIS DE CONTROLE =================
unsigned long lastCapture = 0;
const unsigned long captureInterval = 30000; // Reduzido para 30 segundos
bool wifiConnected = false;
 
// ================= TIMEOUT =================
const unsigned long SEND_TIMEOUT = 20000; // Aumentado para 20 segundos
 
// ================= CONFIGURAÇÕES DE CÂMERA OTIMIZADAS =================
const int TARGET_JPEG_QUALITY = 12;  // Qualidade boa para YOLO (10-15 é ideal)
const size_t MAX_IMAGE_SIZE = 150000; // 150KB limite para VGA
const int MIN_FREE_HEAP = 50000;      // Memória mínima livre
 
// ================= FUNÇÕES =================
bool connectWiFi() {
  Serial.println("Conectando ao WiFi...");
  WiFi.setSleep(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
 
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(1000);
    Serial.print(".");
    attempts++;
  }
 
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("\nFalha na conexao WiFi");
    return false;
  }
 
  wifiConnected = true;
  Serial.println("\nWiFi conectado!");
  Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
  Serial.printf("RSSI: %d dBm\n", WiFi.RSSI());
  return true;
}
 
void optimizeCameraSettings() {
  sensor_t * s = esp_camera_sensor_get();
  if (s == NULL) {
    Serial.println("Erro: sensor não encontrado!");
    return;
  }
  
  // Configurações para melhor qualidade de imagem
  s->set_brightness(s, 0);     // -2 to 2
  s->set_contrast(s, 0);       // -2 to 2
  s->set_saturation(s, 0);     // -2 to 2
  s->set_special_effect(s, 0); // 0 to 6 (0-No Effect, 1-Negative, 2-Grayscale, 3-Red Tint, 4-Green Tint, 5-Blue Tint, 6-Sepia)
  s->set_whitebal(s, 1);       // 0 = disable , 1 = enable
  s->set_awb_gain(s, 1);       // 0 = disable , 1 = enable
  s->set_wb_mode(s, 0);        // 0 to 4 - if awb_gain enabled (0 - Auto, 1 - Sunny, 2 - Cloudy, 3 - Office, 4 - Home)
  s->set_exposure_ctrl(s, 1);  // 0 = disable , 1 = enable
  s->set_aec2(s, 0);           // 0 = disable , 1 = enable
  s->set_ae_level(s, 0);       // -2 to 2
  s->set_aec_value(s, 300);    // 0 to 1200
  s->set_gain_ctrl(s, 1);      // 0 = disable , 1 = enable
  s->set_agc_gain(s, 0);       // 0 to 30
  s->set_gainceiling(s, (gainceiling_t)0);  // 0 to 6
  s->set_bpc(s, 0);            // 0 = disable , 1 = enable
  s->set_wpc(s, 1);            // 0 = disable , 1 = enable
  s->set_raw_gma(s, 1);        // 0 = disable , 1 = enable
  s->set_lenc(s, 1);           // 0 = disable , 1 = enable
  s->set_hmirror(s, 0);        // 0 = disable , 1 = enable
  s->set_vflip(s, 0);          // 0 = disable , 1 = enable
  s->set_dcw(s, 1);            // 0 = disable , 1 = enable
  s->set_colorbar(s, 0);       // 0 = disable , 1 = enable
  
  Serial.println("Configurações de câmera otimizadas aplicadas!");
}
 
bool initCamera() {
  Serial.println("Inicializando camera...");
 
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer   = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  
  // Configurações otimizadas para VGA
  config.xclk_freq_hz = 20000000;        // Aumentado para 20MHz para melhor performance
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_VGA;     // VGA 640x480 para YOLO
  config.jpeg_quality = TARGET_JPEG_QUALITY; // Qualidade otimizada
  config.fb_count = 2;                   // Buffer duplo
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM; // Usar PSRAM se disponível
  
  // Verificar se PSRAM está disponível
  if(!psramFound()) {
    Serial.println("PSRAM não encontrada, usando DRAM");
    config.fb_location = CAMERA_FB_IN_DRAM;
    config.fb_count = 1; // Reduzir para 1 buffer se usando DRAM
  } else {
    Serial.println("PSRAM encontrada, usando PSRAM para frame buffers");
  }
 
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Erro na camera: 0x%x\n", err);
    return false;
  }
  
  // Aplicar configurações otimizadas
  delay(1000); // Aguardar inicialização
  optimizeCameraSettings();
 
  Serial.println("Camera inicializada com sucesso em VGA!");
  Serial.printf("PSRAM disponível: %s\n", psramFound() ? "Sim" : "Não");
  return true;
}
 
void printImageStats(camera_fb_t *fb) {
  Serial.printf("=== ESTATÍSTICAS DA IMAGEM ===\n");
  Serial.printf("Resolução: %dx%d\n", fb->width, fb->height);
  Serial.printf("Tamanho: %d bytes (%.1f KB)\n", fb->len, fb->len / 1024.0);
  Serial.printf("Formato: %s\n", (fb->format == PIXFORMAT_JPEG) ? "JPEG" : "Outro");
  Serial.printf("Timestamp: %lld\n", fb->timestamp.tv_sec);
  Serial.printf("==============================\n");
}
 
bool sendToAPI(uint8_t *data, size_t len) {
  if (!WiFi.isConnected()) {
    Serial.println("WiFi desconectado durante envio");
    return false;
  }
  
  HTTPClient http;
  WiFiClient client;
  
  // Configurações de timeout
  client.setTimeout(SEND_TIMEOUT / 1000);
  http.setTimeout(SEND_TIMEOUT);
  http.setReuse(false); // Evitar problemas de conexão
 
  int retries = 2; // Reduzido tentativas para evitar travamentos
 
  while (retries-- > 0) {
    Serial.printf("Enviando para API (tentativa %d)...\n", 3 - retries);
    
    if (!http.begin(client, apiUrl)) {
      Serial.println("Falha ao iniciar HTTP client");
      delay(1000);
      continue;
    }
 
    http.addHeader("Content-Type", "image/jpeg");
    http.addHeader("Content-Length", String(len));
    
    unsigned long start = millis();
    int httpCode = http.POST(data, len);
    unsigned long duration = millis() - start;
    
    Serial.printf("Tempo de envio: %lu ms\n", duration);
 
    if (httpCode == 200) {
      String response = http.getString();
      http.end();
 
      Serial.println("\n=== RESPOSTA DA API YOLO ===");
      Serial.println(response);
      Serial.println("=============================\n");
 
      return true;
    } else if (httpCode > 0) {
      Serial.printf("HTTP error: %d - %s\n", httpCode, http.errorToString(httpCode).c_str());
      String errorResponse = http.getString();
      if (errorResponse.length() > 0) {
        Serial.printf("Error response: %s\n", errorResponse.c_str());
      }
    } else {
      Serial.printf("Erro de conexão: %s\n", http.errorToString(httpCode).c_str());
    }
    
    http.end();
    
    if (retries > 0) {
      Serial.println("Aguardando antes da próxima tentativa...");
      delay(2000);
    }
  }
 
  return false;
}
 
bool captureAndSend() {
  Serial.printf("Memória livre antes da captura: %d bytes\n", ESP.getFreeHeap());
  
  // Forçar garbage collection
  if (ESP.getFreeHeap() < MIN_FREE_HEAP) {
    Serial.println("Memória baixa, executando limpeza...");
    delay(100);
    return false;
  }
  
  camera_fb_t *fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Falha na captura da imagem");
    return false;
  }
  
  printImageStats(fb);
 
  // Validações de tamanho
  if (fb->len == 0) {
    Serial.println("Imagem vazia");
    esp_camera_fb_return(fb);
    return false;
  }
  
  if (fb->len > MAX_IMAGE_SIZE) {
    Serial.printf("Imagem muito grande: %d bytes (máximo: %d)\n", fb->len, MAX_IMAGE_SIZE);
    esp_camera_fb_return(fb);
    return false;
  }
 
  // Verificar se há memória suficiente para cópia
  if (ESP.getFreeHeap() < (fb->len + MIN_FREE_HEAP)) {
    Serial.println("Memória insuficiente para processar imagem");
    esp_camera_fb_return(fb);
    return false;
  }
  
  // Copia JPEG para heap
  uint8_t *jpeg_copy = (uint8_t*) malloc(fb->len);
  if (!jpeg_copy) {
    Serial.println("Falha ao alocar memoria para copia do JPEG");
    esp_camera_fb_return(fb);
    return false;
  }
  
  memcpy(jpeg_copy, fb->buf, fb->len);
  size_t jpeg_len = fb->len;
  esp_camera_fb_return(fb); // Liberar o frame buffer imediatamente
 
  Serial.printf("Memória livre após cópia: %d bytes\n", ESP.getFreeHeap());
  
  bool success = sendToAPI(jpeg_copy, jpeg_len);
  free(jpeg_copy);
  
  Serial.printf("Memória livre após envio: %d bytes\n", ESP.getFreeHeap());
  return success;
}
 
void checkSystemHealth() {
  Serial.printf("\n=== STATUS DO SISTEMA ===\n");
  Serial.printf("Uptime: %lu ms\n", millis());
  Serial.printf("Memória livre: %d bytes\n", ESP.getFreeHeap());
  Serial.printf("Tamanho mínimo de heap: %d bytes\n", ESP.getMinFreeHeap());
  Serial.printf("WiFi conectado: %s\n", WiFi.isConnected() ? "Sim" : "Não");
  if (WiFi.isConnected()) {
    Serial.printf("Sinal WiFi: %d dBm\n", WiFi.RSSI());
  }
  Serial.printf("========================\n\n");
}
 
// ================= SETUP =================
void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("\n=== ESP32-CAM - Cliente YOLO VGA Otimizado ===");
  
  // Verificar PSRAM
  if(psramFound()) {
    Serial.printf("PSRAM disponível: %d bytes\n", ESP.getPsramSize());
  } else {
    Serial.println("PSRAM não disponível - performance pode ser limitada");
  }
  
  Serial.printf("Memoria livre inicial: %d bytes\n", ESP.getFreeHeap());
 
  if (!connectWiFi()) {
    Serial.println("Falha na conexao WiFi - reiniciando...");
    delay(5000);
    ESP.restart();
  }
 
  if (!initCamera()) {
    Serial.println("Falha na inicializacao da camera - reiniciando...");
    delay(5000);
    ESP.restart();
  }
  
  // Aguardar estabilização
  delay(2000);
  
  checkSystemHealth();
  Serial.println("Setup concluido com sucesso!");
}
 
// ================= LOOP =================
void loop() {
  static unsigned long lastHealthCheck = 0;
  
  // Verificação de saúde do sistema a cada 5 minutos
  if (millis() - lastHealthCheck > 300000) {
    lastHealthCheck = millis();
    checkSystemHealth();
  }
  
  // Monitorar memória crítica
  if (ESP.getFreeHeap() < MIN_FREE_HEAP) {
    Serial.printf("ALERTA: Memoria muito baixa! (%d bytes)\n", ESP.getFreeHeap());
    Serial.println("Aguardando liberação de memória...");
    delay(5000);
    
    if (ESP.getFreeHeap() < 20000) {
      Serial.println("Memoria criticamente baixa! Reiniciando...");
      ESP.restart();
    }
    return;
  }
 
  // Verificar WiFi
  if (!WiFi.isConnected()) {
    Serial.println("WiFi perdido, reconectando...");
    wifiConnected = false;
    
    // Tentar reconectar
    WiFi.disconnect();
    delay(1000);
    
    if (!connectWiFi()) {
      Serial.println("Falha na reconexao, aguardando...");
      delay(10000);
      return;
    }
  }
 
  // Captura e envio
  if (millis() - lastCapture > captureInterval) {
    lastCapture = millis();
    
    Serial.println("\n--- Iniciando ciclo de captura ---");
    
    if (captureAndSend()) {
      Serial.println("✓ Ciclo concluido com sucesso!");
    } else {
      Serial.println("✗ Ciclo falhou, tentando novamente em breve...");
    }
    
    Serial.println("--- Fim do ciclo ---\n");
  }
 
  // Delay mais longo para reduzir consumo de CPU
  delay(2000);
}