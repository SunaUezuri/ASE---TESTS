import random
from collections import defaultdict

class ResponseGenerator:
    def __init__(self):
        """Inicializa o gerador de respostas personalizadas"""
        
        # Dicionário de mensagens personalizadas para diferentes tipos de objetos
        self.personalized_messages = {
            'person': {
                'greetings': [
                    "Olá! Vejo uma pessoa na imagem!",
                    "Oi! Tem alguém na foto!",
                    "Detectei uma pessoa! Olá!",
                    "Vejo uma pessoa aqui! Como vai?"
                ],
                'descriptions': [
                    "Uma pessoa {position} da imagem",
                    "Há uma pessoa {position}",
                    "Encontrei uma pessoa {position}"
                ]
            },
            'car': {
                'greetings': [
                    "Uau! Vejo um carro na imagem!",
                    "Olha só! Tem um carro aqui!",
                    "Detectei um veículo automotor!",
                    "Há um carro na foto!"
                ],
                'descriptions': [
                    "Um carro {size} {position} da imagem",
                    "Vejo um carro {size} {position}",
                    "Há um veículo {size} {position}"
                ]
            },
            'dog': {
                'greetings': [
                    "Au au! Vejo um cachorro!",
                    "Que fofo! Tem um cachorro na imagem!",
                    "Detectei um amigo peludo!",
                    "Há um cachorro aqui!"
                ],
                'descriptions': [
                    "Um cachorro {size} {position} da imagem",
                    "Vejo um cachorro {size} {position}",
                    "Há um cão {size} {position}"
                ]
            },
            'cat': {
                'greetings': [
                    "Miau! Vejo um gato!",
                    "Que gracinha! Tem um gato na imagem!",
                    "Detectei um felino!",
                    "Há um gato aqui!"
                ],
                'descriptions': [
                    "Um gato {size} {position} da imagem",
                    "Vejo um gato {size} {position}",
                    "Há um felino {size} {position}"
                ]
            },
            'book': {
                'greetings': [
                    "Interessante! Vejo um livro!",
                    "Olha só! Tem um livro na imagem!",
                    "Detectei material de leitura!",
                    "Há um livro aqui!"
                ],
                'descriptions': [
                    "Um livro {size} {position} da imagem",
                    "Vejo um livro {size} {position}",
                    "Há um livro {size} {position}"
                ]
            },
            'laptop': {
                'greetings': [
                    "Tecnologia! Vejo um laptop!",
                    "Olha só! Tem um computador na imagem!",
                    "Detectei um dispositivo eletrônico!",
                    "Há um laptop aqui!"
                ],
                'descriptions': [
                    "Um laptop {size} {position} da imagem",
                    "Vejo um computador {size} {position}",
                    "Há um laptop {size} {position}"
                ]
            },
            'cell phone': {
                'greetings': [
                    "Comunicação! Vejo um celular!",
                    "Olha só! Tem um telefone na imagem!",
                    "Detectei um dispositivo móvel!",
                    "Há um celular aqui!"
                ],
                'descriptions': [
                    "Um celular {size} {position} da imagem",
                    "Vejo um telefone {size} {position}",
                    "Há um celular {size} {position}"
                ]
            }
        }
        
        # Mensagens genéricas para objetos não personalizados
        self.generic_messages = [
            "Detectei {count} {object_type} na imagem!",
            "Encontrei {count} {object_type}!",
            "Vejo {count} {object_type} aqui!",
            "Há {count} {object_type} na foto!"
        ]
        
        # Mensagens de resumo
        self.summary_messages = [
            "Resumindo, encontrei {total_objects} objetos na imagem!",
            "No total, detectei {total_objects} itens!",
            "A imagem contém {total_objects} objetos diferentes!",
            "Identifiquei {total_objects} elementos na foto!"
        ]
    
    def generate_response(self, detections):
        """
        Gera uma resposta personalizada baseada nas detecções
        Args:
            detections: Lista de detecções do YOLO
        Returns:
            String com resposta personalizada
        """
        if not detections:
            return "Nenhum objeto foi detectado nesta imagem."
        
        # Agrupar detecções por classe
        grouped_detections = defaultdict(list)
        for detection in detections:
            grouped_detections[detection['class_name']].append(detection)
        
        response_parts = []
        
        # Processar cada tipo de objeto
        for object_type, objects in grouped_detections.items():
            count = len(objects)
            
            # Verificar se há mensagens personalizadas para este objeto
            if object_type in self.personalized_messages:
                response_parts.append(self._generate_personalized_response(object_type, objects))
            else:
                # Usar mensagem genérica
                generic_msg = random.choice(self.generic_messages)
                response_parts.append(generic_msg.format(
                    count=count,
                    object_type=self._pluralize(object_type, count)
                ))
        
        # Adicionar resumo final
        total_objects = len(detections)
        summary_msg = random.choice(self.summary_messages)
        response_parts.append(summary_msg.format(total_objects=total_objects))
        
        # Juntar todas as partes
        full_response = " ".join(response_parts)
        
        return full_response
    
    def _generate_personalized_response(self, object_type, objects):
        """Gera resposta personalizada para um tipo específico de objeto"""
        messages = self.personalized_messages[object_type]
        
        # Escolher saudação aleatória
        greeting = random.choice(messages['greetings'])
        
        # Gerar descrições para cada objeto
        descriptions = []
        for obj in objects:
            desc_template = random.choice(messages['descriptions'])
            description = desc_template.format(
                position=obj['position'],
                size=obj['size']
            )
            descriptions.append(description)
        
        # Juntar tudo
        if len(descriptions) == 1:
            return f"{greeting} {descriptions[0]}."
        else:
            # Múltiplos objetos do mesmo tipo
            count = len(objects)
            count_text = self._pluralize(object_type, count)
            return f"{greeting} Encontrei {count} {count_text}: {', '.join(descriptions)}."
    
    def _pluralize(self, word, count):
        """Pluraliza palavras em português de forma simples"""
        if count == 1:
            return word
        
        # Regras básicas de pluralização
        if word.endswith('ão'):
            return word[:-3] + 'ões'
        elif word.endswith('m'):
            return word[:-1] + 'ns'
        elif word.endswith('l'):
            return word[:-1] + 'is'
        elif word.endswith('r'):
            return word + 'es'
        elif word.endswith('z'):
            return word[:-1] + 'zes'
        else:
            return word + 's'
    
    def get_available_objects(self):
        """Retorna lista de objetos que têm mensagens personalizadas"""
        return list(self.personalized_messages.keys())
