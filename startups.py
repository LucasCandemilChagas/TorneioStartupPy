import random
import faker

fake = faker.Faker()

verbos = ["Descubra", "Aproveite", "Transforme", "Experimente", "Sinta", "Viva"]
objetos = ["o poder", "a inovação", "a diferença", "a revolução", "a mudança", "o futuro"]


class Startups:
    def __init__(self,nome,slogan,ano_fundacao,numero_de_participantes):
        self.nome = nome
        self.slogan = slogan
        self.ano_fundancao = ano_fundacao
        self.numero_de_participantes = numero_de_participantes
        self.pontos = 70
        self.eventos = []

    def __verifica_se_ja_registrado(self, evento):
        return evento in self.eventos
    
    
    def registra_evento(self, eventos, evento):
        if self.__verifica_se_ja_registrado(evento):
            self.eventos.append(evento)
            self.pontos += eventos.get(evento)
        else:
            return False
        return True

    

class StartupsTeste:
    def __init__(self):
        self.nome = self.__gera_nome()
        self.slogan = self.__gera_slogan()
        self.ano_fundancao = random.randint(1899,2020)
        self.numero_de_participantes = random.randint(4,8)
        self.pontos = 70
        self.eventos = []
        
    
    def __gera_slogan(self):
        return f'{verbos[random.randint(0,len(verbos)-1)]} {objetos[random.randint(0,len(objetos)-1)]}'
        
    
    def __gera_nome(self):
        return fake.company()
    
        
    
    
    

    
    
    
    
