from gtts import gTTS
import io
import tempfile
import os
import pygame
import threading
import time

class TTSGenerator:
    def __init__(self, language='pt', slow=False):
        """
        Inicializa o gerador de TTS
        Args:
            language: Idioma para TTS (pt = português)
            slow: Se deve falar mais devagar
        """
        self.language = language
        self.slow = slow
        
        # Inicializar pygame para reprodução de áudio
        try:
            pygame.mixer.init()
            print("✅ Sistema de áudio inicializado!")
        except Exception as e:
            print(f"⚠️ Aviso: Sistema de áudio não disponível: {e}")
            print("   A API funcionará, mas sem reprodução de áudio")
    
    def generate_and_play(self, text, play_audio=True):
        """
        Gera áudio a partir do texto e reproduz se solicitado
        Args:
            text: Texto para converter em áudio
            play_audio: Se deve reproduzir o áudio
        Returns:
            dict: Informações sobre o áudio gerado
        """
        try:
            print(f"🔊 Gerando áudio para: '{text[:50]}...'")
            
            # Gerar áudio com gTTS
            tts = gTTS(text=text, lang=self.language, slow=self.slow)
            
            # Salvar temporariamente em memória
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                tts.save(temp_file.name)
                temp_path = temp_file.name
            
            # Informações do áudio
            audio_info = {
                'text': text,
                'language': self.language,
                'file_path': temp_path,
                'file_size': os.path.getsize(temp_path),
                'duration_estimate': len(text.split()) * 0.5  # Estimativa: 0.5s por palavra
            }
            
            # Reproduzir áudio se solicitado e disponível
            if play_audio and pygame.mixer.get_init():
                self._play_audio(temp_path)
            
            return audio_info
            
        except Exception as e:
            print(f"❌ Erro ao gerar áudio: {e}")
            return None
    
    def _play_audio(self, audio_path):
        """
        Reproduz o áudio usando pygame
        Args:
            audio_path: Caminho para o arquivo de áudio
        """
        try:
            print("🎵 Reproduzindo áudio...")
            
            # Carregar e reproduzir áudio
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            
            # Aguardar a reprodução terminar
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            print("✅ Áudio reproduzido com sucesso!")
            
        except Exception as e:
            print(f"❌ Erro ao reproduzir áudio: {e}")
        finally:
            # Limpar arquivo temporário
            try:
                os.unlink(audio_path)
            except:
                pass
    
    def play_text(self, text):
        """
        Converte texto em áudio e reproduz imediatamente
        Args:
            text: Texto para converter e reproduzir
        """
        return self.generate_and_play(text, play_audio=True)
    
    def generate_only(self, text):
        """
        Apenas gera o áudio sem reproduzir
        Args:
            text: Texto para converter em áudio
        """
        return self.generate_and_play(text, play_audio=False)
    
    def cleanup(self):
        """Limpa recursos de áudio"""
        try:
            pygame.mixer.quit()
        except:
            pass



