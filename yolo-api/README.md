# 🚀 API YOLO com TTS e Áudio - Sistema Inteligente de Detecção de Objetos

Uma API Python completa e robusta que utiliza YOLOv8 para detecção de objetos em tempo real, gera respostas personalizadas em português brasileiro e reproduz áudio automaticamente. Ideal para integração com dispositivos IoT, sistemas de vigilância e aplicações de visão computacional.

## 🌟 Visão Geral

A **API YOLO com TTS** é uma solução completa que combina:

- **🔍 Detecção de Objetos**: YOLOv8 para detecção em tempo real
- **💬 Respostas Inteligentes**: Mensagens contextuais em português
- **🔊 Text-to-Speech**: Conversão automática de texto para áudio
- **🎵 Reprodução de Áudio**: Áudio automático na API
- **📱 Múltiplos Formatos**: Suporte a upload, base64 e JPEG binário
- **⚡ API REST**: Endpoints simples e intuitivos
- **🧪 Testes Automatizados**: Scripts de teste incluídos
- **🇧🇷 Idioma Português**: Respostas e áudio em português brasileiro

## 🎯 Casos de Uso

- **Monitoramento de Segurança**: Detecção automática de pessoas e objetos
- **IoT e Dispositivos**: Integração com ESP32-CAM e outros dispositivos
- **Automação Residencial**: Controle inteligente baseado em detecções
- **Educação e Pesquisa**: Demonstração de IA e visão computacional
- **Sistemas de Vigilância**: Análise automática de imagens
- **Controle de Acesso**: Detecção de presença e identificação
- **Análise de Tráfego**: Contagem e classificação de veículos

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐    HTTP POST    ┌─────────────────┐    YOLO + TTS    ┌─────────────────┐
│   Cliente       │ ──────────────► │   API YOLO      │ ──────────────► │   Áudio +       │
│   (ESP32-CAM)   │   JPEG Binary   │   (Flask)       │   Processamento │   Resposta      │
│                 │                 │                 │                 │                 │
│ • Captura       │                 │ • Recebe JPEG   │                 │ • Detecção      │
│ • Envio         │                 │ • YOLOv8        │                 │ • TTS           │
│ • Comunicação   │                 │ • Resposta      │                 │ • Reprodução    │
└─────────────────┘                 └─────────────────┘                 └─────────────────┘
         │                                                                        │
         │                                                                        ▼
         ▼                                                                ┌─────────────────┐
┌─────────────────┐                                                       │   Sistema       │
│   Logs e        │                                                       │   de Áudio      │
│   Monitoramento │                                                       │   (Pygame)      │
└─────────────────┘                                                       └─────────────────┘
```

## 📁 Estrutura do Projeto

```
yolo-api/
├── 📄 app.py                    # API principal Flask com TTS
├── 📄 yolo_detector.py          # Detector YOLO otimizado
├── 📄 response_generator.py     # Gerador de respostas personalizadas
├── 📄 tts_generator.py          # Sistema TTS e reprodução de áudio
├── 📄 requirements.txt           # Dependências Python
├── 📄 yolov8n.pt                # Modelo YOLO (baixado automaticamente)
├── 📄 test_api.py               # Script de testes da API
├── 📄 test_binary_endpoint.py   # Teste específico do endpoint binário
├── 📄 example_client.py         # Cliente de exemplo Python
├── 📄 README.md                 # Este arquivo
├── 📁 uploads/                  # Pasta para uploads temporários
└── 📁 venv/                     # Ambiente virtual Python
```

## 🚀 Funcionalidades Principais

### 🔍 **Detecção de Objetos com YOLOv8**
- **Modelo**: YOLOv8n (nano) para velocidade máxima
- **Classes**: 80+ tipos de objetos detectáveis
- **Precisão**: Threshold configurável de confiança
- **Tempo Real**: Processamento otimizado para baixa latência
- **Múltiplos Objetos**: Detecção simultânea de vários objetos

### 📸 **Múltiplos Formatos de Entrada**
- **`/detect`**: Upload de arquivo de imagem
- **`/detect-base64`**: Imagem codificada em base64
- **`/detect-bin`**: **JPEG binário direto** ⭐ (ideal para ESP32-CAM)
- **Formatos Suportados**: PNG, JPG, JPEG, GIF, BMP, AVIF

### 💬 **Respostas Inteligentes em Português**
- **Idioma**: Português brasileiro nativo
- **Contextual**: Mensagens baseadas nos objetos detectados
- **Personalizadas**: Diferentes mensagens para cada tipo de objeto
- **Posicionamento**: Análise inteligente de posição dos objetos
- **Tamanho**: Classificação automática de tamanho

### 🔊 **Sistema TTS Avançado**
- **Motor**: Google Text-to-Speech (gTTS)
- **Idioma**: Português brasileiro configurável
- **Qualidade**: Áudio MP3 de alta qualidade
- **Velocidade**: Configurável (normal/lenta)
- **Reprodução**: Automática na API
- **Controle**: Endpoint dedicado para TTS

### 🎵 **Reprodução de Áudio**
- **Automática**: Áudio toca após detecção
- **Biblioteca**: Pygame para reprodução multiplataforma
- **Controle**: Opção de gerar sem reproduzir
- **Limpeza**: Remoção automática de arquivos temporários
- **Fallback**: Funciona mesmo sem sistema de áudio

### ⚡ **API REST Otimizada**
- **Framework**: Flask com CORS habilitado
- **Endpoints**: RESTful e intuitivos
- **Respostas**: JSON estruturado e legível
- **Tratamento de Erros**: Mensagens de erro claras
- **Logs**: Sistema de logging detalhado

## 🔧 Configuração e Instalação

### 📋 Pré-requisitos

#### Sistema
- **Python**: 3.8 ou superior
- **pip**: Gerenciador de pacotes Python
- **Sistema de Áudio**: Funcional (para reprodução automática)
- **Memória**: Mínimo 2GB RAM disponível
- **Armazenamento**: 500MB livres para modelo YOLO

#### Rede
- **Porta**: 5000 (configurável)
- **Firewall**: Porta 5000 liberada
- **Acesso**: Rede local ou internet (configurável)

### 🚀 Instalação Rápida

#### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/yolo-api.git
cd yolo-api
```

#### 2. Crie Ambiente Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale Dependências
```bash
pip install -r requirements.txt
```

#### 4. Execute a API
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

### ⚙️ Configurações Avançadas

#### Configurações da API
```python
# Configurações padrão (editar em app.py)
PORT = 5000                    # Porta da API
HOST = '0.0.0.0'              # Host (aceita conexões externas)
UPLOAD_FOLDER = 'uploads'      # Pasta de uploads
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limite
```

#### Configurações YOLO
```python
# Configurações YOLO (editar em yolo_detector.py)
MODEL_PATH = 'yolov8n.pt'     # Caminho do modelo
CONFIDENCE_THRESHOLD = 0.5    # Threshold de confiança
DEVICE = 'cpu'                 # Dispositivo (cpu/cuda)
```

#### Configurações TTS
```python
# Configurações TTS (editar em tts_generator.py)
LANGUAGE = 'pt'                # Idioma (pt = português)
SLOW = False                   # Velocidade (False = normal)
PLAY_AUDIO = True              # Reprodução automática
```

## 📚 Endpoints da API

### 🏥 Health Check
```http
GET /health
```
Verifica se a API está funcionando.

**Resposta:**
```json
{
  "status": "healthy",
  "message": "YOLO API está funcionando!",
  "version": "1.0.0",
  "features": ["object_detection", "tts", "audio_playback"],
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### ℹ️ Informações da API
```http
GET /info
```
Retorna informações sobre a API e endpoints disponíveis.

**Resposta:**
```json
{
  "name": "YOLO API com TTS",
  "version": "1.0.0",
  "description": "API para detecção de objetos com YOLOv8 e TTS",
  "endpoints": [
    "GET /health",
    "GET /info",
    "POST /detect",
    "POST /detect-base64",
    "POST /detect-bin",
    "POST /tts"
  ],
  "supported_formats": ["PNG", "JPG", "JPEG", "GIF", "BMP", "AVIF"],
  "model_info": {
    "name": "YOLOv8n",
    "classes": 80,
    "confidence_threshold": 0.5
  }
}
```

### 🔍 Detecção de Objetos (Upload)
```http
POST /detect
Content-Type: multipart/form-data

image: [arquivo de imagem]
```

**Resposta:**
```json
{
  "message": "Objetos detectados com sucesso!",
  "detections": [
    {
      "class_name": "person",
      "confidence": 0.95,
      "bbox": {
        "x1": 100,
        "y1": 150,
        "x2": 300,
        "y2": 450,
        "center_x": 200,
        "center_y": 300
      },
      "position": "à esquerda e no meio",
      "size": "médio",
      "area": 60000
    }
  ],
  "response_text": "Olá! Vejo uma pessoa na imagem! Uma pessoa à esquerda e no meio da imagem.",
  "total_objects": 1,
  "audio_generated": true,
  "audio_info": {
    "text": "Olá! Vejo uma pessoa na imagem!",
    "language": "pt",
    "file_size": 15420,
    "duration_estimate": 3.5
  },
  "processing_time": 0.85,
  "image_info": {
    "width": 320,
    "height": 240,
    "format": "JPEG",
    "size_bytes": 45230
  }
}
```

### 📱 Detecção de Objetos (Base64)
```http
POST /detect-base64
Content-Type: application/json

{
  "image": "base64_encoded_image_string"
}
```

**Resposta:** Mesmo formato da detecção por upload.

### 🔌 Detecção de Objetos (JPEG Binário)
```http
POST /detect-bin
Content-Type: image/jpeg

[Binary JPEG Data]
```

**Resposta:** Mesmo formato da detecção por upload.

**⭐ Endpoint Principal para ESP32-CAM**

### 🔊 Texto para Fala (TTS)
```http
POST /tts
Content-Type: application/json

{
  "text": "Texto para converter em áudio",
  "play_audio": true,
  "language": "pt",
  "slow": false
}
```

**Resposta:**
```json
{
  "success": true,
  "message": "Áudio gerado com sucesso!",
  "audio_info": {
    "text": "Texto para converter em áudio",
    "language": "pt",
    "slow": false,
    "file_size": 15420,
    "duration_estimate": 3.5,
    "file_path": "temp_audio_12345.mp3"
  },
  "playback": {
    "played": true,
    "duration": 3.2
  }
}
```

## 🎯 Objetos Suportados

### 🐱 Objetos com Mensagens Personalizadas

A API detecta mais de 80 tipos de objetos e gera mensagens personalizadas para:

#### Pessoas e Animais
- **Pessoas**: "Olá! Vejo uma pessoa na imagem!"
- **Cachorros**: "Au au! Vejo um cachorro!"
- **Gatos**: "Miau! Vejo um gato!"
- **Pássaros**: "Piu piu! Vejo um pássaro!"

#### Veículos
- **Carros**: "Uau! Vejo um carro na imagem!"
- **Motos**: "Vrum vrum! Vejo uma moto!"
- **Bicicletas**: "Pedalando! Vejo uma bicicleta!"
- **Ônibus**: "Transporte público! Vejo um ônibus!"

#### Objetos do Cotidiano
- **Livros**: "Interessante! Vejo um livro!"
- **Laptops**: "Tecnologia! Vejo um laptop!"
- **Celulares**: "Comunicação! Vejo um celular!"
- **Cadeiras**: "Mobiliário! Vejo uma cadeira!"

#### Alimentos
- **Maçãs**: "Saudável! Vejo uma maçã!"
- **Pizzas**: "Delicioso! Vejo uma pizza!"
- **Sanduíches**: "Apetitoso! Vejo um sanduíche!"

### 🔧 Objetos Genéricos

Todos os outros objetos detectados pelo YOLO recebem mensagens genéricas inteligentes baseadas em:
- **Tipo de objeto**: "Interessante! Vejo um [objeto]!"
- **Quantidade**: "Vejo [quantidade] [objetos] na imagem!"
- **Posição**: "O [objeto] está [posição]!"
- **Tamanho**: "É um [objeto] [tamanho]!"

## 🔊 Funcionalidades de Áudio

### TTS Automático

#### Geração de Áudio
- **Motor**: Google Text-to-Speech (gTTS)
- **Idioma**: Português brasileiro (configurável)
- **Qualidade**: Áudio MP3 de alta qualidade
- **Velocidade**: Normal ou lenta (configurável)
- **Cache**: Evita regeneração de áudios idênticos

#### Controle de Áudio
- **Reprodução automática**: Áudio toca após detecção
- **Controle manual**: Endpoint `/tts` para TTS sob demanda
- **Configuração**: Velocidade e idioma ajustáveis
- **Fallback**: Funciona mesmo sem sistema de áudio

### Sistema de Reprodução

#### Pygame Integration
- **Biblioteca**: Pygame para reprodução multiplataforma
- **Formatos**: MP3, WAV, OGG
- **Controles**: Play, stop, pause
- **Volume**: Controle de volume configurável

#### Gerenciamento de Arquivos
- **Temporários**: Arquivos de áudio são temporários
- **Limpeza**: Remoção automática após reprodução
- **Nomenclatura**: Nomes únicos para evitar conflitos
- **Monitoramento**: Controle de espaço em disco

## 📱 Uso com ESP32-CAM

### 🔗 Integração Direta

#### Endpoint Binário
```cpp
// ESP32-CAM envia JPEG binário diretamente
const char* apiUrl = "http://SEU_IP:5000/detect-bin";

// Envio HTTP POST
http.addHeader("Content-Type", "image/jpeg");
http.POST(jpegBuffer, jpegSize);
```

#### Resposta Processada
```cpp
// Processar resposta JSON da API
{
  "detections": [...],
  "response_text": "Detectei uma pessoa na imagem!",
  "audio_generated": true
}
```

### 📊 Fluxo de Funcionamento

1. **ESP32-CAM** captura imagem
2. **Envia JPEG** para `/detect-bin`
3. **API processa** com YOLOv8
4. **Gera resposta** em português
5. **Converte para áudio** (TTS)
6. **Reproduz áudio** automaticamente
7. **Retorna JSON** com todas as informações

## 🧪 Testando a API

### 1. Executar Script de Teste

#### Teste Básico
```bash
python test_api.py
```

#### Teste do Endpoint Binário
```bash
python test_binary_endpoint.py
```

#### Teste do Cliente Python
```bash
python example_client.py
```

### 2. Teste Manual com cURL

#### Health Check
```bash
curl http://localhost:5000/health
```

#### Informações da API
```bash
curl http://localhost:5000/info
```

#### Upload de Imagem
```bash
curl -X POST -F "image=@sua_imagem.jpg" http://localhost:5000/detect
```

#### Base64
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"image":"base64_string_aqui"}' \
  http://localhost:5000/detect-base64
```

#### TTS
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"Olá! Teste de TTS!"}' \
  http://localhost:5000/tts
```

### 3. Teste com Cliente Python

#### Cliente de Exemplo
```python
import requests

# Teste de saúde
response = requests.get('http://localhost:5000/health')
print(response.json())

# Teste de detecção
with open('imagem.jpg', 'rb') as f:
    files = {'image': f}
    response = requests.post('http://localhost:5000/detect', files=files)
    print(response.json())
```

## ⚙️ Configuração Avançada

### Configurações de Sistema

#### Variáveis de Ambiente
```bash
# Configurações via variáveis de ambiente
export YOLO_API_PORT=5000
export YOLO_API_HOST=0.0.0.0
export YOLO_MODEL_PATH=yolov8n.pt
export YOLO_CONFIDENCE=0.5
export TTS_LANGUAGE=pt
export TTS_SLOW=false
export AUDIO_PLAYBACK=true
```

#### Arquivo de Configuração
```python
# config.py
import os

class Config:
    PORT = int(os.getenv('YOLO_API_PORT', 5000))
    HOST = os.getenv('YOLO_API_HOST', '0.0.0.0')
    MODEL_PATH = os.getenv('YOLO_MODEL_PATH', 'yolov8n.pt')
    CONFIDENCE_THRESHOLD = float(os.getenv('YOLO_CONFIDENCE', 0.5))
    TTS_LANGUAGE = os.getenv('TTS_LANGUAGE', 'pt')
    TTS_SLOW = os.getenv('TTS_SLOW', 'false').lower() == 'true'
    AUDIO_PLAYBACK = os.getenv('AUDIO_PLAYBACK', 'true').lower() == 'true'
```

### Personalização de Respostas

#### Mensagens Customizadas
```python
# response_generator.py
CUSTOM_MESSAGES = {
    'person': {
        'pt': 'Olá! Vejo uma pessoa na imagem!',
        'en': 'Hello! I see a person in the image!'
    },
    'car': {
        'pt': 'Uau! Vejo um carro na imagem!',
        'en': 'Wow! I see a car in the image!'
    }
}
```

#### Análise de Posição
```python
def analyze_position(bbox, image_width, image_height):
    """Análise inteligente de posição do objeto"""
    center_x = (bbox['x1'] + bbox['x2']) / 2
    center_y = (bbox['y1'] + bbox['y2']) / 2
    
    # Posição horizontal
    if center_x < image_width * 0.33:
        h_pos = "à esquerda"
    elif center_x > image_width * 0.67:
        h_pos = "à direita"
    else:
        h_pos = "no centro"
    
    # Posição vertical
    if center_y < image_height * 0.33:
        v_pos = "no topo"
    elif center_y > image_height * 0.67:
        v_pos = "na parte inferior"
    else:
        v_pos = "no meio"
    
    return f"{h_pos} e {v_pos}"
```

## 🔍 Monitoramento e Logs

### Sistema de Logging

#### Logs Estruturados
```python
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('yolo_api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

#### Logs de Performance
```python
# Logs de performance
logger.info(f"Detecção processada em {processing_time:.2f}s")
logger.info(f"Imagem: {width}x{height}, {size_bytes} bytes")
logger.info(f"Objetos detectados: {len(detections)}")
logger.info(f"TTS gerado: {tts_time:.2f}s")
```

### Métricas de Sistema

#### Monitoramento em Tempo Real
- **Tempo de resposta**: Por requisição
- **Uso de memória**: Heap e PSRAM
- **CPU**: Utilização durante processamento
- **Disco**: Espaço para uploads e áudios
- **Rede**: Bytes enviados/recebidos

#### Health Checks
```python
@app.route('/health')
def health_check():
    """Verificação de saúde do sistema"""
    try:
        # Verificar modelo YOLO
        if not os.path.exists(yolo_detector.model_path):
            return jsonify({'status': 'unhealthy', 'error': 'Modelo YOLO não encontrado'}), 500
        
        # Verificar espaço em disco
        disk_usage = shutil.disk_usage('/')
        if disk_usage.free < 100 * 1024 * 1024:  # 100MB
            return jsonify({'status': 'warning', 'disk_space': 'Baixo'}), 200
        
        return jsonify({'status': 'healthy'}), 200
        
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500
```

## 🚨 Solução de Problemas

### 🔧 Problemas Comuns

#### Erro: "Modelo YOLO não encontrado"
```bash
# Soluções:
# 1. O modelo será baixado automaticamente na primeira execução
# 2. Verifique a conexão com a internet
# 3. Verifique se há espaço em disco
# 4. Execute manualmente: python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

#### Erro: "Conexão recusada"
```bash
# Verificações:
# 1. API está rodando? (python app.py)
# 2. Porta 5000 está livre? (netstat -an | grep 5000)
# 3. Firewall bloqueando?
# 4. IP correto configurado?
```

#### Erro: "Sistema de áudio não disponível"
```bash
# Soluções:
# 1. Verifique se o sistema tem áudio configurado
# 2. API funcionará sem reprodução de áudio
# 3. Verifique se o pygame está instalado: pip install pygame
# 4. Teste com: python -c "import pygame; pygame.mixer.init()"
```

#### Performance Lenta
```bash
# Otimizações:
# 1. Use modelo YOLOv8n (mais rápido) em vez de YOLOv8x
# 2. Reduza o threshold de confiança
# 3. Processe imagens menores
# 4. Use GPU se disponível (CUDA)
```

### 🐛 Debug Avançado

#### Verificar Dependências
```bash
# Verificar instalação
pip list | grep -E "(torch|ultralytics|flask|opencv)"

# Verificar versões
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import ultralytics; print(f'Ultralytics: {ultralytics.__version__}')"
```

#### Teste de Modelo YOLO
```python
# Teste direto do modelo
from ultralytics import YOLO

try:
    model = YOLO('yolov8n.pt')
    print("✓ Modelo YOLO carregado com sucesso!")
    
    # Teste de inferência
    results = model('test_image.jpg')
    print("✓ Inferência funcionando!")
    
except Exception as e:
    print(f"✗ Erro no modelo YOLO: {e}")
```

#### Teste de Sistema de Áudio
```python
# Teste do sistema de áudio
import pygame

try:
    pygame.mixer.init()
    print("✓ Sistema de áudio funcionando!")
    
    # Teste de reprodução
    sound = pygame.mixer.Sound('test.mp3')
    sound.play()
    print("✓ Reprodução funcionando!")
    
except Exception as e:
    print(f"✗ Erro no sistema de áudio: {e}")
```

## 📈 Performance e Otimizações

### ⚡ Otimizações Implementadas

#### YOLO
- **Modelo**: YOLOv8n (nano) para velocidade máxima
- **Threshold**: 0.5 (balanceia precisão e velocidade)
- **Processamento**: Assíncrono para múltiplas requisições
- **Cache**: Modelo carregado uma vez na inicialização

#### API
- **Flask**: Framework leve e rápido
- **CORS**: Habilitado para integração web
- **Uploads**: Processamento em memória
- **Respostas**: JSON otimizado

#### TTS
- **gTTS**: Serviço Google otimizado
- **Cache**: Evita regeneração de áudios
- **Assíncrono**: Não bloqueia a API
- **Limpeza**: Arquivos temporários removidos

### 📊 Métricas de Performance

#### Tempos Típicos
- **Inicialização**: ~5-10 segundos (primeira vez)
- **Carregamento modelo**: ~2-5 segundos
- **Processamento YOLO**: ~200-500ms
- **Geração TTS**: ~1-3 segundos
- **Reprodução áudio**: ~100-300ms
- **Total por requisição**: ~1-4 segundos

#### Uso de Recursos
- **Memória**: ~500MB - 1GB (depende do modelo)
- **CPU**: ~20-60% durante processamento
- **Disco**: ~100-200MB para modelo e áudios
- **Rede**: ~1-10MB por requisição

## 🔒 Segurança e Boas Práticas

### 🛡️ Considerações de Segurança

#### Rede
- **Firewall**: Configure regras apropriadas
- **Porta**: 5000 (considere mudar para produção)
- **Acesso**: Restrinja se necessário
- **HTTPS**: Considere para produção

#### Sistema
- **Uploads**: Validação de tipos de arquivo
- **Tamanho**: Limite de tamanho de arquivo
- **Sanitização**: Validação de entrada
- **Logs**: Não exponha informações sensíveis

### 📋 Boas Práticas

#### Desenvolvimento
- **Ambiente Virtual**: Sempre use venv
- **Dependências**: Mantenha requirements.txt atualizado
- **Versionamento**: Use Git para controle
- **Testes**: Teste sempre antes de deploy

#### Produção
- **Process Manager**: Use systemd ou supervisor
- **Logs**: Configure rotação de logs
- **Monitoramento**: Implemente health checks
- **Backup**: Faça backup das configurações

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
git clone https://github.com/seu-usuario/yolo-api.git

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

# Teste de integração
python test_integration.py
```

### 🔧 Estrutura de Desenvolvimento

#### Organização do Código
```python
# Estrutura recomendada
yolo-api/
├── app.py                 # Ponto de entrada
├── config.py             # Configurações
├── models/               # Modelos ML
├── services/             # Lógica de negócio
├── utils/                # Utilitários
├── tests/                # Testes
└── docs/                 # Documentação
```

#### Padrões de Código
```python
# PEP 8 compliance
# Docstrings para todas as funções
# Type hints quando possível
# Logging estruturado
# Tratamento de erros robusto
```

## 📚 Recursos e Referências

### 🔗 Links Úteis

- **YOLOv8**: [Ultralytics](https://github.com/ultralytics/ultralytics)
- **Flask**: [Documentação oficial](https://flask.palletsprojects.com/)
- **OpenCV**: [Documentação](https://opencv.org/)
- **PyTorch**: [Documentação](https://pytorch.org/)
- **gTTS**: [Google Text-to-Speech](https://github.com/pndurette/gTTS)
- **Pygame**: [Documentação](https://www.pygame.org/)

### 📖 Documentação Técnica

- **YOLO Object Detection**: [Tutorial completo](https://docs.ultralytics.com/)
- **Flask REST API**: [Guia de desenvolvimento](https://flask-restful.readthedocs.io/)
- **Computer Vision**: [OpenCV tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- **Audio Processing**: [Pygame audio](https://www.pygame.org/docs/ref/mixer.html)

### 🎥 Vídeos e Tutoriais

- **YOLOv8 Tutorial**: [Implementação completa]
- **Flask API**: [Desenvolvimento passo a passo]
- **Computer Vision**: [Fundamentos e aplicações]
- **TTS Integration**: [Sistema de áudio]

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

- **Ultralytics**: Pelo YOLOv8 e biblioteca
- **Flask Team**: Pelo framework web
- **OpenCV**: Pelo processamento de imagem
- **Google**: Pelo serviço TTS
- **Pygame**: Pela reprodução de áudio
- **Comunidade Open Source**: Pelo suporte e contribuições

## 📞 Suporte e Contato

### 🆘 Como Obter Ajuda

1. **Issues GitHub**: [Abra uma issue](https://github.com/seu-usuario/yolo-api/issues)
2. **Wiki**: [Documentação completa](https://github.com/seu-usuario/yolo-api/wiki)
3. **Discussions**: [Fórum da comunidade](https://github.com/seu-usuario/yolo-api/discussions)
4. **Email**: [seu-email@exemplo.com]

### 📋 Checklist de Suporte

Antes de abrir uma issue, verifique:
- [ ] Leu a documentação completa
- [ ] Testou com as configurações padrão
- [ ] Verificou os logs de erro
- [ ] Incluiu informações do sistema
- [ ] Descreveu o problema claramente
- [ ] Testou com os scripts de exemplo
- [ ] Verificou dependências instaladas

---

**🌟 Desenvolvido com ❤️ para a comunidade de IA e IoT!**

*Esta API demonstra o poder da combinação entre visão computacional (YOLO), processamento de linguagem natural (TTS) e desenvolvimento web (Flask) para criar sistemas inteligentes de detecção de objetos com feedback de áudio.*
