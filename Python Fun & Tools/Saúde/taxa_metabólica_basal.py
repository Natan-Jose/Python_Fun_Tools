def calcular_tmb(sexo, peso, altura, idade):
    """
    Calcula a Taxa Metabólica Basal (TMB) usando a equação de Harris-Benedict.
    """
    if sexo == 'm':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura * 100) - (5.677 * idade)
    elif sexo == 'f':
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura * 100) - (4.330 * idade)
    else:
        raise ValueError("Sexo deve ser 'm' para masculino ou 'f' para feminino.")
    
    return tmb

def interpretar_tmb(tmb):
    """
    Interpreta a Taxa Metabólica Basal (TMB) e retorna uma mensagem correspondente.
    """
    if tmb < 1200:
        return "Muito baixa - seu corpo pode estar com dificuldades para obter energia suficiente."
    elif tmb < 1500:
        return "Baixa - seu corpo requer uma quantidade mínima de energia para manter as funções vitais."
    elif tmb < 1800:
        return "Moderada - seu corpo tem uma taxa metabólica basal dentro do intervalo normal."
    elif tmb < 2000:
        return "Alta - seu corpo pode estar queimando calorias mais rapidamente do que a média."
    else:
        return "Muito alta - seu corpo pode ter uma taxa metabólica basal significativamente mais alta do que a média."

def main():
    sexo = input("Informe seu sexo (m/f): ").lower()
    peso = float(input("Informe seu peso em quilogramas: "))
    altura = float(input("Informe sua altura em metros: "))
    idade = int(input("Informe sua idade em anos: "))

    tmb = calcular_tmb(sexo, peso, altura, idade)
    interpretacao = interpretar_tmb(tmb)

    print(f"Sua Taxa Metabólica Basal (TMB) é aproximadamente {tmb:.2f} calorias por dia.")
    print("Interpretação:", interpretacao)

if __name__ == "__main__":
    main()
