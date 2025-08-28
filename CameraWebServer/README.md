# 📸 CameraWebServer - Servidor Web de Referência para ESP32-CAM

Servidor web completo para ESP32-CAM que serve como base de referência para desenvolvimento de aplicações com câmera. Este projeto demonstra como implementar um servidor HTTP para streaming de vídeo, captura de imagens e controle da câmera via interface web.

## 🌟 Visão Geral

O **CameraWebServer** é um exemplo oficial da Espressif que implementa um servidor web completo para ESP32-CAM, permitindo:

- **Streaming de Vídeo**: Visualização em tempo real da câmera
- **Captura de Imagens**: Download de fotos individuais
- **Controle da Câmera**: Ajuste de configurações via interface web
- **Múltiplos Clientes**: Suporte a múltiplas conexões simultâneas
- **Interface Responsiva**: Interface web adaptável a diferentes dispositivos

## 🎯 Casos de Uso

- **Desenvolvimento**: Base para criar aplicações com câmera
- **Prototipagem**: Teste rápido de funcionalidades de câmera
- **Demonstração**: Mostrar capacidades do ESP32-CAM
- **Referência**: Código de exemplo para implementações customizadas
- **Debugging**: Verificar funcionamento da câmera

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐    WiFi    ┌─────────────────┐    HTTP/WebSocket    ┌─────────────────┐
│   ESP32-CAM     │ ◄────────► │   Cliente       │ ◄──────────────────► │   Navegador     │
│   (OV2640)      │            │   (PC/Mobile)   │                      │   Web           │
│                 │            │                 │                      │                 │
│ • Câmera        │            │ • Conecta WiFi  │                      │ • Interface     │
│ • WiFi          │            │ • Acessa IP     │                      │ • Streaming     │
│ • Servidor HTTP │            │ • Navegador     │                      │ • Controles     │
└─────────────────┘            └─────────────────┘                      └─────────────────┘
```

## 📁 Estrutura do Projeto

```
CameraWebServer/
├── 📄 CameraWebServer.ino       # Código principal Arduino
├── 📄 board_config.h            # Configurações específicas da placa
├── 📄 camera_pins.h             # Pinagem da câmera
├── 📄 camera_index.h            # Interface HTML da câmera
├── 📄 app_httpd.cpp             # Implementação do servidor HTTP
├── 📄 ci.json                   # Configuração CI/CD
├── 📄 partitions.csv            # Configuração de partições
└── 📄 README.md                 # Este arquivo
```

## 🚀 Funcionalidades Principais

### 📹 **Streaming de Vídeo**
- **Tempo Real**: Streaming contínuo da câmera
- **Múltiplos Formatos**: Suporte a diferentes resoluções
- **Qualidade Configurável**: Ajuste de qualidade JPEG
- **Baixa Latência**: Otimizado para streaming em tempo real

### 📸 **Captura de Imagens**
- **Foto Individual**: Captura sob demanda
- **Download Direto**: Download imediato da imagem
- **Formato JPEG**: Imagens em alta qualidade
- **Timestamp**: Nomeação automática com timestamp

### 🎛️ **Controle da Câmera**
- **Resolução**: Ajuste de resolução da imagem
- **Qualidade**: Controle de qualidade JPEG
- **Brilho/Contraste**: Ajustes de imagem
- **Efeitos**: Filtros e efeitos visuais
- **White Balance**: Balanceamento de cor automático

### 🌐 **Interface Web**
- **Responsiva**: Adaptável a diferentes dispositivos
- **Controles Intuitivos**: Interface fácil de usar
- **Status em Tempo Real**: Informações da câmera
- **Múltiplos Clientes**: Suporte a várias conexões

## 🔧 Configuração e Instalação

### 📋 Pré-requisitos

#### Hardware
- **ESP32-CAM AI-Thinker** com câmera OV2640
- **Flash**: 4MB ou superior
- **PSRAM**: Recomendado para melhor performance
- **Cabo USB-TTL** para programação
- **Fonte de alimentação 3.3V** estável

#### Software
- **Arduino IDE 2.0+** ou **PlatformIO**
- **ESP32 Board Manager** (Arduino)
- **ESP32 Camera Library**

### 🚀 Instalação Rápida

#### 1. Configurar Arduino IDE
```bash
# 1. Abrir Arduino IDE
# 2. Ir em Ferramentas > Placa > ESP32 Arduino > AI Thinker ESP32-CAM
# 3. Configurar partição para "Huge APP"
# 4. Configurar porta COM correta
```

#### 2. Configurar WiFi
```cpp
// Editar no arquivo CameraWebServer.ino
const char *ssid = "SUA_REDE_WIFI";
const char *password = "SUA_SENHA_WIFI";
```

#### 3. Fazer Upload
```bash
# 1. Verificar configurações
# 2. Clicar em "Upload"
# 3. Aguardar conclusão
# 4. Abrir Serial Monitor (115200 baud)
```

### ⚙️ Configurações Avançadas

#### Configurações de Câmera
```cpp
// Configurações padrão da câmera
config.frame_size = FRAMESIZE_UXGA;        // Resolução máxima
config.pixel_format = PIXFORMAT_JPEG;      // Formato JPEG
config.jpeg_quality = 12;                  // Qualidade JPEG (0-63)
config.fb_count = 2;                       // Frame buffers
config.grab_mode = CAMERA_GRAB_LATEST;     // Último frame
```

#### Configurações de Rede
```cpp
// Configurações WiFi
WiFi.setSleep(false);                      // Desabilita sleep mode
WiFi.mode(WIFI_STA);                       // Modo station
WiFi.begin(ssid, password);                // Conecta à rede
```

## 📊 Configurações de Câmera

### 🎯 Resoluções Suportadas

| Resolução | Tamanho | Uso Recomendado |
|-----------|---------|------------------|
| **QQVGA** | 160x120 | Teste rápido |
| **QVGA** | 320x240 | **Ideal para YOLO** |
| **VGA** | 640x480 | Qualidade média |
| **SVGA** | 800x600 | Qualidade alta |
| **XGA** | 1024x768 | Alta resolução |
| **UXGA** | 1600x1200 | Máxima resolução |

### ⚙️ Parâmetros Ajustáveis

#### Configurações de Imagem
```cpp
// Ajustes de sensor
s->set_brightness(s, 0);       // Brilho: -2 a +2
s->set_contrast(s, 0);         // Contraste: -2 a +2
s->set_saturation(s, 0);       // Saturação: -2 a +2
s->set_special_effect(s, 0);   // Efeitos: 0-6
s->set_whitebal(s, 1);         // White Balance: 0/1
s->set_awb_gain(s, 1);         // Auto WB Gain: 0/1
s->set_wb_mode(s, 0);          // Modo WB: 0-4
```

#### Configurações de Exposição
```cpp
// Controle de exposição
s->set_exposure_ctrl(s, 1);    // Controle automático: 0/1
s->set_aec2(s, 0);             // AEC2: 0/1
s->set_ae_level(s, 0);         // Nível AE: -2 a +2
s->set_aec_value(s, 300);      // Valor AE: 0-1200
s->set_gain_ctrl(s, 1);        // Controle de ganho: 0/1
s->set_agc_gain(s, 0);         // Ganho AGC: 0-30
```

## 🌐 Interface Web

### 🖥️ Página Principal

A interface web inclui:

- **Streaming em Tempo Real**: Visualização da câmera
- **Controles de Câmera**: Ajustes de configuração
- **Captura de Imagens**: Botão para tirar foto
- **Status do Sistema**: Informações de conexão
- **Configurações Avançadas**: Ajustes detalhados

### 📱 Responsividade

- **Desktop**: Interface completa com todos os controles
- **Tablet**: Layout adaptado para telas médias
- **Mobile**: Interface otimizada para smartphones
- **Touch**: Suporte a gestos touch

### 🎨 Controles Disponíveis

#### Controles Básicos
- **Start/Stop Stream**: Iniciar/parar streaming
- **Capture**: Capturar imagem
- **Resolution**: Alterar resolução
- **Quality**: Ajustar qualidade JPEG

#### Controles Avançados
- **Brightness**: Ajustar brilho
- **Contrast**: Ajustar contraste
- **Saturation**: Ajustar saturação
- **Special Effect**: Aplicar efeitos
- **White Balance**: Configurar WB
- **Exposure**: Ajustar exposição

## 🔍 Endpoints da API

### 📡 Endpoints HTTP

#### Streaming
- **`GET /stream`**: Stream de vídeo em tempo real
- **`GET /capture`**: Captura de imagem individual

#### Controle
- **`GET /control`**: Interface de controle da câmera
- **`POST /control`**: Aplicar configurações
- **`GET /status`**: Status do sistema

#### Sistema
- **`GET /`**: Página principal
- **`GET /favicon.ico`**: Ícone do site
- **`GET /style.css`**: Estilos CSS
- **`GET /script.js`**: JavaScript

### 📊 Formato de Resposta

#### Status da Câmera
```json
{
  "status": "ok",
  "resolution": "QVGA",
  "quality": 12,
  "brightness": 0,
  "contrast": 0,
  "saturation": 0,
  "special_effect": 0,
  "white_balance": 1,
  "exposure": 1
}
```

#### Erro
```json
{
  "status": "error",
  "message": "Descrição do erro",
  "code": 500
}
```

## 🚨 Solução de Problemas

### 🔧 Problemas Comuns

#### Câmera não inicializa
```cpp
// Verificações:
// 1. Pinagem correta (verificar camera_pins.h)
// 2. Alimentação estável (3.3V)
// 3. Modelo da câmera (OV2640)
// 4. Conexões dos pinos
```

#### WiFi não conecta
```cpp
// Soluções:
// 1. Verificar credenciais WiFi
// 2. Confirmar que a rede está disponível
// 3. Verificar força do sinal
// 4. Aumentar timeout de conexão
```

#### Streaming lento
```cpp
// Otimizações:
// 1. Reduzir resolução (usar QVGA)
// 2. Diminuir qualidade JPEG
// 3. Verificar velocidade da rede
// 4. Usar PSRAM se disponível
```

#### Erro de memória
```cpp
// Soluções:
// 1. Habilitar PSRAM
// 2. Usar partição "Huge APP"
// 3. Reduzir resolução
// 4. Diminuir número de frame buffers
```

### 🐛 Debug Avançado

#### Verificar Status da Câmera
```cpp
// Teste básico da câmera
camera_fb_t * fb = esp_camera_fb_get();
if (fb) {
  Serial.printf("Câmera OK: %dx%d, %d bytes\n", 
    fb->width, fb->height, fb->len);
  esp_camera_fb_return(fb);
} else {
  Serial.println("Erro na câmera!");
}
```

#### Verificar Memória
```cpp
Serial.printf("Heap livre: %d bytes\n", ESP.getFreeHeap());
Serial.printf("PSRAM livre: %d bytes\n", ESP.getFreePsram());
Serial.printf("Heap mínimo: %d bytes\n", ESP.getMinFreeHeap());
```

#### Verificar WiFi
```cpp
Serial.printf("Status WiFi: %d\n", WiFi.status());
Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
Serial.printf("RSSI: %d dBm\n", WiFi.RSSI());
Serial.printf("Canal: %d\n", WiFi.channel());
```

### 🔗 Links Úteis

- **ESP32-CAM**: [Documentação oficial](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)
- **Arduino ESP32**: [Board Manager](https://github.com/espressif/arduino-esp32)
- **Camera Library**: [ESP32 Camera](https://github.com/espressif/esp32-camera)

### 📖 Documentação Técnica

- **ESP32-CAM Pinout**: [Pinagem detalhada](https://randomnerdtutorials.com/esp32-cam-pinout-gpio-pins/)
- **Camera Configuration**: [Configurações avançadas](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)
- **WiFi Configuration**: [Configuração de rede](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi.html)

### 📋 Checklist de Suporte

Antes de pedir ajuda, verifique:
- [ ] Leu a documentação oficial
- [ ] Testou com configurações padrão
- [ ] Verificou pinagem da câmera
- [ ] Confirmou alimentação estável
- [ ] Testou com exemplo básico

---

*Use este código como referência para criar suas próprias aplicações com câmera, streaming e interface web.*
