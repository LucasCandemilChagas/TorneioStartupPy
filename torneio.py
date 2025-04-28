import random
import os
import time

from startups import Startups
from startups import StartupsTeste
from batalhas import Batalhas


def limpar_console():
    print(os.name)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def defini_quantidade_startups_TESTE():
    return [StartupsTeste() for _ in range(random.choice([4,6,8]))]

def verifica_quant_de_startups(startups):
    return len(startups) >= 4 and len(startups) % 2 == 0

def verifica_termino_da_batalha():
    op = input('Deseja terminar batalha? s/qualquer outra tecla: ').lower()
    if op == 's':
        return True
    return False

def verifica_saida():
    op = input('Deseja sair? s/qualquer outra tecla: ').lower()
    if op == 's':
        return True
    return False

def verifica_se_ja_foi_reg_evento_nas_startups(id_ev_ja_reg_nas_startups,mod_menu_ev):
    if id_ev_ja_reg_nas_startups > 0 and mod_menu_ev[id_ev_ja_reg_nas_startups-1] != 1:
        mod_menu_ev[id_ev_ja_reg_nas_startups-1] = 1



def cadastra_startups():
    startups = []
    id = 1
    while True:
        try:
            print(f'Startup {id}')
            nome = input('Digite o Nome da Startup: ')
            slogan = input('Digite o Slogan da Startup: ')
            ano_fundacao = int(input('Digite o Ano de fundacao da Startup: '))
            participantes = int(input('Digite quantas pessoas irao participar (Entre 4 e 8 sendo numero par): '))
            if participantes % 2 != 0:
                raise ValueError
            startups.append(Startups(nome,slogan,ano_fundacao,participantes))
        except ValueError:
            print("Ano esta incorreto ou Numeros de participantes nao permitido")
        else:
            id+=1
        if verifica_quant_de_startups(startups):  
            if verifica_saida():
                break
        
    return startups
           
def menu_inicial():
    print('Startup Rush!!')
    print('Escolha entre as opcoes abaixo:')
    print('1 - Cadastrar Startup')
    print('2 - Sair')

def menu_escolha_de_batalha(pares,batalhas):
    print('Escolha entre essas batalhas')
    for ind, par in enumerate(pares):
        if par not in batalhas.get_feitas():  
            print(f'Batalha {ind} - {par[0].nome} vs {par[1].nome}')
        
def menu_pos_selecao_batalha(op, pares):
    
    print('Batalha selecionada!!')
    print(f'Par - {pares[op][0].nome} ({pares[op][0].pontos}p) vs {pares[op][1].nome} ({pares[op][1].pontos}p)')
    print('Escolha umas das startup respectivamente (0-1)')
    print('Para atribuir um evento!!')

def menu_de_escolha_eventos(mod_menu_ev):
    limpar_console()  
    print('Selecione entre os eventos a seguir:')   
    if not mod_menu_ev[0]: 
        print('1 - Pitch convincente')
    else:
        print('1 - Pitch convincente (indisponivel)    REGISTRADO EM TODAS AS STARTUPS!!')
    if not mod_menu_ev[1]:        
        print('2 - Produto com bugs ')
    else:
        print('2 - Produto com bugs (indisponivel)    REGISTRADO EM TODAS AS STARTUPS!!')
    if not mod_menu_ev[2]:    
        print('3 - Boa tracao de usuarios')  
    else:
        print('3 - Boa tracao de usuarios (indisponivel)    REGISTRADO EM TODAS AS STARTUPS!!')  
    if not mod_menu_ev[3]:    
        print('4 - Investidor irritado')  
    else:
        print('4 - Investidor irritado (indisponivel)    REGISTRADO EM TODAS AS STARTUPS!!')  
    if not mod_menu_ev[4]:    
        print('5 - Fake news no pitch')    
    else: 
        print('5 - Fake news no pitch (indisponivel)    REGISTRADO EM TODAS AS STARTUPS!!')    

def display_vencedor(par):
    print("Batalha finaizada!!!")
    if par[0].pontos > par[1].pontos:
        print(par[0].nome)  
        print(f'Eh a vencedora!! Com {par[0].pontos}p')
    else:
        print(par[1].nome)  
        print(f'Eh a vencedora!! Com {par[1].pontos}p')
    
             

while True:
    min_regs_atingido = 0 
    quer_sair = 0  
    try:
        # Cadastro das Startups ######################
        menu_inicial()
        while True:
            op = int(input('Digite aqui: '))
            if op == 1:
                startups_list = defini_quantidade_startups_TESTE()
                #startups_list = cadastra_startups()
                print('Startups cadastradas!!')
                break
            else:
                print('Numero Invalido!!')
        #############################################
        
        comecar_batalha = int(input('Digite 1 para comecar as batalhas: '))
        if comecar_batalha == 1:
            b = Batalhas()
            b.sortea_pares(startups_list)
            # Batalhas ################################################
            while True:
                pares = b.get_pares()
                limpar_console()
                menu_escolha_de_batalha(pares,b)
                id_par = int(input('Digite aqui a batalha desejada: '))
                b.set_par_escolhido(id_par)
                limpar_console()
                menu_pos_selecao_batalha(id_par,pares)
                startup = int(input('Digite aqui: '))
                
                mod_menu_ev = [0,0,0,0,0]
                # Rodada #######################################################
                while True: 
                    menu_de_escolha_eventos(mod_menu_ev)
                    id_evento = int(input(f'Digite aqui para a startup {startup}: '))
                    limpar_console() 
                    id_ev_ja_reg_nas_startups = b.verifica_atribuicao_de_ev(id_evento,startup)
                    verifica_se_ja_foi_reg_evento_nas_startups(id_ev_ja_reg_nas_startups,mod_menu_ev)
                    menu_pos_selecao_batalha(id_par,pares)
                    if min_regs_atingido == 1:
                        term_bat = verifica_termino_da_batalha()
                        if term_bat:
                            if not b.verifica_igualdade_de_pontos():
                                b.add_batalha_ja_feita()
                                break
                            else: 
                                print('Startups estao empatadas!')
                                print('Shark Fight iniciada!!')
                                b.shark_fight()
                                b.add_batalha_ja_feita()
                                break
                    # Escolha da proxima Startup ##################################
                    while True:
                        startup = int(input('Digite aqui a proxima startup: '))
                        min_regs_atingido = 1
                        if len(b.get_par_escolhido()[startup].eventos) == 5:
                            print('Startup tem todos os eventos ja!!')
                        else:
                            break
                        
                        if b.verifica_se_nao_tem_como_reg_evs():
                            break
                    ################################################################
                    
                    limpar_console()
                ##############################################################################        
                    
                limpar_console()
                display_vencedor(b.get_par_escolhido())
                time.sleep(5) 
                if quer_sair:
                    break   
            ##########################################################################################                       
        print(pares)
        limpar_console() 
    except ValueError:
        continue
    except KeyboardInterrupt:
        print('PROGRAMA ENCERRADO ATE!!')
        break