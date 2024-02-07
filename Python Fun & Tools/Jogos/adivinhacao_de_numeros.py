import random

def jogo_adivinhacao():
    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas_maximas = 10
    tentativas_realizadas = 0

    print("Bem-vindo ao Jogo de Adivinhação de Números!")
    print(f"Tente adivinhar o número entre 1 e 100. Você tem {tentativas_maximas} tentativas.")

    while tentativas_realizadas < tentativas_maximas:
        # Obter o palpite do jogador
        palpite = int(input("Digite seu palpite: "))
        tentativas_realizadas += 1

        # Verificar se o palpite está correto
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas_realizadas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    # Se o jogador não acertou dentro do número máximo de tentativas
    if palpite != numero_secreto:
        print(f"Fim do jogo! O número correto era {numero_secreto}.")

# Iniciar o jogo de Adivinhação de Números
jogo_adivinhacao()
