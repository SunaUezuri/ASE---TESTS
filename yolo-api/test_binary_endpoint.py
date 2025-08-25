#!/usr/bin/env python3
"""
Script de teste para o endpoint /detect-bin
Testa o envio de imagens JPEG binárias para a API
"""

import requests
import time
from PIL import Image
import io
import os

def create_test_image():
    """Cria uma imagem JPEG de teste"""
    # Criar uma imagem simples 320x240
    img = Image.new('RGB', (320, 240), color='red')
    
    # Adicionar um retângulo azul
    for x in range(100, 200):
        for y in range(100, 140):
            img.putpixel((x, y), (0, 0, 255))
    
    # Converter para JPEG
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG', quality=85)
    img_byte_arr.seek(0)
    
    return img_byte_arr.getvalue()

def test_binary_endpoint():
    """Testa o endpoint /detect-bin"""
    url = "http://127.0.0.1:5000/detect-bin"
    
    print("🧪 Testando endpoint /detect-bin")
    print(f"📡 URL: {url}")
    
    # Criar imagem de teste
    print("🖼️  Criando imagem de teste...")
    image_data = create_test_image()
    print(f"📊 Tamanho da imagem: {len(image_data)} bytes")
    
    # Preparar headers
    headers = {
        'Content-Type': 'image/jpeg',
        'User-Agent': 'Test-Script'
    }
    
    try:
        print("📤 Enviando imagem para API...")
        start_time = time.time()
        
        response = requests.post(url, data=image_data, headers=headers)
        
        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # em ms
        
        print(f"⏱️  Tempo de resposta: {response_time:.2f}ms")
        print(f"📥 Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Sucesso! Resposta da API:")
            try:
                result = response.json()
                print(f"   📝 Mensagem: {result.get('message', 'N/A')}")
                print(f"   🎯 Objetos detectados: {result.get('total_objects', 0)}")
                print(f"   🔊 Áudio gerado: {result.get('audio_generated', False)}")
                
                if result.get('detections'):
                    print("   🔍 Detecções:")
                    for det in result['detections']:
                        print(f"      - {det.get('class', 'N/A')}: {det.get('confidence', 0):.2f}")
                        
            except Exception as e:
                print(f"   📄 Resposta (texto): {response.text[:200]}...")
        else:
            print(f"❌ Erro! Resposta: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão: API não está rodando ou não acessível")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def test_health_endpoint():
    """Testa o endpoint de saúde"""
    url = "http://127.0.0.1:5000/health"
    
    print("\n🏥 Testando endpoint /health")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ API está funcionando!")
            result = response.json()
            print(f"   📊 Status: {result.get('status')}")
            print(f"   📝 Mensagem: {result.get('message')}")
            print(f"   🔢 Versão: {result.get('version')}")
        else:
            print(f"❌ API retornou status {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao testar saúde da API: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando testes da API YOLO")
    print("=" * 50)
    
    # Testar saúde da API primeiro
    test_health_endpoint()
    
    print("\n" + "=" * 50)
    
    # Testar endpoint binário
    test_binary_endpoint()
    
    print("\n" + "=" * 50)
    print("🏁 Testes concluídos!")

