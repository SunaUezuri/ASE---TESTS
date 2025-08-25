#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// ================= CONFIGURAÇÕES =================
const char* ssid = "jani 2.4GHz";
const char* password = "W58924013";
const char* apiUrl = "http://127.0.0.1:5000/detect-bin";

unsigned long lastDetection = 0;
const unsigned long detectionInterval = 5000;

// ================= PINOS CAMERA (AI-Thinker OV2640) ===================
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
// ==================================================

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32-CAM YOLO Client");

  // Inicializa câmera
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
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_QVGA;  // 320x240 - menor uso de RAM
  config.jpeg_quality = 15;            // Qualidade média para economizar RAM
  config.fb_count = 1;                 // Apenas 1 buffer para economizar RAM

  if(esp_camera_init(&config) != ESP_OK){
    Serial.println("Falha na inicializacao da camera");
    return;
  }
  Serial.println("Camera inicializada");

  // Conecta Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi");
  while(WiFi.status() != WL_CONNECTED){ 
    delay(500); 
    Serial.print("."); 
  }
  Serial.println("\nWiFi conectado");
  Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
}

void loop() {
  // Verificar se WiFi ainda está conectado
  if(WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi desconectado, tentando reconectar...");
    WiFi.reconnect();
    delay(2000);
    return;
  }

  if(millis() - lastDetection >= detectionInterval){
    lastDetection = millis();
    
    Serial.println("Capturando imagem...");
    
    camera_fb_t *fb = esp_camera_fb_get();
    if(!fb){
      Serial.println("Falha ao capturar imagem");
      return;
    }

    Serial.printf("Imagem: %d bytes\n", fb->len);

    // Verificar se a imagem não é muito grande (evitar problemas de RAM)
    if(fb->len > 50000) { // Máximo 50KB
      Serial.println("Imagem muito grande, pulando...");
      esp_camera_fb_return(fb);
      return;
    }

    // Envia JPEG para a API
    HTTPClient http;
    http.setTimeout(8000); // Timeout de 8 segundos
    
    if(http.begin(apiUrl)) {
      http.addHeader("Content-Type", "image/jpeg");
      
      int code = http.POST(fb->buf, fb->len);
      
      if(code > 0){
        // Limitar tamanho da resposta para economizar RAM
        String resp = http.getString();
        if(resp.length() > 500) {
          resp = resp.substring(0, 500) + "...";
        }
        Serial.printf("API respondeu (%d): %s\n", code, resp.c_str());
      } else {
        Serial.printf("Erro HTTP: %d\n", code);
      }
      http.end();
    } else {
      Serial.println("Falha ao iniciar HTTP client");
    }

    // Liberar buffer da câmera IMEDIATAMENTE
    esp_camera_fb_return(fb);
    
    // Pequena pausa para estabilizar
    delay(200);
    
    Serial.println("Ciclo concluido\n");
  }
  
  // Pausa no loop principal para estabilidade
  delay(200);
}
