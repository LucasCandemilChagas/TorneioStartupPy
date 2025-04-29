import random
import time
import os

def limpar_console():
    print(os.name)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Batalhas:
    
    def __init__(self):
        self.eventos = {'pconv' : 6, 'prodcbugs' : -4, 'btracaousuarios' : 3, 'invirritado' : -6, 'fakenews' : -8}
        self.batalhas_ja_feitas = []
        self.pares = []
        self.par_escolhido = []
        self.vencedores = []
    
    
    def menu_pos_selecao_batalha(self,id_par):
        print('Batalha selecionada!!')
        print(f'Par - {self.pares[id_par][0].nome} ({self.pares[id_par][0].pontos}p) vs {self.pares[id_par][1].nome} ({self.pares[id_par][1].pontos}p)')
        print('Escolha umas das startup respectivamente (0-1)')
        print('Para atribuir um evento!!')
        print('Caso queira sair aperte Ctrl+C')
        
    def menu_escolha_de_batalha(self):
        print('Escolha entre essas batalhas')
        for ind, par in enumerate(self.pares):
            if par not in self.get_feitas():  
                print(f'Batalha {ind} - {par[0].nome} vs {par[1].nome}')   
        print('Caso queira sair aperte Ctrl+C')
    
    def display_vencedor(self, vencedor):
        print("Batalha finaizada!!!")
        print(vencedor.nome)  
        print(f'Eh a vencedora!! Com {vencedor.pontos}p')
        
    def get_pares(self):
        return self.pares
    
    def __set_pares_para_prox_fase(self):
        self.sortea_pares(self.get_vencedores())
    
    def get_par_escolhido(self):
        return self.par_escolhido
    
    def get_feitas(self):
        return self.batalhas_ja_feitas
    
    def get_vencedores(self):
        return self.vencedores
        
    def __verifica_igualdade_de_pontos(self):
        return self.par_escolhido[0].pontos == self.par_escolhido[1].pontos

    def __validacao_id_evento(self,id):
        return id <= 5 and id >= 1
    
    def __verifica_se_nao_existe_evento(self,ev,startup):
        return ev not in startup.eventos
    
    def __verifica_se_startups_ja_tem_reg_do_ev(self,id_evento):
        ev = list(self.eventos.keys())[id_evento-1]
        return ev in self.par_escolhido[0].eventos and ev in self.par_escolhido[1].eventos
    
    def __verifica_se_nao_tem_como_reg_evs(self):
        return self.par_escolhido[0].eventos in list(self.eventos.keys()) and self.par_escolhido[1].eventos in list(self.eventos.keys())
    
    def __verifica_se_startup1_pontos_maior_que_startup2(self):
        return self.par_escolhido[0].pontos > self.par_escolhido[1].pontos
    
    
    def __verifica_se_ev_indisp(self,id_ev_ja_reg_nas_startups,mod_menu_ev):
        return id_ev_ja_reg_nas_startups > 0 and mod_menu_ev[id_ev_ja_reg_nas_startups-1] != 1

    def __verifica_se_todas_as_batalhas_teve_vencedor(self,pares):
        return len(self.get_vencedores()) == len(pares) and len(self.get_vencedores()) > 1
    
    def __verifica_termino_da_batalha(self):
        op = input('Deseja terminar batalha? s/qualquer outra tecla: ').lower()
        if op == 's':
            return True
        return False
    
    def __atribuicao_evento(self,startup,id_evento):
        if self.__validacao_id_evento(id_evento):
            ev = list(self.eventos.keys())[id_evento-1]
            if self.__verifica_se_nao_existe_evento(ev,startup):
                startup.eventos.append(ev)
                startup.pontos += self.eventos.get(ev)
            else:
                return False
        return True   
    
    def __verifica_atribuicao_de_ev(self,id_evento,num_startup):
        startup_escolhida = self.par_escolhido[num_startup]
        if not self.__atribuicao_evento(startup_escolhida,id_evento):
            print('EVENTO JA REGISTRADO NA STARTUP!!')
        if self.__verifica_se_startups_ja_tem_reg_do_ev(id_evento):
            return id_evento
        return -1
    
    def __add_batalha_ja_feita(self):
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
            
    def __add_vencedor_na_list_vencedores(self,vencedor):
        self.vencedores.append(vencedor)
    
    def remove_vencedor_na_list_vencedores(self,ant_venc):
        self.vencedores.remove(ant_venc)
        
    def set_par_escolhido(self, id_par):
        self.par_escolhido = self.pares[id_par]
     
    def __list_de_ev_indisp_att(self,id_ev_ja_reg_nas_startups,mod_menu_ev):
        if self.__verifica_se_ev_indisp(id_ev_ja_reg_nas_startups,mod_menu_ev):
            mod_menu_ev[id_ev_ja_reg_nas_startups-1] = 1
        return mod_menu_ev
        
    def __retorna_list_de_ev_indisp_att(self,mod_menu_ev,id_ev_ja_reg_nas_startups):
        return self.__list_de_ev_indisp_att(id_ev_ja_reg_nas_startups,mod_menu_ev)
    
    def __shark_fight(self):
        startup_que_recebera = self.par_escolhido[random.randint(0,1)]
        startup_que_recebera.pontos += 2
    
    def __termino_da_batalha(self,term_bat):
        if term_bat:
            if not self.__verifica_igualdade_de_pontos():
                self.__add_batalha_ja_feita()
                return True
            else: 
                limpar_console()
                print('Startups estao empatadas!')
                print('Shark Fight iniciada!!')
                self.__shark_fight()
                self.__add_batalha_ja_feita()
                time.sleep(5)
                return True
        return False
    
    def __escolhe_prox_startup_da_bat(self,min_regs_atingido):
        startup = int(input('Digite aqui a proxima startup: '))
        min_regs_atingido = 1
        if len(self.get_par_escolhido()[startup].eventos) == 5:
            print('Startup tem todos os eventos ja!!')
        else:
            return True, min_regs_atingido, startup
        if self.__verifica_se_nao_tem_como_reg_evs():
            return True, min_regs_atingido, startup

        return False, 0, startup
    
    def mostra_vencedores_de_rodada(self):
        for venc in self.get_vencedores():
            print(f'{venc.nome} -> {venc.pontos}p')
    
    
    
    def realiza_batalha(self,id_evento,pares,mod_menu_ev,id_par,min_regs_atingido,startup):
    
        id_ev_ja_reg_nas_startups = self.__verifica_atribuicao_de_ev(id_evento,startup)

        list_ev_indisp = self.__retorna_list_de_ev_indisp_att(mod_menu_ev,id_ev_ja_reg_nas_startups)

        self.menu_pos_selecao_batalha(id_par)

        if min_regs_atingido == 1:
            term_bat = self.__verifica_termino_da_batalha()
            if self.__termino_da_batalha(term_bat):
                return True, list_ev_indisp, startup, min_regs_atingido

        while True:
            verf_se_sai_loop, min_regs_atingido, startup = self.__escolhe_prox_startup_da_bat(min_regs_atingido)
            if verf_se_sai_loop:
                break
        return False, list_ev_indisp, startup, min_regs_atingido
    
    
    def realiza_resultados_rodada(self):
        if self.__verifica_se_todas_as_batalhas_teve_vencedor(self.pares):
            print("Vencedor(es) desta rodada sao: ")
            self.__set_pares_para_prox_fase()
            self.mostra_vencedores_de_rodada()
            time.sleep(5)
        elif len(self.get_vencedores()) == 1: # Entra quando tiver um vencedor final
            limpar_console()
            print(f'A startup vencedora do torneio de Startup eh {self.get_vencedores()[0].nome}')
            time.sleep(5)
            return True     
        
    def realiza_resultados_batalha(self):
        vencedor = self.get_vencedor_com_pontos_bonus()
        self.__add_vencedor_na_list_vencedores(vencedor) 
        self.display_vencedor(vencedor)
        print("Por favor aguarde, NAO APERTE NENHUM BOTAO")
        