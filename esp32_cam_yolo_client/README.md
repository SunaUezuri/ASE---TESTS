# 📱 Exemplos Arduino para API YOLO com TTS

Esta pasta contém exemplos de código Arduino para integração com a API YOLO com TTS e reprodução de áudio.

## 🚀 Projetos Disponíveis

### 1. **ESP32-CAM YOLO Client** (`esp32_cam_yolo_client.ino`)
- **Descrição**: Cliente completo para ESP32-CAM que captura imagens e envia para a API
- **Funcionalidades**:
  - Captura automática de imagens a cada 10 segundos
  - Conversão para base64
  - Envio para API YOLO
  - Processamento de resposta JSON
  - Integração com TTS automático da API

## 📋 Requisitos

### Hardware
- **ESP32-CAM** (qualquer modelo)
- **Cabo USB** para programação
- **Conexão WiFi** estável

### Bibliotecas Arduino
```cpp
#include "esp_camera.h"        // ESP32-CAM
#include <WiFi.h>              // WiFi
#include <HTTPClient.h>         // HTTP Client
#include <base64.h>            // Base64 encoding
#include <ArduinoJson.h>       // JSON parsing
```

### Instalação das Bibliotecas
1. Abra o Arduino IDE
2. Vá em **Sketch > Include Library > Manage Libraries**
3. Instale as seguintes bibliotecas:
   - `ESP32` (se não estiver instalada)
   - `ArduinoJson` por Benoit Blanchon
   - `base64` por Arturo Guadalupi

## ⚙️ Configuração

### 1. **Configurar WiFi**
```cpp
const char* ssid = "SUA_REDE_WIFI";
const char* password = "SUA_SENHA_WIFI";
```

### 2. **Configurar IP da API**
```cpp
const char* apiUrl = "http://SEU_IP:5000/detect-base64";
```
**Substitua `SEU_IP` pelo IP do computador onde a API está rodando**

### 3. **Ajustar Intervalo de Detecção**
```cpp
const int detectionInterval = 10000; // 10 segundos
```

## 🔧 Como Usar

### 1. **Preparar o ESP32-CAM**
- Conecte o ESP32-CAM ao computador
- Selecione a placa correta no Arduino IDE
- Configure as opções de upload se necessário

### 2. **Configurar o Código**
- Abra o arquivo `.ino` desejado
- Ajuste as configurações WiFi e IP da API
- Salve o arquivo

### 3. **Fazer Upload**
- Clique em **Upload** no Arduino IDE
- Aguarde a compilação e upload
- Abra o **Serial Monitor** (115200 baud)

### 4. **Monitorar Funcionamento**
- O ESP32-CAM se conectará ao WiFi
- A câmera será inicializada
- Imagens serão capturadas automaticamente
- Respostas da API aparecerão no Serial Monitor

## 📊 Saída do Serial Monitor

```
🚀 ESP32-CAM YOLO API Client
📸 Sistema de Detecção de Objetos com TTS
📷 Configurando câmera...
✅ Câmera inicializada com sucesso!
📶 Conectando ao WiFi...
✅ WiFi conectado!
📡 Endereço IP: 192.168.1.100
🎯 Sistema pronto para detecção de objetos!
📸 Capturando imagens a cada 10 segundos...
🔊 O áudio será reproduzido automaticamente na API!

🔍 Iniciando nova detecção...
📸 Imagem capturada: 640x480, 15420 bytes
🔢 Imagem convertida para base64: 20560 caracteres
📤 Enviando imagem para API YOLO...
📥 Resposta recebida: 200
🎯 Objetos detectados: 2
   1. person (0.95) - à esquerda e no meio, médio
   2. chair (0.87) - à direita e na parte inferior, pequeno
💬 Resposta da API: Olá! Vejo uma pessoa na imagem! Uma pessoa à esquerda e no meio da imagem. Detectei 1 chair na imagem!
🔊 Este texto foi convertido em áudio na API!
🎵 Áudio gerado e reproduzido com sucesso na API!
✅ Detecção concluída com sucesso!
```

## 🔍 Funcionalidades

### **Captura Automática**
- Imagens capturadas a cada 10 segundos
- Qualidade configurável (SVGA/UXGA)
- Conversão automática para base64

### **Comunicação com API**
- Envio via HTTP POST
- Formato JSON com imagem base64
- Processamento de resposta completa

### **Integração TTS**
- **Não é necessário configurar TTS no ESP32-CAM**
- A API gera e reproduz o áudio automaticamente
- Status do áudio retornado na resposta

### **Tratamento de Erros**
- Reconexão WiFi automática
- Validação de respostas da API
- Logs detalhados no Serial Monitor

## ⚠️ Solução de Problemas

### **WiFi não conecta**
- Verifique credenciais
- Confirme força do sinal
- Reinicie o ESP32-CAM

### **Câmera não funciona**
- Verifique conexões físicas
- Confirme seleção da placa correta
- Verifique biblioteca ESP32-CAM

### **API não responde**
- Confirme IP da API
- Verifique se a API está rodando
- Teste conectividade de rede

### **Erro de memória**
- Reduza qualidade da imagem
- Aumente intervalo entre detecções
- Use modelo YOLO menor

## 📚 Exemplos de Uso

### **Monitoramento de Segurança**
- Detecção de pessoas em áreas restritas
- Alertas automáticos via TTS da API
- Logs de todas as detecções

### **Contagem de Objetos**
- Monitoramento de estoque
- Contagem de pessoas em eventos
- Análise de tráfego

### **Automação Residencial**
- Detecção de movimento
- Alertas de presença
- Controle de iluminação

## 🔗 Integração com API

### **Endpoint Utilizado**
```
POST /detect-base64
Content-Type: application/json

{
  "image": "base64_encoded_image_string"
}
```

### **Resposta Esperada**
```json
{
  "message": "Objetos detectados com sucesso!",
  "detections": [...],
  "response_text": "Texto em português",
  "audio_generated": true,
  "audio_info": {...}
}
```

## 🚀 Próximos Passos

1. **Configure o ESP32-CAM** com suas credenciais WiFi
2. **Ajuste o IP da API** no código
3. **Faça upload** para o ESP32-CAM
4. **Monitore** o funcionamento via Serial Monitor
5. **Ajuste configurações** conforme necessário

## 📞 Suporte

- **Documentação da API**: Veja a pasta `yolo-api/`
- **Problemas de Hardware**: Consulte documentação do ESP32-CAM
- **Problemas de Código**: Verifique logs do Serial Monitor

---

**🎯 Desenvolvido para integração perfeita com a API YOLO com TTS!**
