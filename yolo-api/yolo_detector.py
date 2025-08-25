from ultralytics import YOLO
import os

class YOLODetector:
    def __init__(self, model_path='yolov8n.pt'):
        """
        Inicializa o detector YOLO
        Args:
            model_path: Caminho para o modelo YOLO (usa yolov8n.pt por padrão)
        """
        print(f"🔄 Carregando modelo YOLO: {model_path}")
        
        try:
            # Carregar modelo YOLO
            self.model = YOLO(model_path)
            print("✅ Modelo YOLO carregado com sucesso!")
            
            # Configurar confiança mínima
            self.conf_threshold = 0.5
            
        except Exception as e:
            print(f"❌ Erro ao carregar modelo YOLO: {e}")
            print("📥 Baixando modelo padrão...")
            
            try:
                # Tentar baixar modelo padrão
                self.model = YOLO('yolov8n.pt')
                print("✅ Modelo padrão baixado e carregado!")
            except Exception as e2:
                print(f"❌ Erro fatal ao carregar modelo: {e2}")
                raise e2
    
    def detect(self, image_path):
        """
        Detecta objetos em uma imagem
        Args:
            image_path: Caminho para a imagem
        Returns:
            Lista de detecções com informações dos objetos
        """
        try:
            # Verificar se a imagem existe
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
            
            print(f"🔍 Processando imagem: {image_path}")
            
            # Executar detecção
            results = self.model(image_path, conf=self.conf_threshold)
            
            detections = []
            
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        # Obter coordenadas e confiança
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        confidence = float(box.conf[0].cpu().numpy())
                        class_id = int(box.cls[0].cpu().numpy())
                        
                        # Obter nome da classe
                        class_name = result.names[class_id]
                        
                        # Calcular centro do objeto
                        center_x = int((x1 + x2) / 2)
                        center_y = int((y1 + y2) / 2)
                        
                        # Calcular tamanho relativo
                        width = x2 - x1
                        height = y2 - y1
                        area = width * height
                        
                        # Determinar posição relativa
                        position = self._get_position_description(center_x, center_y)
                        
                        # Determinar tamanho relativo
                        size_description = self._get_size_description(area)
                        
                        detection = {
                            'class_name': class_name,
                            'confidence': round(confidence, 3),
                            'bbox': {
                                'x1': int(x1),
                                'y1': int(y1),
                                'x2': int(x2),
                                'y2': int(y2),
                                'center_x': center_x,
                                'center_y': center_y
                            },
                            'position': position,
                            'size': size_description,
                            'area': int(area)
                        }
                        
                        detections.append(detection)
            
            # Ordenar detecções por confiança (mais alta primeiro)
            detections.sort(key=lambda x: x['confidence'], reverse=True)
            
            print(f"🎯 {len(detections)} objetos detectados")
            for det in detections:
                print(f"   - {det['class_name']} ({det['confidence']:.2f}) - {det['position']}")
            
            return detections
            
        except Exception as e:
            print(f"❌ Erro na detecção: {e}")
            raise e
    
    def _get_position_description(self, center_x, center_y):
        """Determina descrição da posição do objeto na imagem"""
        # Assumindo imagem padrão 640x640 do YOLO
        img_width, img_height = 640, 640
        
        # Normalizar coordenadas
        norm_x = center_x / img_width
        norm_y = center_y / img_height
        
        # Determinar posição horizontal
        if norm_x < 0.33:
            h_pos = "à esquerda"
        elif norm_x < 0.66:
            h_pos = "no centro"
        else:
            h_pos = "à direita"
        
        # Determinar posição vertical
        if norm_y < 0.33:
            v_pos = "na parte superior"
        elif norm_y < 0.66:
            v_pos = "no meio"
        else:
            v_pos = "na parte inferior"
        
        return f"{h_pos} e {v_pos}"
    
    def _get_size_description(self, area):
        """Determina descrição do tamanho do objeto"""
        # Área normalizada (assumindo imagem 640x640)
        norm_area = area / (640 * 640)
        
        if norm_area < 0.01:
            return "muito pequeno"
        elif norm_area < 0.05:
            return "pequeno"
        elif norm_area < 0.15:
            return "médio"
        elif norm_area < 0.3:
            return "grande"
        else:
            return "muito grande"
    
    def get_model_info(self):
        """Retorna informações sobre o modelo carregado"""
        return {
            'model_name': self.model.ckpt_path if hasattr(self.model, 'ckpt_path') else 'yolov8n.pt',
            'confidence_threshold': self.conf_threshold,
            'classes': list(self.model.names.values()) if hasattr(self.model, 'names') else []
        }
