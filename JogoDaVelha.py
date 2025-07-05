'''
Jogo da Velha
Desenvolvido por: Ellis Moura
2025.06.04
'''

msgsInicio    = ['Bem-vindo ao Jogo da Velha', 'Você é o "X" e o computador é o "O"', 'Jogo dessenvolvido por Ellis Moura']
msgJogador    = 'Jogador começa a Jogada'
msgComputador = 'Computador começa a Jogada'

from module import CriaTabuleiro, MostraCabecalho, SorteiaJogador, MostraQuemComeca, MostraTabuleiro, JogadaUsuario, JogadaComputador, VerificaVitoria, JogarNovamente

def JogarJogoVelha():
    tabuleiro = CriaTabuleiro()
    
    MostraCabecalho(msgsInicio)

    vez        = SorteiaJogador(msgJogador, msgComputador)
    msgJogarUm = {vez.capitalize()}
    
    MostraQuemComeca(msgJogarUm)

    while True: #while true pois quero que fique até a vitório ou empate acontecer
        MostraTabuleiro(tabuleiro)

        if vez == msgJogador:
            JogadaUsuario(tabuleiro)
            if VerificaVitoria(tabuleiro, "X"):
                MostraTabuleiro(tabuleiro)
                print("Parabéns! Você venceu! \O/")
                break #caso o jogador seja vencedor sai do laço
            vez = msgComputador  # próxima vez é do computador
        else:
            JogadaComputador(tabuleiro)
            if VerificaVitoria(tabuleiro, "O"):
                MostraTabuleiro(tabuleiro)
                print("O computador venceu! :(")
                break #caso o camputador seja o vencedor sai do laço
            vez = msgJogador  # próxima vez é do jogador

        # Verifica empate
        if " " not in tabuleiro:
            MostraTabuleiro(tabuleiro)
            print("Deu velha! Empate!")
            break

    if JogarNovamente():
       JogarJogoVelha()

JogarJogoVelha()