from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64
from PIL import Image
import io
import uuid
from yolo_detector import YOLODetector
from response_generator import ResponseGenerator
from tts_generator import TTSGenerator

app = Flask(__name__)

# Configurar CORS
CORS(app)

# Configurações da aplicação
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Criar pasta de uploads se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Inicializar componentes
yolo_detector = YOLODetector()
response_generator = ResponseGenerator()
tts_generator = TTSGenerator(language='pt', slow=False)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de verificação de saúde da API"""
    return jsonify({
        'status': 'healthy',
        'message': 'YOLO API está funcionando!',
        'version': '1.0.0',
        'features': ['object_detection', 'tts', 'audio_playback']
    })

@app.route('/detect', methods=['POST'])
def detect_objects():
    """Endpoint principal para detecção de objetos"""
    try:
        # Verificar se há arquivo na requisição
        if 'image' not in request.files:
            return jsonify({'error': 'Nenhuma imagem enviada'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Tipo de arquivo não suportado'}), 400
        
        # Salvar imagem temporariamente
        temp_filename = f"{uuid.uuid4()}_{file.filename}"
        temp_path = os.path.join(UPLOAD_FOLDER, temp_filename)
        file.save(temp_path)
        
        try:
            # Detectar objetos com YOLO
            detections = yolo_detector.detect(temp_path)
            
            # Gerar resposta personalizada
            response_text = response_generator.generate_response(detections)
            
            # Gerar e reproduzir áudio
            audio_info = tts_generator.play_text(response_text)
            
            # Limpar arquivo temporário
            os.remove(temp_path)
            
            return jsonify({
                'message': 'Objetos detectados com sucesso!' if detections else 'Nenhum objeto detectado',
                'detections': detections,
                'response_text': response_text,
                'total_objects': len(detections),
                'audio_generated': audio_info is not None,
                'audio_info': audio_info
            })
            
        except Exception as e:
            # Limpar arquivo temporário em caso de erro
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise e
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/detect-base64', methods=['POST'])
def detect_objects_base64():
    """Endpoint para receber imagens em base64"""
    try:
        data = request.get_json()
        
        if not data or 'image' not in data:
            return jsonify({'error': 'Dados de imagem não fornecidos'}), 400
        
        # Decodificar imagem base64
        try:
            image_data = base64.b64decode(data['image'])
            image = Image.open(io.BytesIO(image_data))
            
            # Salvar temporariamente
            temp_filename = f"{uuid.uuid4()}.jpg"
            temp_path = os.path.join(UPLOAD_FOLDER, temp_filename)
            image.save(temp_path, 'JPEG')
            
        except Exception as e:
            return jsonify({'error': 'Formato de imagem base64 inválido'}), 400
        
        try:
            # Detectar objetos
            detections = yolo_detector.detect(temp_path)
            
            # Gerar resposta
            response_text = response_generator.generate_response(detections)
            
            # Gerar e reproduzir áudio
            audio_info = tts_generator.play_text(response_text)
            
            # Limpar arquivo temporário
            os.remove(temp_path)
            
            return jsonify({
                'message': 'Objetos detectados com sucesso!' if detections else 'Nenhum objeto detectado',
                'detections': detections,
                'response_text': response_text,
                'total_objects': len(detections),
                'audio_generated': audio_info is not None,
                'audio_info': audio_info
            })
            
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise e
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/detect-bin', methods=['POST'])
def detect_objects_binary():
    """Endpoint para receber imagens JPEG binárias diretamente"""
    try:
        # Verificar se há dados na requisição
        if not request.data:
            return jsonify({'error': 'Nenhuma imagem enviada'}), 400
        
        # Verificar o Content-Type
        if request.content_type != 'image/jpeg':
            return jsonify({'error': 'Content-Type deve ser image/jpeg'}), 400
        
        # Obter dados binários da imagem
        image_data = request.data
        
        # Salvar imagem temporariamente
        temp_filename = f"{uuid.uuid4()}.jpg"
        temp_path = os.path.join(UPLOAD_FOLDER, temp_filename)
        
        with open(temp_path, 'wb') as f:
            f.write(image_data)
        
        try:
            # Detectar objetos com YOLO
            detections = yolo_detector.detect(temp_path)
            
            # Gerar resposta personalizada
            response_text = response_generator.generate_response(detections)
            
            # Gerar e reproduzir áudio
            audio_info = tts_generator.play_text(response_text)
            
            # Limpar arquivo temporário
            os.remove(temp_path)
            
            return jsonify({
                'message': 'Objetos detectados com sucesso!' if detections else 'Nenhum objeto detectado',
                'detections': detections,
                'response_text': response_text,
                'total_objects': len(detections),
                'audio_generated': audio_info is not None,
                'audio_info': audio_info
            })
            
        except Exception as e:
            # Limpar arquivo temporário em caso de erro
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise e
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/tts', methods=['POST'])
def text_to_speech():
    """Endpoint para converter texto em áudio e reproduzir"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        text = data['text']
        play_audio = data.get('play_audio', True)
        
        # Gerar e reproduzir áudio
        audio_info = tts_generator.generate_and_play(text, play_audio=play_audio)
        
        if audio_info:
            return jsonify({
                'message': 'Áudio gerado e reproduzido com sucesso!',
                'text': text,
                'audio_info': audio_info
            })
        else:
            return jsonify({'error': 'Falha ao gerar áudio'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/info', methods=['GET'])
def get_api_info():
    """Endpoint para informações da API"""
    return jsonify({
        'name': 'YOLO Object Detection API with TTS',
        'version': '1.0.0',
        'description': 'API para detecção de objetos usando YOLO com TTS e reprodução de áudio',
        'endpoints': {
            'health': 'GET /health - Verificação de saúde',
            'detect': 'POST /detect - Upload de imagem',
            'detect-base64': 'POST /detect-base64 - Imagem em base64',
            'detect-bin': 'POST /detect-bin - Imagem JPEG binária',
            'tts': 'POST /tts - Texto para fala',
            'info': 'GET /info - Informações da API'
        },
        'features': {
            'object_detection': 'YOLOv8 para detecção de objetos',
            'tts': 'Google Text-to-Speech para geração de áudio',
            'audio_playback': 'Reprodução automática de áudio',
            'personalized_responses': 'Respostas personalizadas em português'
        },
        'supported_formats': list(ALLOWED_EXTENSIONS),
        'model': 'YOLOv8',
        'tts_language': 'pt (português)'
    })

if __name__ == '__main__':
    print("🚀 Iniciando API YOLO com TTS e Áudio...")
    print("📱 Endpoints disponíveis:")
    print("   - POST /detect - Upload de imagem")
    print("   - POST /detect-base64 - Imagem em base64")
    print("   - POST /detect-bin - Imagem JPEG binária")
    print("   - POST /tts - Texto para fala")
    print("   - GET /health - Verificação de saúde")
    print("   - GET /info - Informações da API")
    print("\n🎯 Modelo YOLO carregando...")
    print("🔊 Sistema de áudio inicializando...")
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        # Limpeza ao finalizar
        tts_generator.cleanup()
