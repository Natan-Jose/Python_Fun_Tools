import random

def criar_baralho():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def calcular_pontuacao(mao):
    pontuacao = sum(mao)
    if 11 in mao and pontuacao > 21:
        mao.remove(11)
        mao.append(1)
    return pontuacao

def jogo_blackjack():
    baralho = criar_baralho()
    random.shuffle(baralho)

    jogador = [baralho.pop(), baralho.pop()]
    computador = [baralho.pop()]

    while True:
        print(f"Jogador: {jogador} (Pontuação: {calcular_pontuacao(jogador)})")
        escolha = input("Deseja comprar mais uma carta? (S/N): ").upper()

        if escolha == 'S':
            jogador.append(baralho.pop())
            if calcular_pontuacao(jogador) > 21:
                print("Você estourou! Fim do jogo.")
                break
        else:
            while calcular_pontuacao(computador) < 17:
                computador.append(baralho.pop())

            print(f"Jogador: {jogador} (Pontuação: {calcular_pontuacao(jogador)})")
            print(f"Computador: {computador} (Pontuação: {calcular_pontuacao(computador)})")

            if calcular_pontuacao(jogador) > 21 or (calcular_pontuacao(computador) <= 21 and calcular_pontuacao(computador) > calcular_pontuacao(jogador)):
                print("Computador venceu!")
            else:
                print("Você venceu!")

            break

# Iniciar o jogo de Blackjack
jogo_blackjack()
