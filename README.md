# ESP32-CAM YOLO Object Detection

Sistema de detecção de objetos em tempo real usando ESP32-CAM com câmera OV2640 e API YOLO.

## 🚀 Funcionalidades

- **Captura de Imagens**: ESP32-CAM captura imagens JPEG em tempo real
- **Detecção de Objetos**: API YOLO detecta objetos nas imagens
- **Resposta Personalizada**: Gera respostas em português baseadas nas detecções
- **Text-to-Speech**: Converte respostas em áudio e reproduz automaticamente
- **Comunicação Direta**: Envio direto de JPEG binário (sem base64)

## 📁 Estrutura do Projeto

```
ESP32-CAM/
├── CameraWebServer/           # Servidor web da câmera (referência)
├── esp32_cam_yolo_client/     # Cliente ESP32-CAM para YOLO
├── yolo-api/                  # API YOLO com TTS
└── README.md                  # Este arquivo
```

## 🔧 Configuração

### ESP32-CAM (AI-Thinker OV2640)

O ESP32-CAM está configurado para:
- **Resolução**: 320x240 (QVGA)
- **Formato**: JPEG
- **Qualidade**: 10 (alta qualidade)
- **Intervalo**: 5 segundos entre capturas
- **Comunicação**: HTTP POST direto com JPEG binário

#### Pinagem (AI-Thinker)
```
PWDN_GPIO_NUM     32
RESET_GPIO_NUM    -1
XCLK_GPIO_NUM     0
SIOD_GPIO_NUM     26
SIOC_GPIO_NUM     27
Y9_GPIO_NUM       35
Y8_GPIO_NUM       34
Y7_GPIO_NUM       39
Y6_GPIO_NUM       36
Y5_GPIO_NUM       21
Y4_GPIO_NUM       19
Y3_GPIO_NUM       18
Y2_GPIO_NUM       5
VSYNC_GPIO_NUM    25
HREF_GPIO_NUM     23
PCLK_GPIO_NUM     22
LED_GPIO_NUM      4
```

### API YOLO

A API suporta três formas de receber imagens:

1. **`/detect`** - Upload de arquivo de imagem
2. **`/detect-base64`** - Imagem codificada em base64
3. **`/detect-bin`** - **Imagem JPEG binária direta** ⭐

#### Endpoint Principal: `/detect-bin`

```http
POST /detect-bin
Content-Type: image/jpeg

[Binary JPEG Data]
```

**Resposta:**
```json
{
  "message": "Objetos detectados com sucesso!",
  "detections": [
    {
      "class": "person",
      "confidence": 0.95,
      "bbox": [x1, y1, x2, y2]
    }
  ],
  "response_text": "Detectei uma pessoa na imagem",
  "total_objects": 1,
  "audio_generated": true,
  "audio_info": {...}
}
```

## 🚀 Como Usar

### 1. Configurar ESP32-CAM

1. Abra `esp32_cam_yolo_client.ino` no Arduino IDE
2. Configure suas credenciais WiFi:
   ```cpp
   const char* ssid = "SUA_REDE_WIFI";
   const char* password = "SUA_SENHA_WIFI";
   ```
3. Configure a URL da API:
   ```cpp
   const char* apiUrl = "http://SEU_IP:5000/detect-bin";
   ```
4. Faça upload para o ESP32-CAM

### 2. Executar API YOLO

```bash
cd yolo-api
python app.py
```

### 3. Testar Sistema

Execute o script de teste:
```bash
cd yolo-api
python test_binary_endpoint.py
```

## 🔍 Vantagens da Nova Implementação

### ✅ **Antes (Base64)**
- Conversão desnecessária de binário para texto
- Aumento de ~33% no tamanho dos dados
- Processamento adicional no ESP32-CAM
- Maior uso de memória

### 🚀 **Agora (JPEG Direto)**
- **Envio direto** de dados binários
- **Sem conversão** desnecessária
- **Menor uso de memória** no ESP32-CAM
- **Comunicação mais eficiente**
- **Menor latência** na transmissão

## 📊 Monitoramento

O ESP32-CAM inclui indicadores visuais via LED:

- **3 piscadas lentas**: Sistema inicializado
- **LED aceso**: Capturando imagem
- **2 piscadas rápidas**: Sucesso na API
- **3 piscadas lentas**: Erro na comunicação

## 🛠️ Dependências

### ESP32-CAM
- ESP32 Arduino Core
- ESP32 Camera Library

### API YOLO
- Python 3.8+
- Flask
- OpenCV
- PyTorch
- YOLOv8
- gTTS
- pygame

## 🔧 Solução de Problemas

### ESP32-CAM não conecta ao WiFi
- Verifique credenciais WiFi
- Confirme que a rede está disponível

### Erro na API
- Verifique se a API está rodando
- Confirme o IP e porta corretos
- Teste com o script de teste

### Câmera não inicializa
- Verifique a pinagem
- Confirme o modelo da câmera
- Teste com o exemplo básico primeiro

## 📝 Logs

O ESP32-CAM envia logs detalhados via Serial:
- Status da câmera
- Informações da imagem capturada
- Respostas da API
- Erros de comunicação

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ para detecção de objetos em tempo real com ESP32-CAM**
