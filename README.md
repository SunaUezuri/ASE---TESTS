# 🚀 ESP32-CAM YOLO Object Detection - Sistema Inteligente de Detecção

Sistema completo de detecção de objetos em tempo real usando ESP32-CAM com câmera OV2640 e API YOLO, incluindo Text-to-Speech e reprodução automática de áudio.

## 🌟 Visão Geral do Projeto

Este projeto implementa um sistema inteligente de detecção de objetos que combina:
- **ESP32-CAM**: Captura de imagens em tempo real
- **YOLOv8**: Detecção de objetos com alta precisão
- **API REST**: Backend Python com Flask
- **Text-to-Speech**: Conversão automática de texto para áudio
- **Reprodução de Áudio**: Áudio automático na API

## 🎯 Casos de Uso

- **Monitoramento de Segurança**: Detecção de pessoas e objetos em tempo real
- **Automação Residencial**: Controle inteligente baseado em detecções
- **IoT Industrial**: Monitoramento de equipamentos e processos
- **Educação**: Demonstração de IA e visão computacional
- **Pesquisa**: Base para projetos de detecção de objetos

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐    HTTP POST    ┌─────────────────┐    YOLO + TTS    ┌─────────────────┐
│   ESP32-CAM     │ ──────────────► │   API YOLO      │ ──────────────► │   Áudio +       │
│   (OV2640)      │   JPEG Binary   │   (Flask)       │   Processamento │   Resposta      │
│                 │                 │                 │                 │                 │
│ • Captura       │                 │ • Recebe JPEG   │                 │ • Detecção      │
│ • WiFi          │                 │ • YOLOv8        │                 │ • TTS           │
│ • HTTP Client   │                 │ • Resposta      │                 │ • Reprodução    │
└─────────────────┘                 └─────────────────┘                 └─────────────────┘
```

## 📁 Estrutura do Projeto

```
ESP32-CAM-YOLO/
├── 📁 CameraWebServer/           # Servidor web da câmera (referência)
│   ├── CameraWebServer.ino       # Código Arduino do servidor web
│   ├── board_config.h            # Configurações da placa
│   ├── camera_pins.h             # Pinagem da câmera
│   ├── camera_index.h            # Interface HTML da câmera
│   ├── app_httpd.cpp             # Servidor HTTP
│   ├── ci.json                   # Configuração CI/CD
│   └── partitions.csv            # Configuração de partições
│
├── 📁 esp32_cam_yolo_client/     # Cliente ESP32-CAM para YOLO
│   ├── esp32_cam_yolo_client.ino # Código principal do cliente
│   └── README.md                 # Documentação específica
│
├── 📁 yolo-api/                  # API YOLO com TTS
│   ├── app.py                    # API principal Flask
│   ├── yolo_detector.py          # Detector YOLO
│   ├── response_generator.py     # Gerador de respostas
│   ├── tts_generator.py          # Sistema TTS
│   ├── requirements.txt           # Dependências Python
│   ├── yolov8n.pt                # Modelo YOLO (baixado automaticamente)
│   ├── test_api.py               # Script de testes
│   ├── example_client.py         # Cliente de exemplo
│   └── README.md                 # Documentação da API
│
└── README.md                     # Este arquivo
```

## 🚀 Funcionalidades Principais

### 🔍 **Detecção de Objetos**
- **YOLOv8**: Modelo de última geração para detecção
- **80+ Classes**: Suporte a mais de 80 tipos de objetos
- **Tempo Real**: Processamento em tempo real
- **Alta Precisão**: Threshold configurável de confiança

### 📸 **Captura de Imagens**
- **Resolução**: 320x240 (QVGA) otimizada para YOLO
- **Formato**: JPEG de alta qualidade
- **Intervalo**: Configurável (padrão: 30 segundos)
- **Otimização**: Configurações de câmera para melhor detecção

### 💬 **Respostas Inteligentes**
- **Português**: Respostas em português brasileiro
- **Contextual**: Mensagens baseadas nos objetos detectados
- **Personalizadas**: Diferentes mensagens para cada tipo de objeto
- **Formatadas**: Informações estruturadas e legíveis

### 🔊 **Sistema de Áudio**
- **TTS Automático**: Google Text-to-Speech
- **Reprodução**: Áudio automático na API
- **Idioma**: Português brasileiro
- **Qualidade**: MP3 de alta qualidade

### 🌐 **Comunicação**
- **HTTP POST**: Envio direto de JPEG binário
- **WiFi**: Conexão WiFi configurável
- **Timeout**: Sistema de timeout para evitar travamentos
- **Retry**: Reconexão automática em caso de falha

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
- **Python 3.8+** (para a API)
- **ESP32 Board Manager** (Arduino)
- **Bibliotecas Python** (veja requirements.txt)

### 🚀 Instalação Rápida

#### 1. Configurar ESP32-CAM
```bash
# 1. Abrir esp32_cam_yolo_client.ino no Arduino IDE
# 2. Configurar WiFi e IP da API
# 3. Selecionar placa "AI Thinker ESP32-CAM"
# 4. Configurar partição "Huge APP"
# 5. Fazer upload
```

#### 2. Executar API YOLO
```bash
cd yolo-api
pip install -r requirements.txt
python app.py
```

#### 3. Testar Sistema
```bash
cd yolo-api
python test_binary_endpoint.py
```

## ⚙️ Configurações Detalhadas

### 🔧 ESP32-CAM

#### Pinagem (AI-Thinker OV2640)
```cpp
// Pinagem padrão para ESP32-CAM AI-Thinker
#define PWDN_GPIO_NUM     32    // Power Down
#define RESET_GPIO_NUM    -1    // Reset (não usado)
#define XCLK_GPIO_NUM     0     // Clock da câmera
#define SIOD_GPIO_NUM     26    // I2C Data
#define SIOC_GPIO_NUM     27    // I2C Clock
#define Y9_GPIO_NUM       35    // D0
#define Y8_GPIO_NUM       34    // D1
#define Y7_GPIO_NUM       39    // D2
#define Y6_GPIO_NUM       36    // D3
#define Y5_GPIO_NUM       21    // D4
#define Y4_GPIO_NUM       19    // D5
#define Y3_GPIO_NUM       18    // D6
#define Y2_GPIO_NUM       5     // D7
#define VSYNC_GPIO_NUM    25    // Vertical Sync
#define HREF_GPIO_NUM     23    // Horizontal Reference
#define PCLK_GPIO_NUM     22    // Pixel Clock
```

#### Configurações de Câmera
```cpp
// Configurações otimizadas para YOLO
const int TARGET_JPEG_QUALITY = 12;     // Qualidade JPEG (10-15 ideal)
const size_t MAX_IMAGE_SIZE = 150000;   // Tamanho máximo (150KB)
const int MIN_FREE_HEAP = 50000;        // Memória mínima livre
const unsigned long captureInterval = 30000; // Intervalo de captura (30s)
```

#### Configurações WiFi
```cpp
const char* ssid = "SUA_REDE_WIFI";
const char* password = "SUA_SENHA_WIFI";
const char* apiUrl = "http://SEU_IP:5000/detect-bin";
```

### 🐍 API YOLO

#### Configurações da API
```python
# Configurações padrão
PORT = 5000
HOST = '0.0.0.0'
MODEL_PATH = 'yolov8n.pt'
CONFIDENCE_THRESHOLD = 0.5
UPLOAD_FOLDER = 'uploads'
```

#### Endpoints Disponíveis
- **`GET /health`**: Verificação de saúde da API
- **`GET /info`**: Informações da API
- **`POST /detect`**: Upload de arquivo de imagem
- **`POST /detect-base64`**: Imagem em base64
- **`POST /detect-bin`**: **JPEG binário direto** ⭐
- **`POST /tts`**: Text-to-Speech sob demanda

## 📊 Exemplos de Uso

### 🔍 Detecção de Objetos

#### Envio via ESP32-CAM
```cpp
// O ESP32-CAM envia automaticamente a cada 30 segundos
// Resposta da API:
{
  "message": "Objetos detectados com sucesso!",
  "detections": [
    {
      "class_name": "person",
      "confidence": 0.95,
      "bbox": {
        "x1": 100, "y1": 150,
        "x2": 300, "y2": 450,
        "center_x": 200, "center_y": 300
      },
      "position": "à esquerda e no meio",
      "size": "médio",
      "area": 60000
    }
  ],
  "response_text": "Olá! Vejo uma pessoa na imagem!",
  "total_objects": 1,
  "audio_generated": true
}
```

#### Teste Manual com cURL
```bash
# Teste de saúde
curl http://localhost:5000/health

# Upload de imagem
curl -X POST -F "image=@imagem.jpg" http://localhost:5000/detect

# TTS manual
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"Olá! Teste de TTS!"}' \
  http://localhost:5000/tts
```

### 🎵 Text-to-Speech

#### Configuração TTS
```python
# Configurações do TTS
language = 'pt'        # Português brasileiro
slow = False           # Velocidade normal
play_audio = True      # Reprodução automática
```

#### Exemplo de Uso
```python
from tts_generator import TTSGenerator

tts = TTSGenerator(language='pt', slow=False)
audio_info = tts.play_text("Detectei uma pessoa na imagem!")
```

## 🔍 Monitoramento e Debug

### 📊 Indicadores Visuais (ESP32-CAM)

#### LED Status
- **3 piscadas lentas**: Sistema inicializado
- **LED aceso**: Capturando imagem
- **2 piscadas rápidas**: Sucesso na API
- **3 piscadas lentas**: Erro na comunicação

#### Serial Monitor
```cpp
// Logs detalhados via Serial
Serial.println("=== RESPOSTA DA API YOLO ===");
Serial.println(response);
Serial.println("=============================");

Serial.println("📊 RESUMO DA DETECÇÃO:");
Serial.printf("Total de objetos: %d\n", totalObjects);
```

### 📝 Logs da API

#### Console Output
```
[INFO] API YOLO iniciada na porta 5000
[INFO] Modelo YOLO carregado: yolov8n.pt
[INFO] Sistema TTS inicializado
[INFO] Recebida imagem: 320x240, 45.2KB
[INFO] Detecção: 2 objetos encontrados
[INFO] TTS gerado: "Detectei uma pessoa e uma cadeira"
[INFO] Áudio reproduzido com sucesso
```

#### Métricas de Performance
- Tempo de resposta por requisição
- Número de objetos detectados
- Confiança das detecções
- Status do TTS e áudio

## 🚨 Solução de Problemas

### 🔧 Problemas Comuns

#### ESP32-CAM não conecta ao WiFi
```cpp
// Soluções:
// 1. Verificar credenciais WiFi
// 2. Confirmar que a rede está disponível
// 3. Verificar força do sinal (RSSI)
// 4. Aumentar timeout de conexão
```

#### Erro na API
```bash
# Verificações:
# 1. API está rodando? (curl /health)
# 2. IP e porta corretos?
# 3. Firewall bloqueando?
# 4. Teste com script de teste
```

#### Câmera não inicializa
```cpp
// Verificações:
// 1. Pinagem correta
// 2. Modelo da câmera (OV2640)
// 3. Alimentação estável (3.3V)
// 4. Teste com exemplo básico primeiro
```

#### Problemas de Memória
```cpp
// Soluções:
// 1. Habilitar PSRAM
// 2. Usar partição "Huge APP"
// 3. Reduzir qualidade JPEG
// 4. Aumentar intervalo de captura
```

### 🐛 Debug Avançado

#### Verificar Memória
```cpp
Serial.printf("Memória livre: %d bytes\n", ESP.getFreeHeap());
Serial.printf("PSRAM livre: %d bytes\n", ESP.getFreePsram());
```

#### Testar Câmera
```cpp
// Teste básico da câmera
camera_fb_t * fb = esp_camera_fb_get();
if (fb) {
  Serial.printf("Imagem: %dx%d, %d bytes\n", 
    fb->width, fb->height, fb->len);
  esp_camera_fb_return(fb);
}
```

#### Verificar WiFi
```cpp
Serial.printf("Status WiFi: %d\n", WiFi.status());
Serial.printf("IP: %s\n", WiFi.localIP().toString().c_str());
Serial.printf("RSSI: %d dBm\n", WiFi.RSSI());
```

## 📈 Performance e Otimizações

### ⚡ Otimizações Implementadas

#### ESP32-CAM
- **Qualidade JPEG**: 12 (balanceia qualidade e tamanho)
- **Resolução**: QVGA (320x240) para YOLO
- **Timeout**: 20 segundos para evitar travamentos
- **Memória**: Verificação de memória livre
- **WiFi**: Desabilita sleep mode para estabilidade

#### API YOLO
- **Modelo**: YOLOv8n (mais rápido)
- **Threshold**: 0.5 (balanceia precisão e velocidade)
- **Processamento**: Assíncrono para múltiplas requisições
- **Cache**: Modelo carregado uma vez na inicialização

### 📊 Métricas de Performance

#### Tempos Típicos
- **Captura ESP32-CAM**: ~100ms
- **Envio WiFi**: ~500ms (depende da rede)
- **Processamento YOLO**: ~200ms
- **Geração TTS**: ~1s
- **Reprodução Áudio**: ~100ms

#### Total por Ciclo
- **Tempo total**: ~2 segundos
- **Intervalo recomendado**: 30 segundos
- **Throughput**: ~2 imagens/minuto

## 🔒 Segurança e Boas Práticas

### 🛡️ Considerações de Segurança

#### Rede
- **WiFi**: Use WPA2/WPA3
- **API**: Restrinja acesso se necessário
- **Firewall**: Configure regras apropriadas

#### Dados
- **Imagens**: Não são armazenadas permanentemente
- **Logs**: Contêm informações de debug
- **API**: Endpoints públicos (configure conforme necessário)

### 📋 Boas Práticas

#### Desenvolvimento
- **Versionamento**: Use Git para controle de versão
- **Testes**: Teste sempre antes de deploy
- **Documentação**: Mantenha READMEs atualizados
- **Logs**: Use logs estruturados

#### Produção
- **Monitoramento**: Implemente health checks
- **Backup**: Faça backup das configurações
- **Updates**: Mantenha dependências atualizadas
- **Escalabilidade**: Considere load balancing se necessário

## 🤝 Contribuição e Desenvolvimento

### 🚀 Como Contribuir

1. **Fork** o projeto
2. **Clone** o repositório
3. **Crie** uma branch para sua feature
4. **Desenvolva** e teste sua funcionalidade
5. **Commit** suas mudanças
6. **Push** para a branch
7. **Abra** um Pull Request

### 🧪 Desenvolvimento Local

#### Ambiente de Desenvolvimento
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/esp32-cam-yolo.git

# 2. Configure o ambiente Python
cd yolo-api
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute em modo desenvolvimento
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows
python app.py
```

#### Testes
```bash
# Executar todos os testes
python -m pytest

# Teste específico
python test_api.py

# Teste de performance
python test_performance.py
```

## 📚 Recursos e Referências

### 🔗 Links Úteis

- **ESP32-CAM**: [Documentação oficial](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)
- **YOLOv8**: [Ultralytics](https://github.com/ultralytics/ultralytics)
- **Flask**: [Documentação oficial](https://flask.palletsprojects.com/)
- **Arduino**: [ESP32 Board Manager](https://github.com/espressif/arduino-esp32)

### 📖 Documentação Técnica

- **ESP32-CAM Pinout**: [Pinagem detalhada](https://randomnerdtutorials.com/esp32-cam-pinout-gpio-pins/)
- **YOLO Object Detection**: [Tutorial completo](https://docs.ultralytics.com/)
- **Flask REST API**: [Guia de desenvolvimento](https://flask-restful.readthedocs.io/)

### 🎥 Vídeos e Tutoriais

- **Configuração ESP32-CAM**: [Tutorial passo a passo]
- **Integração YOLO**: [Demonstração completa]
- **Sistema TTS**: [Funcionalidades de áudio]

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

- **Espressif Systems**: Pelo ESP32-CAM
- **Ultralytics**: Pelo YOLOv8
- **Flask Team**: Pelo framework web
- **Google**: Pelo serviço TTS
- **Comunidade Open Source**: Pelo suporte e contribuições

## 📞 Suporte e Contato

### 🆘 Como Obter Ajuda

1. **Issues GitHub**: [Abra uma issue](https://github.com/seu-usuario/esp32-cam-yolo/issues)
2. **Wiki**: [Documentação completa](https://github.com/seu-usuario/esp32-cam-yolo/wiki)
3. **Discussions**: [Fórum da comunidade](https://github.com/seu-usuario/esp32-cam-yolo/discussions)
4. **Email**: [seu-email@exemplo.com]

### 📋 Checklist de Suporte

Antes de abrir uma issue, verifique:
- [ ] Leia a documentação completa
- [ ] Testou com as configurações padrão
- [ ] Verificou os logs de erro
- [ ] Incluiu informações do sistema
- [ ] Descreveu o problema claramente

---

**🌟 Desenvolvido com ❤️ para a comunidade de IoT e IA!**

*Este projeto demonstra o poder da combinação entre hardware IoT (ESP32-CAM) e inteligência artificial (YOLO) para criar sistemas inteligentes de detecção de objetos em tempo real.*
