# 🤖 ESP32-CAM YOLO Client - Cliente Inteligente para Detecção de Objetos

Cliente ESP32-CAM otimizado que captura imagens automaticamente e as envia para uma API YOLO para detecção de objetos em tempo real. Este projeto implementa um sistema inteligente de captura e envio de imagens com processamento de respostas JSON e indicadores visuais.

## 🌟 Visão Geral

O **ESP32-CAM YOLO Client** é um cliente especializado que:

- **Captura Imagens**: Captura automática de imagens da câmera OV2640
- **Envia para YOLO**: Comunicação HTTP com API YOLO para detecção
- **Processa Respostas**: Parse inteligente de respostas JSON da API
- **Indicadores Visuais**: LED para status do sistema
- **Otimizações**: Configurações específicas para YOLO e IoT

## 🎯 Casos de Uso

- **Monitoramento Inteligente**: Detecção automática de objetos
- **Segurança IoT**: Sistema de vigilância com IA
- **Automação Residencial**: Controle baseado em detecções
- **Pesquisa e Educação**: Demonstração de IA em dispositivos IoT
- **Prototipagem**: Base para projetos de visão computacional

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐    Captura    ┌─────────────────┐    HTTP POST    ┌─────────────────┐
│   ESP32-CAM     │ ─────────────► │   Processador   │ ──────────────► │   API YOLO      │
│   (OV2640)      │   Automática  │   de Imagem     │   JPEG Binary   │   (Flask)       │
│                 │                │                 │                 │                 │
│ • Câmera        │                │ • Otimização    │                 │ • Detecção      │
│ • WiFi          │                │ • Compressão    │                 │ • YOLOv8        │
│ • LED Status    │                │ • Validação     │                 │ • Resposta      │
└─────────────────┘                └─────────────────┘                 └─────────────────┘
         │                                                                        │
         │                                                                        │
         ▼                                                                        ▼
┌─────────────────┐                                                ┌─────────────────┐
│   Serial Logs   │                                                │   JSON Response │
│   (Debug)       │                                                │   (Processed)   │
└─────────────────┘                                                └─────────────────┘
```

## 📁 Estrutura do Projeto

```
esp32_cam_yolo_client/
├── 📄 esp32_cam_yolo_client.ino    # Código principal Arduino
├── 📄 platformio.ini               # Configuração PlatformIO (opcional)
├── 📄 README.md                    # Este arquivo
└── 📁 examples/                    # Exemplos de uso
    ├── basic_capture.ino           # Captura básica
    ├── wifi_test.ino               # Teste de WiFi
    └── camera_test.ino             # Teste de câmera
```

## 🚀 Funcionalidades Principais

### 📸 **Captura Inteligente de Imagens**
- **Automática**: Captura a cada 30 segundos (configurável)
- **Otimizada**: Configurações específicas para YOLO
- **Qualidade**: JPEG otimizado (qualidade 12)
- **Resolução**: QVGA (320x240) ideal para detecção
- **Validação**: Verificação de tamanho e qualidade

### 🌐 **Comunicação HTTP**
- **Endpoint**: `/detect-bin` para JPEG binário direto
- **Método**: POST com Content-Type: image/jpeg
- **Timeout**: 20 segundos para evitar travamentos
- **Retry**: Reconexão automática em caso de falha
- **Headers**: Configuração otimizada para transmissão

### 🔍 **Processamento de Respostas**
- **Parse JSON**: Processamento inteligente de respostas
- **Formatação**: Exibição legível das detecções
- **Estatísticas**: Contagem e resumo de objetos
- **Posicionamento**: Análise de posição dos objetos
- **Confiança**: Exibição de scores de detecção

### 💡 **Indicadores Visuais**
- **LED Status**: Indicadores visuais do sistema
- **3 Piscadas Lentas**: Sistema inicializado
- **LED Aceso**: Capturando imagem
- **2 Piscadas Rápidas**: Sucesso na API
- **3 Piscadas Lentas**: Erro na comunicação

### ⚡ **Otimizações de Performance**
- **Memória**: Gerenciamento eficiente de memória
- **WiFi**: Configurações otimizadas para estabilidade
- **Câmera**: Configurações específicas para YOLO
- **Timeout**: Sistema de timeout para evitar travamentos
- **PSRAM**: Uso otimizado de memória externa

## 🔧 Configuração e Instalação

### 📋 Pré-requisitos

#### Hardware
- **ESP32-CAM AI-Thinker** com câmera OV2640
- **Flash**: 4MB ou superior
- **PSRAM**: Recomendado para melhor performance
- **Cabo USB-TTL** para programação
- **Fonte de alimentação 3.3V** estável
- **LED externo** (opcional, para indicadores)

#### Software
- **Arduino IDE 2.0+** ou **PlatformIO**
- **ESP32 Board Manager** (Arduino)
- **ESP32 Camera Library**
- **ArduinoJson 6.21.4+**

### 🚀 Instalação Rápida

#### 1. Configurar Arduino IDE
```bash
# 1. Abrir Arduino IDE
# 2. Ir em Ferramentas > Placa > ESP32 Arduino > AI Thinker ESP32-CAM
# 3. Configurar partição para "Huge APP"
# 4. Configurar porta COM correta
# 5. Configurar velocidade de upload para 115200
```

#### 2. Instalar Bibliotecas
```bash
# Via Library Manager:
# 1. Sketch > Include Library > Manage Libraries
# 2. Buscar e instalar:
#    - ESP32 Camera
#    - ArduinoJson (versão 6.21.4+)
#    - WiFi (já incluída)
#    - HTTPClient (já incluída)
```

#### 3. Configurar WiFi e API
```cpp
// Editar no arquivo esp32_cam_yolo_client.ino
const char* ssid = "SUA_REDE_WIFI";
const char* password = "SUA_SENHA_WIFI";
const char* apiUrl = "http://SEU_IP:5000/detect-bin";
```

#### 4. Fazer Upload
```bash
# 1. Verificar configurações
# 2. Clicar em "Upload"
# 3. Aguardar conclusão
# 4. Abrir Serial Monitor (115200 baud)
```

### ⚙️ Configurações Avançadas

#### Configurações de Câmera
```cpp
// Configurações otimizadas para YOLO
const int TARGET_JPEG_QUALITY = 12;     // Qualidade JPEG (10-15 ideal)
const size_t MAX_IMAGE_SIZE = 150000;   // Tamanho máximo (150KB)
const int MIN_FREE_HEAP = 50000;        // Memória mínima livre
const unsigned long captureInterval = 30000; // Intervalo de captura (30s)
```

#### Configurações de Rede
```cpp
// Configurações WiFi otimizadas
WiFi.setSleep(false);                   // Desabilita sleep mode
WiFi.mode(WIFI_STA);                    // Modo station
const unsigned long SEND_TIMEOUT = 20000; // Timeout de envio (20s)
```

#### Configurações de Sistema
```cpp
// Configurações de sistema
const int LED_PIN = 4;                  // Pino do LED
const bool ENABLE_DEBUG = true;         // Habilitar debug
const int SERIAL_BAUD = 115200;         // Velocidade do Serial
```

## 📊 Configurações de Câmera

### 🎯 Configurações Otimizadas para YOLO

#### Resolução e Formato
```cpp
// Configurações recomendadas para YOLO
config.frame_size = FRAMESIZE_QVGA;     // 320x240 (ideal para YOLO)
config.pixel_format = PIXFORMAT_JPEG;   // Formato JPEG
config.jpeg_quality = 12;               // Qualidade balanceada
config.fb_count = 2;                    // Frame buffers
config.grab_mode = CAMERA_GRAB_LATEST;  // Último frame
```

#### Otimizações de Sensor
```cpp
// Configurações de sensor para melhor detecção
s->set_brightness(s, 0);                // Brilho neutro
s->set_contrast(s, 0);                  // Contraste neutro
s->set_saturation(s, 0);                // Saturação neutra
s->set_special_effect(s, 0);            // Sem efeitos
s->set_whitebal(s, 1);                  // White Balance automático
s->set_awb_gain(s, 1);                  // Auto WB Gain
s->set_wb_mode(s, 0);                   // Modo WB automático
s->set_exposure_ctrl(s, 1);             // Controle automático de exposição
s->set_aec2(s, 0);                      // AEC2 desabilitado
s->set_ae_level(s, 0);                  // Nível AE neutro
s->set_aec_value(s, 300);               // Valor AE padrão
s->set_gain_ctrl(s, 1);                 // Controle automático de ganho
s->set_agc_gain(s, 0);                  // Ganho AGC padrão
s->set_gainceiling(s, (gainceiling_t)0); // Teto de ganho padrão
s->set_bpc(s, 0);                       // BPC desabilitado
s->set_wpc(s, 1);                       // WPC habilitado
s->set_raw_gma(s, 1);                   // Raw GMA habilitado
s->set_lenc(s, 1);                      // LENC habilitado
s->set_hmirror(s, 0);                   // Espelhamento horizontal desabilitado
s->set_vflip(s, 0);                     // Flip vertical desabilitado
s->set_dcw(s, 1);                       // DCW habilitado
s->set_colorbar(s, 0);                  // Colorbar desabilitado
```

### 📏 Tamanhos de Imagem Suportados

| Resolução | Tamanho | Uso | Tamanho Arquivo |
|-----------|---------|-----|------------------|
| **QQVGA** | 160x120 | Teste | ~5-15KB |
| **QVGA** | 320x240 | **Ideal YOLO** | ~15-45KB |
| **VGA** | 640x480 | Qualidade | ~45-150KB |
| **SVGA** | 800x600 | Alta | ~80-200KB |

## 🌐 Configuração de Rede

### 📡 Configurações WiFi

#### Conexão WiFi
```cpp
// Configuração de conexão WiFi
bool connectWiFi() {
  Serial.println("Conectando ao WiFi...");
  WiFi.setSleep(false);                 // Desabilita sleep mode
  WiFi.mode(WIFI_STA);                  // Modo station
  WiFi.begin(ssid, password);           // Inicia conexão
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(1000);
    Serial.print(".");
    attempts++;
  }
  
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("\nFalha na conexão WiFi");
    return false;
  }
  
  Serial.println("\nWiFi conectado!");
  Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
  Serial.printf("RSSI: %d dBm\n", WiFi.RSSI());
  return true;
}
```

#### Configurações de API
```cpp
// Configuração da API YOLO
const char* apiUrl = "http://192.168.1.100:5000/detect-bin";
const unsigned long SEND_TIMEOUT = 20000; // 20 segundos
const int HTTP_RETRY_COUNT = 3;          // Tentativas de reconexão
```

### 🔄 Sistema de Reconexão

#### Reconexão Automática
```cpp
// Sistema de reconexão automática
void reconnectWiFi() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Reconectando WiFi...");
    WiFi.disconnect();
    delay(1000);
    WiFi.begin(ssid, password);
    
    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED && attempts < 10) {
      delay(1000);
      Serial.print(".");
      attempts++;
    }
    
    if (WiFi.status() == WL_CONNECTED) {
      Serial.println("\nWiFi reconectado!");
    }
  }
}
```

## 📤 Envio de Imagens

### 🖼️ Processo de Captura e Envio

#### Captura de Imagem
```cpp
// Captura de imagem otimizada
camera_fb_t *captureImage() {
  camera_fb_t *fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Falha na captura da câmera");
    return NULL;
  }
  
  Serial.printf("Imagem capturada: %dx%d, %d bytes\n", 
    fb->width, fb->height, fb->len);
  
  // Verificar tamanho da imagem
  if (fb->len > MAX_IMAGE_SIZE) {
    Serial.printf("Imagem muito grande: %d bytes\n", fb->len);
    esp_camera_fb_return(fb);
    return NULL;
  }
  
  return fb;
}
```

#### Envio HTTP
```cpp
// Envio HTTP otimizado
bool sendImageToAPI(camera_fb_t *fb) {
  HTTPClient http;
  http.begin(apiUrl);
  http.setTimeout(SEND_TIMEOUT);
  
  // Configurar headers
  http.addHeader("Content-Type", "image/jpeg");
  http.addHeader("Content-Length", String(fb->len));
  
  // Enviar imagem
  int httpResponseCode = http.POST(fb->buf, fb->len);
  
  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println("Resposta da API:");
    Serial.println(response);
    
    // Processar resposta JSON
    processAPIResponse(response);
    
    http.end();
    return true;
  } else {
    Serial.printf("Erro HTTP: %d\n", httpResponseCode);
    http.end();
    return false;
  }
}
```

### 📊 Otimizações de Transmissão

#### Compressão e Qualidade
```cpp
// Otimizações para transmissão
void optimizeForTransmission() {
  sensor_t * s = esp_camera_sensor_get();
  if (s != NULL) {
    // Qualidade JPEG otimizada para transmissão
    s->set_quality(s, TARGET_JPEG_QUALITY);
    
    // Resolução otimizada para YOLO
    s->set_framesize(s, FRAMESIZE_QVGA);
    
    // Configurações para menor tamanho de arquivo
    s->set_contrast(s, 0);              // Contraste neutro
    s->set_saturation(s, 0);            // Saturação neutra
    s->set_brightness(s, 0);            // Brilho neutro
  }
}
```

## 🔍 Processamento de Respostas

### 📝 Parse de JSON

#### Processamento de Resposta
```cpp
// Processamento inteligente de resposta JSON
void processAPIResponse(String response) {
  Serial.println("=== RESPOSTA DA API YOLO ===");
  Serial.println(response);
  Serial.println("=============================");
  
  // Parse JSON
  DynamicJsonDocument doc(2048);
  DeserializationError error = deserializeJson(doc, response);
  
  if (error) {
    Serial.printf("Erro no parse JSON: %s\n", error.c_str());
    return;
  }
  
  // Extrair informações
  String message = doc["message"] | "Sem mensagem";
  int totalObjects = doc["total_objects"] | 0;
  
  Serial.println("📊 RESUMO DA DETECÇÃO:");
  Serial.printf("Mensagem: %s\n", message.c_str());
  Serial.printf("Total de objetos detectados: %d\n", totalObjects);
  
  // Processar detecções
  if (doc.containsKey("detections")) {
    JsonArray detections = doc["detections"];
    Serial.println("\n🔍 OBJETOS DETECTADOS:");
    
    for (JsonObject detection : detections) {
      String className = detection["class_name"] | "desconhecido";
      float confidence = detection["confidence"] | 0.0;
      String position = detection["position"] | "posição desconhecida";
      String size = detection["size"] | "tamanho desconhecido";
      
      Serial.printf("  • %s (Confiança: %.1f%%)\n", 
        className.c_str(), confidence * 100);
      Serial.printf("    Posição: %s\n", position.c_str());
      Serial.printf("    Tamanho: %s\n", size.c_str());
    }
  }
  
  // Informações de áudio
  if (doc.containsKey("response_text")) {
    String responseText = doc["response_text"] | "";
    Serial.printf("\n💬 Resposta gerada: %s\n", responseText.c_str());
  }
  
  if (doc.containsKey("audio_generated")) {
    bool audioGenerated = doc["audio_generated"] | false;
    Serial.printf("🔊 Áudio gerado: %s\n", audioGenerated ? "Sim" : "Não");
  }
  
  Serial.println("=============================");
}
```

### 📊 Análise de Detecções

#### Análise de Posição
```cpp
// Análise inteligente de posição
String analyzePosition(JsonObject bbox) {
  int centerX = bbox["center_x"] | 0;
  int centerY = bbox["center_y"] | 0;
  
  String position = "";
  
  // Posição horizontal
  if (centerX < 107) position += "à esquerda";
  else if (centerX > 213) position += "à direita";
  else position += "no centro";
  
  position += " e ";
  
  // Posição vertical
  if (centerY < 80) position += "no topo";
  else if (centerY > 160) position += "na parte inferior";
  else position += "no meio";
  
  return position;
}
```

#### Análise de Tamanho
```cpp
// Análise inteligente de tamanho
String analyzeSize(int area) {
  if (area < 10000) return "pequeno";
  else if (area < 50000) return "médio";
  else return "grande";
}
```

## 💡 Sistema de Indicadores

### 🔴 LED Status

#### Configuração do LED
```cpp
// Configuração do LED de status
void setupLED() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
}

// Indicadores visuais
void indicateStatus(int status) {
  switch (status) {
    case STATUS_INIT:
      // 3 piscadas lentas - Sistema inicializado
      for (int i = 0; i < 3; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(500);
        digitalWrite(LED_PIN, LOW);
        delay(500);
      }
      break;
      
    case STATUS_CAPTURING:
      // LED aceso - Capturando imagem
      digitalWrite(LED_PIN, HIGH);
      break;
      
    case STATUS_SUCCESS:
      // 2 piscadas rápidas - Sucesso na API
      digitalWrite(LED_PIN, LOW);
      for (int i = 0; i < 2; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(100);
        digitalWrite(LED_PIN, LOW);
        delay(100);
      }
      break;
      
    case STATUS_ERROR:
      // 3 piscadas lentas - Erro na comunicação
      for (int i = 0; i < 3; i++) {
        digitalWrite(LED_PIN, HIGH);
        delay(300);
        digitalWrite(LED_PIN, LOW);
        delay(300);
      }
      break;
  }
}
```

### 📊 Logs de Status

#### Sistema de Logs
```cpp
// Sistema de logs estruturados
void logStatus(const char* message, int level = LOG_INFO) {
  String timestamp = String(millis());
  
  switch (level) {
    case LOG_INFO:
      Serial.printf("[INFO] [%s] %s\n", timestamp.c_str(), message);
      break;
    case LOG_WARNING:
      Serial.printf("[WARN] [%s] %s\n", timestamp.c_str(), message);
      break;
    case LOG_ERROR:
      Serial.printf("[ERROR] [%s] %s\n", timestamp.c_str(), message);
      break;
    case LOG_DEBUG:
      if (ENABLE_DEBUG) {
        Serial.printf("[DEBUG] [%s] %s\n", timestamp.c_str(), message);
      }
      break;
  }
}
```

## 🚨 Solução de Problemas

### 🔧 Problemas Comuns

#### Câmera não inicializa
```cpp
// Verificações para câmera
void checkCamera() {
  // 1. Verificar pinagem
  Serial.println("Verificando pinagem da câmera...");
  
  // 2. Verificar alimentação
  Serial.printf("Voltagem: %.2fV\n", analogRead(36) * 3.3 / 4095.0);
  
  // 3. Verificar sensor
  sensor_t * s = esp_camera_sensor_get();
  if (s) {
    Serial.printf("Sensor ID: 0x%02X\n", s->id.PID);
  } else {
    Serial.println("Sensor não encontrado!");
  }
}
```

#### Problemas de WiFi
```cpp
// Diagnóstico de WiFi
void diagnoseWiFi() {
  Serial.println("=== DIAGNÓSTICO WIFI ===");
  Serial.printf("Status: %d\n", WiFi.status());
  Serial.printf("SSID: %s\n", WiFi.SSID().c_str());
  Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
  Serial.printf("Gateway: %s\n", WiFi.gatewayIP().toString().c_str());
  Serial.printf("DNS: %s\n", WiFi.dnsIP().toString().c_str());
  Serial.printf("RSSI: %d dBm\n", WiFi.RSSI());
  Serial.printf("Canal: %d\n", WiFi.channel());
  Serial.println("========================");
}
```

#### Problemas de Memória
```cpp
// Verificação de memória
void checkMemory() {
  Serial.println("=== VERIFICAÇÃO DE MEMÓRIA ===");
  Serial.printf("Heap livre: %d bytes\n", ESP.getFreeHeap());
  Serial.printf("Heap mínimo: %d bytes\n", ESP.getMinFreeHeap());
  Serial.printf("Heap máximo: %d bytes\n", ESP.getMaxAllocHeap());
  
  if (psramFound()) {
    Serial.printf("PSRAM livre: %d bytes\n", ESP.getFreePsram());
    Serial.printf("PSRAM total: %d bytes\n", ESP.getTotalPsram());
  } else {
    Serial.println("PSRAM não encontrado!");
  }
  Serial.println("=============================");
}
```

### 🐛 Debug Avançado

#### Teste de Câmera
```cpp
// Teste completo da câmera
void testCamera() {
  Serial.println("=== TESTE DE CÂMERA ===");
  
  // Teste de captura
  camera_fb_t * fb = esp_camera_fb_get();
  if (fb) {
    Serial.printf("✓ Captura OK: %dx%d, %d bytes\n", 
      fb->width, fb->height, fb->len);
    
    // Verificar qualidade
    if (fb->len > 0 && fb->len < MAX_IMAGE_SIZE) {
      Serial.println("✓ Tamanho da imagem OK");
    } else {
      Serial.printf("⚠ Tamanho da imagem: %d bytes\n", fb->len);
    }
    
    esp_camera_fb_return(fb);
  } else {
    Serial.println("✗ Falha na captura da câmera");
  }
  
  Serial.println("=======================");
}
```

#### Teste de API
```cpp
// Teste de conectividade com API
void testAPI() {
  Serial.println("=== TESTE DE API ===");
  
  HTTPClient http;
  http.begin(apiUrl);
  http.setTimeout(5000);
  
  int httpResponseCode = http.GET();
  if (httpResponseCode > 0) {
    Serial.printf("✓ API acessível: %d\n", httpResponseCode);
  } else {
    Serial.printf("✗ API não acessível: %d\n", httpResponseCode);
  }
  
  http.end();
  Serial.println("===================");
}
```

## 📈 Performance e Otimizações

### ⚡ Otimizações Implementadas

#### Memória
- **PSRAM**: Uso otimizado de memória externa
- **Buffer Management**: Gerenciamento eficiente de buffers
- **Garbage Collection**: Limpeza automática de memória
- **Heap Monitoring**: Monitoramento contínuo de memória

#### Rede
- **WiFi Sleep**: Desabilitado para estabilidade
- **HTTP Keep-Alive**: Conexões persistentes
- **Timeout Configurável**: Sistema de timeout inteligente
- **Retry Logic**: Lógica de reconexão automática

#### Câmera
- **Qualidade Otimizada**: JPEG balanceado para YOLO
- **Resolução Ideal**: QVGA para melhor performance
- **Configurações de Sensor**: Otimizadas para detecção
- **Frame Buffer**: Múltiplos buffers para streaming

### 📊 Métricas de Performance

#### Tempos Típicos
- **Inicialização**: ~3-5 segundos
- **Captura**: ~100-200ms
- **Processamento**: ~50-100ms
- **Envio WiFi**: ~500ms - 2s (depende da rede)
- **Resposta API**: ~200ms - 1s
- **Total por Ciclo**: ~1-4 segundos

#### Uso de Recursos
- **Memória Heap**: ~80-120KB
- **Memória PSRAM**: ~200-500KB
- **CPU**: ~20-40% durante captura
- **WiFi**: ~1-5MB por hora (depende do intervalo)

## 🔒 Segurança e Boas Práticas

### 🛡️ Considerações de Segurança

#### Rede
- **WiFi**: Use WPA2/WPA3
- **API**: Restrinja acesso se necessário
- **Firewall**: Configure regras apropriadas
- **VLAN**: Isole dispositivos IoT se possível

#### Sistema
- **Logs**: Contêm informações de debug
- **Credenciais**: Armazenadas no código (considere criptografia)
- **Acesso**: Interface pública por padrão
- **Updates**: Mantenha firmware atualizado

### 📋 Boas Práticas

#### Desenvolvimento
- **Versionamento**: Use Git para controle de versão
- **Testes**: Teste sempre antes de deploy
- **Documentação**: Mantenha READMEs atualizados
- **Logs**: Use logs estruturados e apropriados

#### Produção
- **Monitoramento**: Implemente health checks
- **Backup**: Faça backup das configurações
- **Updates**: Mantenha dependências atualizadas
- **Escalabilidade**: Considere load balancing se necessário

## 🤝 Integração com Outros Projetos

### 🔗 Como Usar como Base

#### Para Novos Projetos
```cpp
// Este projeto serve como base para:
// 1. Configuração da câmera ESP32-CAM
// 2. Sistema de comunicação WiFi
// 3. Envio de imagens para APIs
// 4. Processamento de respostas JSON
// 5. Sistema de indicadores visuais
```

#### Para Customizações
```cpp
// Você pode:
// 1. Modificar intervalo de captura
// 2. Alterar endpoint da API
// 3. Adicionar novos indicadores
// 4. Implementar processamento local
// 5. Adicionar sensores adicionais
```

### 📚 Exemplos de Uso

#### Captura Programada
```cpp
// Implementar captura baseada em eventos
void captureOnEvent() {
  // Captura quando movimento é detectado
  // Captura quando timer expira
  // Captura quando botão é pressionado
  // Captura quando sensor é ativado
}
```

#### Processamento Local
```cpp
// Adicionar processamento local
void processLocally(camera_fb_t *fb) {
  // Detecção de movimento
  // Análise de cores
  // Compressão avançada
  // Filtros de imagem
}
```

## 📚 Recursos e Referências

### 🔗 Links Úteis

- **ESP32-CAM**: [Documentação oficial](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)
- **Arduino ESP32**: [Board Manager](https://github.com/espressif/arduino-esp32)
- **Camera Library**: [ESP32 Camera](https://github.com/espressif/esp32-camera)
- **ArduinoJson**: [Biblioteca JSON](https://github.com/bblanchon/ArduinoJson)

### 📖 Documentação Técnica

- **ESP32-CAM Pinout**: [Pinagem detalhada](https://randomnerdtutorials.com/esp32-cam-pinout-gpio-pins/)
- **Camera Configuration**: [Configurações avançadas](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)
- **WiFi Configuration**: [Configuração de rede](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html)
- **HTTP Client**: [Cliente HTTP](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_http_client.html)

### 🎥 Vídeos e Tutoriais

- **Configuração ESP32-CAM**: [Tutorial passo a passo]
- **Integração YOLO**: [Demonstração completa]
- **Sistema de Indicadores**: [Implementação LED]

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 📝 Termos da Licença MIT

```
MIT License

Copyright (c) 2024 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Agradecimentos

- **Espressif Systems**: Pelo ESP32-CAM e bibliotecas
- **Arduino Team**: Pela plataforma Arduino
- **Benoit Blanchon**: Pela biblioteca ArduinoJson
- **Comunidade ESP32**: Pelo suporte e contribuições
- **Desenvolvedores Open Source**: Pelo código de exemplo

## 📞 Suporte e Contato

### 🆘 Como Obter Ajuda

1. **Issues GitHub**: [Abra uma issue](https://github.com/seu-usuario/esp32-cam-yolo-client/issues)
2. **Fórum ESP32**: [Comunidade oficial](https://esp32.com/)
3. **Documentação**: [ESP32 Docs](https://docs.espressif.com/projects/esp-idf/)
4. **Email**: [seu-email@exemplo.com]

### 📋 Checklist de Suporte

Antes de pedir ajuda, verifique:
- [ ] Leu a documentação completa
- [ ] Testou com configurações padrão
- [ ] Verificou pinagem da câmera
- [ ] Confirmou alimentação estável
- [ ] Testou com exemplo básico
- [ ] Verificou logs de erro
- [ ] Incluiu informações do sistema

---

**🌟 Este projeto demonstra o poder do ESP32-CAM para aplicações de IA!**

*Use este código como base para criar sistemas inteligentes de detecção de objetos com ESP32-CAM e APIs de machine learning.*
