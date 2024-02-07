import random

tabuleiro = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

def exibir_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))

def verificar_vitoria_linha(jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    return False

def verificar_vitoria_coluna(jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
    return False

def verificar_vitoria_diagonal(jogador):
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogar():
  
    jogador_atual = 'X' if random.randint(0, 1) == 0 else 'O'

    while True:
 
        exibir_tabuleiro()

        print(f'Jogador {jogador_atual}, sua vez.')
        entrada_jogador = input('Digite a linha e a coluna: ')
        linha, coluna = entrada_jogador.split()
        linha = int(linha)
        coluna = int(coluna)
        
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print('Entrada inválida.')
            continue

        if tabuleiro[linha][coluna] != ' ':
            print('Posição ocupada.')
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria_linha(jogador_atual):
            print(f'O jogador {jogador_atual} venceu!')
            break
        elif verificar_vitoria_coluna(jogador_atual):
            print(f'O jogador {jogador_atual} venceu!')
            break
        elif verificar_vitoria_diagonal(jogador_atual):
            print(f'O jogador {jogador_atual} venceu!')
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

    if not verificar_vitoria_linha(jogador_atual) and not verificar_vitoria_coluna(jogador_atual) and not verificar_vitoria_diagonal(jogador_atual):
        print('O jogo empatou!')

def main():
    jogar()

if __name__ == '__main__':
    main()
