import random

def CriaTabuleiro():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "] #pode ser substituído por return [" " for _ in range(9)], mas acho q fica mais legível

def MostraCabecalho(msgsInicio):
    print('=' * 40)
    for msg in msgsInicio:
        print(f'{msg:^40}')
    print('=' * 40)

def MostraQuemComeca(jogadorInicial):
    for msg in jogadorInicial:
        print(f'{msg:^40}')
    print('-' * 40)

def SorteiaJogador(msgJogador, msgComputador):
    return random.choice([msgJogador, msgComputador]) # Sorteia quem começa

def MostraTabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

def VerificaVitoria(tabuleiro, jogador):
    #Verifica Linha, Coluna e Diagonal ex se tabuleiro[a 0][b 1][c 2] forem iguais a X é sinal q a primeira linha ta com x
    for a, b, c in [
       (0,1,2), (3,4,5), (6,7,8),
       (0,3,6), (1,4,7), (2,5,8),
       (0,4,8), (2,4,6)
    ]:
       if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador:
          return True
    return False

def JogadaUsuario(tabuleiro):
    while True: #while true pois quero q fique infinitamente aqui, até ser digitado o valor certo
        try:
            pos = int(input("Escolha uma posição (1-9): ")) - 1 #Como o array começa em 0 subtrai 1
            if 0 <= pos <= 8 and tabuleiro[pos] == " ": #Verifica se posição é vazia
                tabuleiro[pos] = "X"
                break #Quando o valor ta certo ele da break para sair desse laço
            else:
                print("Posição inválida ou ocupada! Tente novamente.")
        except ValueError: #Verifica se é um número INTEIRO
            print("Digite um número válido!")

def JogadaComputador(tabuleiro):
    # Primeiro, verifica se pode vencer se puder ele vence
    for i in range(9): #O range percorre todas as posições
        if tabuleiro[i] == " ": #Verifica se ta vazia
            tabuleiro[i] = "O"  #
            if VerificaVitoria(tabuleiro, "O"):
                return
            tabuleiro[i] = " "  # desfaz jogada

    # Depois, verifica se precisa bloquear o jogador Isso faz o jogo ficar impossível
    #"""Computador joga de forma mais inteligente"""
    #for i in range(9):
    #    if tabuleiro[i] == " ":
    #        tabuleiro[i] = "X"
    #        if VerificaVitoria(tabuleiro, "X"):
    #            tabuleiro[i] = "O"
    #            return
    #        tabuleiro[i] = " "  # desfaz jogada

    # Se o meio estiver livre, joga no meio
    if tabuleiro[4] == " ":
        tabuleiro[4] = "O"
        return

    # Se tiver canto livre, escolhe um aleatório
    cantos = [i for i in [0,2,6,8] if tabuleiro[i] == " "]
    if cantos:
        escolha = random.choice(cantos)
        tabuleiro[escolha] = "X"
        if VerificaVitoria(tabuleiro, "X"):
           tabuleiro[escolha] = "O"
           return
        tabuleiro[escolha] = " "

    # Se não, joga em qualquer posição livre
    livres = [i for i, v in enumerate(tabuleiro) if v == " "] #enumarate enumera as casas vazias do tabuleiro
    if livres:
        tabuleiro[random.choice(livres)] = "O" #escolhe uma casa aleatória e preenche

def JogarNovamente():
    resposta = input('Deseja jogar novamente? (s/n): ').strip().lower()
    
    while not resposta in ['s', 'n']:
      resposta = input('Deseja jogar novamente? (s/n): ').strip().lower() 
    return resposta == 's'