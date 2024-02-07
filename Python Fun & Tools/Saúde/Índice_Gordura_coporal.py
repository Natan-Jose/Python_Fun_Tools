def calcular_igc_homens(soma_dobras_cutaneas, idade):
    """
    Calcula o Índice de Gordura Corporal (IGC) para homens usando a fórmula de Jackson-Pollock.
    """
    if idade >= 17 and idade <= 19:
        constante_a = 1.15
        constante_b = 0.143
        constante_c = 0.157
    elif idade >= 20 and idade <= 29:
        constante_a = 1.15
        constante_b = 0.140
        constante_c = 0.157
    elif idade >= 30 and idade <= 39:
        constante_a = 1.15
        constante_b = 0.137
        constante_c = 0.157
    elif idade >= 40 and idade <= 49:
        constante_a = 1.15
        constante_b = 0.133
        constante_c = 0.157
    elif idade >= 50 and idade <= 59:
        constante_a = 1.15
        constante_b = 0.129
        constante_c = 0.157
    else:
        raise ValueError("Esta fórmula é aplicável apenas para homens entre 17 e 59 anos de idade.")
    
    densidade_corporal = constante_a - (constante_b * soma_dobras_cutaneas)
    igc = ((4.95 / densidade_corporal) - constante_c) * 100
    return igc

def main():
    soma_dobras_cutaneas = float(input("Digite a soma das dobras cutâneas (em milímetros): "))
    idade = int(input("Digite sua idade: "))

    igc = calcular_igc_homens(soma_dobras_cutaneas, idade)

    print(f"Seu Índice de Gordura Corporal (IGC) é aproximadamente {igc:.2f}%.")

if __name__ == "__main__":
    main()
