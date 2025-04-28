import random

class Batalhas:
    
    def __init__(self):
        self.eventos = {'pconv' : 6, 'prodcbugs' : -4, 'btracaousuarios' : 3, 'invirritado' : -6, 'fakenews' : -8}
        self.batalhas_ja_feitas = []
        self.pares = []
        self.par_escolhido = []
        self.vencedores = []
    
    def __validacao_id_evento(self,id):
        return id <= 5 and id >= 1
    
    def __verifica_se_nao_existe_evento(self,ev,startup):
        return ev not in startup.eventos
    
    def __verifica_se_startups_ja_tem_reg_do_ev(self,id_evento):
        ev = list(self.eventos.keys())[id_evento-1]
        return ev in self.par_escolhido[0].eventos and ev in self.par_escolhido[1].eventos
    
    def verifica_se_nao_tem_como_reg_evs(self):
        return self.par_escolhido[0].eventos in list(self.eventos.keys()) and self.par_escolhido[1].eventos in list(self.eventos.keys())
    
    def __verifica_se_startup1_pontos_maior_que_startup2(self):
        return self.par_escolhido[0].pontos > self.par_escolhido[1].pontos
    
    def __atribuicao_evento(self,startup,id_evento):
        if self.__validacao_id_evento(id_evento):
            ev = list(self.eventos.keys())[id_evento-1]
            if self.__verifica_se_nao_existe_evento(ev,startup):
                startup.eventos.append(ev)
                startup.pontos += self.eventos.get(ev)
            else:
                return False
        return True   
    
    def add_batalha_ja_feita(self):
        self.batalhas_ja_feitas.append(self.par_escolhido)
       
    def sortea_pares(self, startups : list):
        if len(startups) > 2:
            random.shuffle(startups)
            self.pares = [[startups[i],startups[i+1]] for i in range(0,len(startups),2)]
        else:
            self.pares = [startups]
    
    def get_vencedor_com_pontos_bonus(self):
        if self.__verifica_se_startup1_pontos_maior_que_startup2():
            self.par_escolhido[0].pontos += 30
            return self.par_escolhido[0]
        else:
            self.par_escolhido[1].pontos += 30
            return self.par_escolhido[1]
            
    def add_vencedor_na_list_vencedores(self,vencedor):
        self.vencedores.append(vencedor)
    
    def remove_vencedor_na_list_vencedores(self,ant_venc):
        self.vencedores.remove(ant_venc)
        
    def set_par_escolhido(self, id_par):
        self.par_escolhido = self.pares[id_par]
    
    def verifica_atribuicao_de_ev(self,id_evento,num_startup):
        startup_escolhida = self.par_escolhido[num_startup]
        if not self.__atribuicao_evento(startup_escolhida,id_evento):
            print('EVENTO JA REGISTRADO NA STARTUP!!')
        if self.__verifica_se_startups_ja_tem_reg_do_ev(id_evento):
            return id_evento
        return -1
    
    def verifica_igualdade_de_pontos(self):
        return self.par_escolhido[0].pontos == self.par_escolhido[1].pontos
    
    def shark_fight(self):
        startup_que_recebera = self.par_escolhido[random.randint(0,1)]
        startup_que_recebera.pontos += 2
    
    def get_pares(self):
        return self.pares
    
    def set_pares_para_prox_fase(self,pares):
        self.pares = pares
    
    def get_par_escolhido(self):
        return self.par_escolhido
    
    def get_feitas(self):
        return self.batalhas_ja_feitas
    
    def get_vencedores(self):
        return self.vencedores    
        

        