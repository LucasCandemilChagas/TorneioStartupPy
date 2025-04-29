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
    return [StartupsTeste() for _ in range(4)]

def verifica_quant_de_startups(startups):
    return len(startups) >= 4 and len(startups) % 2 == 0

def verifica_saida():
    op = input('Deseja sair? s/qualquer outra tecla: ').lower()
    if op == 's':
        return True
    return False

def cadastra_startups():
    startups = []
    id = 1
    while True:
        try:
            print(f'Startup {id}')
            nome = input('Digite o Nome da Startup: ')
            slogan = input('Digite o Slogan da Startup: ')
            ano_fundacao = int(input('Digite o Ano de fundacao da Startup: '))
            if ano_fundacao < 1899 or ano_fundacao > 2025:
                raise ValueError
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
    print('Caso queira sair aperte Ctrl+C')
           
while True:
    torneio_acabou = False
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
            elif op == 2:
                quer_sair = 1
            else:
                print('Numero Invalido!!')
        #############################################
        
        if quer_sair:
            break
        
        comecar_batalha = int(input('Digite 1 para comecar as batalhas: '))
        if comecar_batalha == 1:
            b = Batalhas()
            b.sortea_pares(startups_list)
            # Batalhas ################################################
            while True:
                min_regs_atingido = 0 
                
                pares = b.get_pares()
                
                limpar_console()
                
                b.menu_escolha_de_batalha()
                
                while True:
                    id_par = int(input('Digite aqui a batalha desejada: '))
                    if id_par < len(pares):
                        break
                    print('Batalha Invalida!!')
                    
                b.set_par_escolhido(id_par)
                
                limpar_console()
                
                b.menu_pos_selecao_batalha(id_par)
                
                startup = int(input('Digite aqui: '))
                
                mod_menu_ev = [0,0,0,0,0] # Lista que muda a interface de escolha de evento
                
                # Rodada #######################################################
                while True: 
                    menu_de_escolha_eventos(mod_menu_ev)
                    
                    id_evento = int(input(f'Digite aqui para a startup {startup}: '))
                    
                    limpar_console() 
                    ver_batalha_acabada, mod_menu_ev, startup, min_regs_atingido = b.realiza_batalha(id_evento,pares,mod_menu_ev,id_par,min_regs_atingido, startup)
                    if ver_batalha_acabada:
                        break
                    
                    limpar_console()
                ##############################################################################        
                    
                limpar_console()
                
                # Ve quem venceu e mostra na tela ###########################################
                
                b.realiza_resultados_batalha()
                
                time.sleep(5)
                
                torneio_acabou = b.realiza_resultados_rodada()
                
                if torneio_acabou:
                    break
                
                ###################################################################################
                
            ##########################################################################################                       
        limpar_console()
        if torneio_acabou:
            break
    except ValueError:
        continue
    except KeyboardInterrupt:
        print('PROGRAMA ENCERRADO ATE!!')
        break
print('PROGRAMA ENCERRADO ATE!!')