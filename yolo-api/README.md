# 🚀 API YOLO com TTS e Áudio - Detecção de Objetos Inteligente

Uma API Python completa que utiliza YOLO para detecção de objetos, gera respostas personalizadas em português e reproduz áudio automaticamente.

## ✨ Características

- **🔍 Detecção de Objetos**: Utiliza YOLOv8 para detectar mais de 80 tipos de objetos
- **💬 Respostas Personalizadas**: Mensagens naturais e contextuais para diferentes objetos
- **🔊 TTS Automático**: Converte texto em áudio usando Google Text-to-Speech
- **🎵 Reprodução de Áudio**: Toca o áudio automaticamente na API
- **📱 Múltiplos Formatos**: Aceita imagens via upload ou base64
- **⚡ API REST**: Endpoints simples e intuitivos
- **🧪 Testes Automatizados**: Script de teste incluído
- **🇧🇷 Idioma Português**: Respostas e áudio em português brasileiro

## 🏗️ Arquitetura do Projeto

```
📁 Projeto YOLO com TTS
├── 📁 yolo-api/              # API Python principal
│   ├── app.py                 # API principal Flask com TTS
│   ├── yolo_detector.py       # Detector YOLO
│   ├── response_generator.py  # Gerador de respostas personalizadas
│   ├── tts_generator.py       # Sistema TTS e reprodução de áudio
│   ├── test_api.py           # Script de testes
│   ├── example_client.py      # Cliente de exemplo Python
│   ├── requirements.txt       # Dependências Python
│   └── README.md             # Documentação da API
│
└── 📁 arduino-examples/       # Exemplos Arduino
    ├── esp32_cam_yolo_client.ino  # Cliente ESP32-CAM
    └── README.md              # Documentação Arduino
```

## 🚀 Instalação

### 1. Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Sistema de áudio funcional (para reprodução)

### 2. Instalar Dependências

```bash
cd yolo-api
pip install -r requirements.txt
```

### 3. Executar a API

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

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
  "features": ["object_detection", "tts", "audio_playback"]
}
```

### ℹ️ Informações da API
```http
GET /info
```
Retorna informações sobre a API e endpoints disponíveis.

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

### 🔊 Texto para Fala (TTS)
```http
POST /tts
Content-Type: application/json

{
  "text": "Texto para converter em áudio",
  "play_audio": true
}
```

## 🎯 Objetos Suportados

A API detecta mais de 80 tipos de objetos, incluindo:

### 🐱 Objetos com Mensagens Personalizadas
- **Pessoas**: "Olá! Vejo uma pessoa na imagem!"
- **Carros**: "Uau! Vejo um carro na imagem!"
- **Cachorros**: "Au au! Vejo um cachorro!"
- **Gatos**: "Miau! Vejo um gato!"
- **Livros**: "Interessante! Vejo um livro!"
- **Laptops**: "Tecnologia! Vejo um laptop!"
- **Celulares**: "Comunicação! Vejo um celular!"

### 🔧 Objetos Genéricos
Todos os outros objetos detectados pelo YOLO recebem mensagens genéricas inteligentes.

## 🔊 Funcionalidades de Áudio

### TTS Automático
- **Geração**: Usa Google Text-to-Speech para converter texto em áudio
- **Idioma**: Português brasileiro (configurável)
- **Qualidade**: Áudio MP3 de alta qualidade
- **Reprodução**: Toca automaticamente na API

### Controle de Áudio
- **Reprodução automática**: Áudio toca após detecção
- **Controle manual**: Endpoint `/tts` para TTS sob demanda
- **Configuração**: Velocidade e idioma ajustáveis

## 📱 Uso com ESP32-CAM

### 📁 Exemplos Arduino
Os exemplos de código Arduino estão na pasta `arduino-examples/`:

- **`esp32_cam_yolo_client.ino`**: Cliente completo para ESP32-CAM
- **`README.md`**: Documentação detalhada dos exemplos Arduino

### 🔧 Configuração Rápida
1. **Abra o arquivo Arduino** na pasta `arduino-examples/`
2. **Configure WiFi** e IP da API
3. **Faça upload** para o ESP32-CAM
4. **Monitore** via Serial Monitor

### 📊 Funcionamento
- ESP32-CAM captura imagens automaticamente
- Envia para a API via endpoint `/detect-base64`
- API detecta objetos e gera resposta em português
- **Áudio é reproduzido automaticamente na API**
- Resposta JSON retorna todas as informações

## 🧪 Testando a API

### 1. Executar Script de Teste

```bash
python test_api.py
```

### 2. Teste Manual com cURL

```bash
# Health check
curl http://localhost:5000/health

# Informações da API
curl http://localhost:5000/info

# Upload de imagem
curl -X POST -F "image=@sua_imagem.jpg" http://localhost:5000/detect

# Base64
curl -X POST -H "Content-Type: application/json" \
  -d '{"image":"base64_string_aqui"}' \
  http://localhost:5000/detect-base64

# TTS
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"Olá! Teste de TTS!"}' \
  http://localhost:5000/tts
```

### 3. Teste com Cliente Python

```bash
python example_client.py
```

## ⚙️ Configuração

### Configurações Padrão

- **Porta**: 5000
- **Host**: 0.0.0.0 (aceita conexões de qualquer IP)
- **Modelo YOLO**: yolov8n.pt (baixado automaticamente)
- **Threshold de confiança**: 0.5
- **Formatos suportados**: PNG, JPG, JPEG, GIF, BMP
- **TTS**: Português brasileiro
- **Reprodução de áudio**: Automática

### Personalização

Para alterar configurações, edite diretamente os valores no código:

```python
# Em tts_generator.py
self.language = 'pt'  # Alterar idioma
self.slow = False     # Alterar velocidade

# Em yolo_detector.py
self.conf_threshold = 0.5  # Alterar threshold

# Em app.py
UPLOAD_FOLDER = 'uploads'  # Alterar pasta de uploads
```

## 🔧 Solução de Problemas

### Erro: "Modelo YOLO não encontrado"
- O modelo será baixado automaticamente na primeira execução
- Verifique a conexão com a internet

### Erro: "Conexão recusada"
- Verifique se a porta 5000 está livre
- Use `netstat -an | grep 5000` para verificar

### Erro: "Sistema de áudio não disponível"
- Verifique se o sistema tem áudio configurado
- A API funcionará sem reprodução de áudio
- Verifique se o pygame está instalado corretamente

### Performance Lenta
- Use modelo YOLOv8n (mais rápido) em vez de YOLOv8x
- Reduza o threshold de confiança
- Processe imagens menores

## 📊 Monitoramento

### Logs da API
- Todos os logs são exibidos no console
- Inclui informações sobre detecções, TTS e áudio
- Status do sistema de áudio

### Métricas
- Tempo de resposta por requisição
- Número de objetos detectados
- Confiança das detecções
- Status do TTS e reprodução de áudio

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 🙏 Agradecimentos

- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLOv8
- [Flask](https://flask.palletsprojects.com/) - Framework web
- [OpenCV](https://opencv.org/) - Processamento de imagem
- [gTTS](https://github.com/pndurette/gTTS) - Google Text-to-Speech
- [Pygame](https://www.pygame.org/) - Reprodução de áudio

## 📞 Suporte

- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/yolo-api/issues)
- 📖 Wiki: [Documentação completa](https://github.com/seu-usuario/yolo-api/wiki)

---

**Desenvolvido com ❤️ para ESP32-CAM e detecção inteligente de objetos com áudio!**

## 🆕 Funcionalidades de Áudio

- ✅ **TTS Automático**: Gera áudio a partir do texto das detecções
- ✅ **Reprodução Automática**: Toca o áudio na API automaticamente
- ✅ **Endpoint TTS**: `/tts` para conversão manual de texto para áudio
- ✅ **Controle de Áudio**: Opção de gerar sem reproduzir
- ✅ **Limpeza Automática**: Remove arquivos temporários de áudio
- ✅ **Sistema Robusto**: Funciona mesmo sem sistema de áudio

## 📁 Estrutura do Projeto

- **`yolo-api/`**: API Python principal com TTS e áudio
- **`arduino-examples/`**: Exemplos de código para ESP32-CAM
- **Separação clara** entre backend Python e exemplos Arduino
- **Documentação específica** para cada parte do projeto
