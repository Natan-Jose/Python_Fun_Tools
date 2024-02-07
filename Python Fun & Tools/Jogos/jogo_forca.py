import random

def escolher_palavra_e_dica():
    palavras_e_dicas = {
        "python": "Uma linguagem de programação popular.",
        "javascript": "Uma linguagem de script para páginas web.",
        "java": "Uma linguagem de programação versátil.",
        "ruby": "Uma linguagem dinâmica e orientada a objetos.",
        "html": "Usada para criar a estrutura de páginas web.",
        "css": "Usada para estilizar páginas web.",
        "php": "Uma linguagem de script server-side.",
        "csharp": "Uma linguagem de programação da Microsoft.",
        "cplusplus": "Uma linguagem de programação de propósito geral.",
        "swift": "Uma linguagem de programação desenvolvida pela Apple.",
        "kotlin": "Uma linguagem de programação moderna para Android.",
        "typescript": "Um superset de JavaScript que adiciona tipagem estática.",
        "sql": "Uma linguagem de consulta estruturada para banco de dados.",
        "r": "Uma linguagem de programação estatística e ambiente de software.",
        "django": "Um framework web de alto nível em Python.",
        "react": "Uma biblioteca JavaScript para construir interfaces de usuário.",
        "angular": "Um framework JavaScript mantido pelo Google para construir aplicativos web.",
        "wordpress": "Um sistema de gerenciamento de conteúdo para criação de sites.",
        "flutter": "Um kit de desenvolvimento de interface de usuário da Google para criar aplicativos nativos compilados.",
        "docker": "Uma plataforma para desenvolvimento, envio e execução de aplicativos em contêineres.",
        "ansible": "Uma ferramenta de automação de TI para provisionamento, configuração, gerenciamento e orquestração de sistemas.",
        "terraform": "Uma ferramenta de infraestrutura como código para construir, alterar e versionar infraestrutura com segurança e eficiência.",
        "kubernetes": "Uma plataforma de código aberto projetada para automatizar a implantação, o dimensionamento e a operação de aplicativos em contêineres.",
        "raspberrypi": "Um computador de placa única do tamanho de um cartão de crédito, que pode ser usado para vários fins.",
        "arduino": "Uma plataforma de eletrônica de prototipagem de hardware de código aberto baseada em software e hardware flexíveis e fáceis de usar.",
        "tensorflow": "Uma biblioteca de código aberto para aprendizado de máquina e aprendizado profundo.",
        "opencv": "Uma biblioteca de código aberto de visão computacional e aprendizado de máquina.",
        "numpy": "Uma biblioteca para a linguagem de programação Python, que adiciona suporte para arrays e matrizes multidimensionais de grande tamanho, junto com uma grande coleção de funções matemáticas de alto nível para operar nesses arrays.",
        "pandas": "Uma biblioteca de software escrita para a linguagem de programação Python para manipulação e análise de dados.",
        "matplotlib": "Uma biblioteca de plotagem para a linguagem de programação Python e sua extensão de matemática NumPy."
    }
    palavra = random.choice(list(palavras_e_dicas.keys()))
    dica = palavras_e_dicas[palavra]
    return palavra, dica

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_forca():
    palavra_secreta, dica = escolher_palavra_e_dica()
    letras_corretas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Dica:", dica)
    mostrar_forca(palavra_secreta, letras_corretas)

    while tentativas > 0:
        letra_tentativa = input("Digite uma letra: ").lower()

        if letra_tentativa in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
        elif letra_tentativa in palavra_secreta:
            letras_corretas.add(letra_tentativa)
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")

        mostrar_forca(palavra_secreta, letras_corretas)

        if set(palavra_secreta) == letras_corretas:
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas == 0:
        print(f"Fim de jogo! A palavra era '{palavra_secreta}'.")

if __name__ == "__main__":
    jogar_forca()
