#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// ================= CONFIGURAÇÕES =================
const char* ssid = "Suna";
const char* password = "Suna06091171";
const char* apiUrl = "http://172.16.71.174:5000/detect-bin";

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

// Variáveis de controle
unsigned long lastCapture = 0;
const unsigned long captureInterval = 60000; // 60 segundos - reduz concorrencia com WiFi
bool cameraInitialized = false;
bool wifiConnected = false;

void setup() {
  Serial.begin(115200);
  delay(2000); // Aguarda estabilização
  Serial.println("\n=== ESP32-CAM - Versao Segura ===");
  
  // Verificar memória
  Serial.printf("Memoria livre: %d bytes\n", ESP.getFreeHeap());
  
  // Conectar WiFi de forma segura (antes da camera para evitar DMA overflow durante handshake)
  if (!connectWiFi()) {
    Serial.println("Falha na conexao WiFi - reiniciando...");
    delay(5000);
    ESP.restart();
  }
  
  // Adiar inicializacao da camera para o momento da captura
  
  Serial.println("Setup concluido com sucesso!");
  Serial.printf("Memoria final: %d bytes\n", ESP.getFreeHeap());
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
  config.xclk_freq_hz = 8000000;  // 8MHz - reduz carga no cam_task
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_QQVGA;
  config.jpeg_quality = 30; // mais compressao -> menor tamanho
  config.fb_count = 1; // 1 buffer para evitar sobrecarga
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY; // captura apenas quando solicitado
  config.fb_location = CAMERA_FB_IN_DRAM; // DRAM para estabilidade

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Erro na camera: 0x%x\n", err);
    return false;
  }
  
  cameraInitialized = true;
  Serial.println("Camera inicializada com sucesso!");
  return true;
}

bool connectWiFi() {
  Serial.println("Conectando ao WiFi...");
  
  WiFi.setSleep(false); // evita pausas longas do WiFi que atrapalham a camera
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
  return true;
}

void loop() {
  // Verificar memória periodicamente
  static unsigned long lastMemoryCheck = 0;
  if (millis() - lastMemoryCheck > 60000) { // A cada 1 minuto
    lastMemoryCheck = millis();
    Serial.printf("Memoria: %d bytes\n", ESP.getFreeHeap());
    
    // Se memória muito baixa, reiniciar
    if (ESP.getFreeHeap() < 30000) {
      Serial.println("Memoria muito baixa! Reiniciando...");
      ESP.restart();
    }
  }
  
  // Verificar WiFi
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi perdido, reconectando...");
    wifiConnected = false;
    if (!connectWiFi()) {
      Serial.println("Falha na reconexao, aguardando...");
      delay(10000);
      return;
    }
  }
  
  // Capturar e enviar imagem
  if (millis() - lastCapture > captureInterval) {
    lastCapture = millis();
    
    if (captureAndSend()) {
      Serial.println("Ciclo concluido com sucesso!");
    } else {
      Serial.println("Ciclo falhou, tentando novamente em breve...");
    }
  }
  
  delay(1000); // Pausa no loop principal
}

bool captureAndSend() {
  // Inicializa a camera somente quando necessario
  if (!cameraInitialized && !initCamera()) {
    Serial.println("Falha ao inicializar camera para captura");
    return false;
  }

  Serial.println("Capturando imagem...");

  // Capturar imagem com proteção
  camera_fb_t *fb = NULL;
  fb = esp_camera_fb_get();
  
  if (!fb) {
    Serial.println("Falha na captura da imagem");
    return false;
  }
  
  Serial.printf("Imagem capturada: %d bytes\n", fb->len);
  
  // Verificar tamanho da imagem
  if (fb->len == 0 || fb->len > 80000) { // limite menor para garantir margem de RAM
    Serial.println("Imagem invalida ou muito grande");
    esp_camera_fb_return(fb);
    return false;
  }
  
  // Copiar JPEG para heap e liberar frame buffer o quanto antes
  uint8_t *jpeg_copy = (uint8_t*) malloc(fb->len); // DRAM
  if (!jpeg_copy) {
    Serial.println("Falha ao alocar memoria para copia do JPEG");
    esp_camera_fb_return(fb);
    return false;
  }

  size_t jpeg_len = fb->len;
  memcpy(jpeg_copy, fb->buf, jpeg_len);

  // Liberar buffer da camera imediatamente para evitar overflows
  esp_camera_fb_return(fb);
  fb = NULL;

  // Desinicializar camera imediatamente apos liberar o frame buffer
  esp_camera_deinit();
  cameraInitialized = false;

  // Enviar para API usando a copia
  bool success = sendToAPI(jpeg_copy, jpeg_len);

  // Liberar copia
  free(jpeg_copy);

  return success;
}

bool sendToAPI(uint8_t *data, size_t len) {
  Serial.println("Enviando para API...");
  
  HTTPClient http;
  http.setTimeout(20000); // 20 segundos timeout
  http.setReuse(false);
  
  WiFiClient client;
  if (!http.begin(client, apiUrl)) {
    Serial.println("Falha ao iniciar HTTP client");
    return false;
  }
  
  // Configurar headers
  http.addHeader("Content-Type", "image/jpeg");
  http.addHeader("Connection", "close");
  
  // Enviar POST
  int httpCode = http.POST(data, len);
  
  if (httpCode > 0) {
    Serial.printf("HTTP Response: %d\n", httpCode);
    
    if (httpCode == 200) {
      Serial.println("HTTP 200 OK");
      http.end();
      return true;
    } else {
      Serial.printf("HTTP error: %d\n", httpCode);
      http.end();
      return false;
    }
  } else {
    Serial.printf("HTTP error: %s\n", http.errorToString(httpCode).c_str());
    http.end();
    return false;
  }
}
