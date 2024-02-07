def calcular_frequencia_cardiaca_maxima(idade):
    """
    Calcula a frequência cardíaca máxima (FCM) utilizando a fórmula 220 - idade.
    """
    return 220 - idade

def calcular_zona_alvo_treinamento(fcm):
    """
    Calcula a zona alvo de treinamento para exercícios aeróbicos,
    que varia de 50% a 85% da frequência cardíaca máxima (FCM).
    """
    zona_min = 0.5 * fcm
    zona_max = 0.85 * fcm
    return zona_min, zona_max

def main():
    idade = int(input("Digite sua idade: "))

    fcm = calcular_frequencia_cardiaca_maxima(idade)
    zona_min, zona_max = calcular_zona_alvo_treinamento(fcm)

    print(f"Sua frequência cardíaca máxima é {fcm} bpm.")
    print(f"Sua zona alvo de treinamento é de {zona_min:.0f} a {zona_max:.0f} bpm.")

if __name__ == "__main__":
    main()
