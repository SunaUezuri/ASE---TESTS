#!/usr/bin/env python3
"""
Cliente de exemplo para a API YOLO com TTS e Áudio
Demonstra como usar todos os endpoints da API
"""

import requests
import json
import base64
import os
from PIL import Image

class YOLOAPIClient:
    def __init__(self, base_url="http://localhost:5000"):
        """
        Inicializa o cliente da API
        Args:
            base_url: URL base da API
        """
        self.base_url = base_url
        self.session = requests.Session()
        
        # Configurar headers padrão
        self.session.headers.update({
            'User-Agent': 'YOLO-API-Client/1.0'
        })
    
    def health_check(self):
        """Verifica a saúde da API"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro no health check: {e}")
            return None
    
    def get_info(self):
        """Obtém informações da API"""
        try:
            response = self.session.get(f"{self.base_url}/info")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao obter informações: {e}")
            return None
    
    def text_to_speech(self, text, play_audio=True):
        """
        Converte texto em áudio e reproduz
        Args:
            text: Texto para converter em áudio
            play_audio: Se deve reproduzir o áudio
        Returns:
            dict: Resposta da API ou None se erro
        """
        try:
            print(f"🔊 Convertendo texto para áudio: '{text[:50]}...'")
            
            payload = {
                'text': text,
                'play_audio': play_audio
            }
            
            response = self.session.post(f"{self.base_url}/tts", json=payload)
            response.raise_for_status()
            result = response.json()
            
            print(f"✅ TTS bem-sucedido!")
            print(f"   Mensagem: {result['message']}")
            if 'audio_info' in result:
                print(f"   Tamanho do áudio: {result['audio_info']['file_size']} bytes")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro no TTS: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return None
    
    def detect_from_file(self, image_path):
        """
        Detecta objetos a partir de um arquivo de imagem
        Args:
            image_path: Caminho para o arquivo de imagem
        Returns:
            dict: Resposta da API ou None se erro
        """
        try:
            if not os.path.exists(image_path):
                print(f"❌ Arquivo não encontrado: {image_path}")
                return None
            
            print(f"📤 Enviando imagem: {image_path}")
            
            with open(image_path, 'rb') as f:
                files = {'image': f}
                response = self.session.post(f"{self.base_url}/detect", files=files)
            
            response.raise_for_status()
            result = response.json()
            
            print(f"✅ Detecção bem-sucedida!")
            print(f"   Objetos detectados: {len(result['detections'])}")
            print(f"   Resposta: {result['response_text']}")
            print(f"   Áudio gerado: {result['audio_generated']}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na detecção: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return None
    
    def detect_from_base64(self, image_path):
        """
        Detecta objetos a partir de uma imagem convertida para base64
        Args:
            image_path: Caminho para o arquivo de imagem
        Returns:
            dict: Resposta da API ou None se erro
        """
        try:
            if not os.path.exists(image_path):
                print(f"❌ Arquivo não encontrado: {image_path}")
                return None
            
            print(f"📱 Convertendo imagem para base64: {image_path}")
            
            # Converter imagem para base64
            with open(image_path, 'rb') as f:
                image_data = f.read()
                base64_image = base64.b64encode(image_data).decode('utf-8')
            
            # Preparar payload
            payload = {'image': base64_image}
            
            # Enviar requisição
            response = self.session.post(
                f"{self.base_url}/detect-base64",
                json=payload
            )
            
            response.raise_for_status()
            result = response.json()
            
            print(f"✅ Detecção base64 bem-sucedida!")
            print(f"   Objetos detectados: {len(result['detections'])}")
            print(f"   Áudio gerado: {result['audio_generated']}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na detecção base64: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return None
    
    def create_test_image(self, output_path="test_image.jpg", size=(640, 640)):
        """
        Cria uma imagem de teste simples
        Args:
            output_path: Caminho para salvar a imagem
            size: Tamanho da imagem (largura, altura)
        Returns:
            bool: True se sucesso
        """
        try:
            print(f"🎨 Criando imagem de teste: {output_path}")
            
            # Criar imagem com formas básicas
            img = Image.new('RGB', size, color='white')
            
            from PIL import ImageDraw
            draw = ImageDraw.Draw(img)
            
            # Adicionar formas para simular objetos
            draw.rectangle([100, 100, 300, 400], fill='blue', outline='black', width=3)
            draw.ellipse([400, 200, 600, 400], fill='red', outline='black', width=3)
            draw.rectangle([200, 50, 400, 150], fill='green', outline='black', width=3)
            
            # Adicionar texto
            draw.text((50, 50), "Teste YOLO", fill='black')
            
            # Salvar imagem
            img.save(output_path, quality=95)
            
            print(f"✅ Imagem de teste criada: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar imagem de teste: {e}")
            return False
    
    def run_demo(self):
        """Executa uma demonstração completa da API"""
        print("🚀 Iniciando demonstração da API YOLO com TTS e Áudio...")
        print("=" * 70)
        
        # 1. Health check
        print("\n🏥 1. Verificando saúde da API...")
        health = self.health_check()
        if not health:
            print("❌ API não está respondendo. Verifique se está rodando.")
            return
        
        print(f"✅ API está funcionando: {health['message']}")
        print(f"   Features: {', '.join(health['features'])}")
        
        # 2. Obter informações
        print("\nℹ️ 2. Obtendo informações da API...")
        info = self.get_info()
        if info:
            print(f"✅ API: {info['name']} v{info['version']}")
            print(f"   Modelo: {info['model']}")
            print(f"   TTS: {info['tts_language']}")
        
        # 3. Testar TTS
        print("\n🔊 3. Testando TTS...")
        test_text = "Olá! Esta é uma demonstração da API YOLO com TTS e reprodução de áudio!"
        tts_result = self.text_to_speech(test_text)
        if not tts_result:
            print("❌ Falha no teste TTS.")
            return
        
        # 4. Criar imagem de teste
        print("\n🎨 4. Criando imagem de teste...")
        test_image = "demo_test_image.jpg"
        if not self.create_test_image(test_image):
            print("❌ Falha ao criar imagem de teste.")
            return
        
        # 5. Testar detecção com upload
        print("\n🔍 5. Testando detecção com upload de arquivo...")
        result = self.detect_from_file(test_image)
        if not result:
            print("❌ Falha na detecção com upload.")
            return
        
        # 6. Testar detecção com base64
        print("\n📱 6. Testando detecção com base64...")
        result_base64 = self.detect_from_base64(test_image)
        if not result_base64:
            print("❌ Falha na detecção com base64.")
            return
        
        # 7. Limpeza
        print("\n🧹 7. Limpeza...")
        try:
            if os.path.exists(test_image):
                os.remove(test_image)
                print(f"✅ Arquivo de teste removido: {test_image}")
        except Exception as e:
            print(f"⚠️ Erro ao remover arquivo de teste: {e}")
        
        print("\n🎉 Demonstração concluída com sucesso!")
        print("🔊 TTS e reprodução de áudio funcionando perfeitamente!")
        print("=" * 70)

def main():
    """Função principal"""
    # Criar cliente
    client = YOLOAPIClient()
    
    # Executar demonstração
    client.run_demo()

if __name__ == "__main__":
    main()
