#!/usr/bin/env python3
"""
Script de teste para a API YOLO com TTS e Áudio
Testa todos os endpoints e funcionalidades
"""

import requests
import json
import base64
import os
from PIL import Image

# Configurações
API_BASE_URL = "http://localhost:5000"
TEST_IMAGE_PATH = "test_image.jpg"

def create_test_image():
    """Cria uma imagem de teste simples"""
    try:
        # Criar imagem simples 640x640 com cores diferentes
        img = Image.new('RGB', (640, 640), color='white')
        
        # Adicionar algumas formas básicas para simular objetos
        from PIL import ImageDraw
        draw = ImageDraw.Draw(img)
        
        # Retângulo azul (simulando um objeto)
        draw.rectangle([100, 100, 300, 400], fill='blue', outline='black')
        
        # Círculo vermelho (simulando outro objeto)
        draw.ellipse([400, 200, 600, 400], fill='red', outline='black')
        
        # Salvar imagem
        img.save(TEST_IMAGE_PATH)
        print(f"✅ Imagem de teste criada: {TEST_IMAGE_PATH}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar imagem de teste: {e}")
        return False

def test_health_endpoint():
    """Testa o endpoint de saúde da API"""
    print("\n🏥 Testando endpoint de saúde...")
    
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check OK: {data['message']}")
            print(f"   Features: {', '.join(data['features'])}")
            return True
        else:
            print(f"❌ Health check falhou: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API. Verifique se está rodando.")
        return False
    except Exception as e:
        print(f"❌ Erro no health check: {e}")
        return False

def test_info_endpoint():
    """Testa o endpoint de informações da API"""
    print("\nℹ️ Testando endpoint de informações...")
    
    try:
        response = requests.get(f"{API_BASE_URL}/info")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Info endpoint OK: {data['name']}")
            print(f"   Versão: {data['version']}")
            print(f"   Modelo: {data['model']}")
            print(f"   TTS: {data['tts_language']}")
            return True
        else:
            print(f"❌ Info endpoint falhou: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no info endpoint: {e}")
        return False

def test_tts_endpoint():
    """Testa o endpoint TTS"""
    print("\n🔊 Testando endpoint TTS...")
    
    try:
        test_text = "Olá! Este é um teste da API YOLO com TTS!"
        
        payload = {
            'text': test_text,
            'play_audio': True
        }
        
        response = requests.post(f"{API_BASE_URL}/tts", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ TTS endpoint OK: {data['message']}")
            print(f"   Texto: {data['text']}")
            print(f"   Áudio gerado: {data['audio_info']['file_size']} bytes")
            return True
        else:
            print(f"❌ TTS endpoint falhou: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste TTS: {e}")
        return False

def test_detection_endpoint():
    """Testa o endpoint principal de detecção"""
    print("\n🔍 Testando endpoint de detecção...")
    
    if not os.path.exists(TEST_IMAGE_PATH):
        print("❌ Imagem de teste não encontrada")
        return False
    
    try:
        # Preparar arquivo para upload
        with open(TEST_IMAGE_PATH, 'rb') as f:
            files = {'image': f}
            
            response = requests.post(f"{API_BASE_URL}/detect", files=files)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Detecção bem-sucedida!")
            print(f"   Mensagem: {data['message']}")
            print(f"   Objetos detectados: {len(data['detections'])}")
            print(f"   Resposta de texto: {data['response_text'][:100]}...")
            print(f"   Total de objetos: {data['total_objects']}")
            print(f"   Áudio gerado: {data['audio_generated']}")
            
            return True
        else:
            print(f"❌ Detecção falhou: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste de detecção: {e}")
        return False

def test_base64_endpoint():
    """Testa o endpoint de detecção com base64"""
    print("\n📱 Testando endpoint base64...")
    
    if not os.path.exists(TEST_IMAGE_PATH):
        print("❌ Imagem de teste não encontrada")
        return False
    
    try:
        # Converter imagem para base64
        with open(TEST_IMAGE_PATH, 'rb') as f:
            image_data = f.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')
        
        # Enviar requisição
        payload = {'image': base64_image}
        response = requests.post(f"{API_BASE_URL}/detect-base64", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Detecção base64 bem-sucedida!")
            print(f"   Objetos detectados: {len(data['detections'])}")
            print(f"   Áudio gerado: {data['audio_generated']}")
            return True
        else:
            print(f"❌ Detecção base64 falhou: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste base64: {e}")
        return False

def cleanup():
    """Limpa arquivos de teste"""
    try:
        if os.path.exists(TEST_IMAGE_PATH):
            os.remove(TEST_IMAGE_PATH)
            print(f"🧹 Arquivo de teste removido: {TEST_IMAGE_PATH}")
    except Exception as e:
        print(f"⚠️ Erro ao limpar arquivo de teste: {e}")

def main():
    """Função principal de teste"""
    print("🧪 Iniciando testes da API YOLO com TTS e Áudio...")
    print("=" * 60)
    
    # Criar imagem de teste
    if not create_test_image():
        print("❌ Falha ao criar imagem de teste. Abortando testes.")
        return
    
    try:
        # Testar endpoints
        tests_passed = 0
        total_tests = 5
        
        if test_health_endpoint():
            tests_passed += 1
        
        if test_info_endpoint():
            tests_passed += 1
        
        if test_tts_endpoint():
            tests_passed += 1
        
        if test_detection_endpoint():
            tests_passed += 1
        
        if test_base64_endpoint():
            tests_passed += 1
        
        # Resumo dos testes
        print("\n" + "=" * 60)
        print(f"📊 RESULTADO DOS TESTES: {tests_passed}/{total_tests} passaram")
        
        if tests_passed == total_tests:
            print("🎉 Todos os testes passaram! API está funcionando perfeitamente.")
            print("🔊 TTS e reprodução de áudio funcionando!")
        else:
            print("⚠️ Alguns testes falharam. Verifique os logs acima.")
        
    except KeyboardInterrupt:
        print("\n⏹️ Testes interrompidos pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado durante os testes: {e}")
    finally:
        # Limpeza
        cleanup()
        print("\n✨ Testes concluídos!")

if __name__ == "__main__":
    main()
