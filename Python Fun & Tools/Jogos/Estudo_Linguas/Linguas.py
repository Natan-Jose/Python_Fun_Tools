import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

vocabulario = {
    "casa": {"inglês": "house", "espanhol": "casa", "francês": "maison", "alemão": "haus", "italiano": "casa", "japonês": "家", "coreano": "집"},
    "carro": {"inglês": "car", "espanhol": "coche", "francês": "voiture", "alemão": "auto", "italiano": "auto", "japonês": "車", "coreano": "자동차"},
    "livro": {"inglês": "book", "espanhol": "libro", "francês": "livre", "alemão": "buch", "italiano": "libro", "japonês": "本", "coreano": "책"}
}

import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Função para reproduzir música
def play_music():
    pygame.mixer.music.load("./musica/Y2meta.app - Undertale - Megalovania (Oscar Santos EDM Remix 2019) (128 kbps).mp3")
    pygame.mixer.music.play()

play_music()  # Chamar a função para reproduzir música



def verificar_resposta(palavra, idioma_alvo, resposta_usuario, chances_restantes_label, dica_label):
    resposta_correta = vocabulario[palavra][idioma_alvo]
    if resposta_usuario.strip() == "":
        messagebox.showerror("Resposta Vazia", "Por favor, insira uma resposta antes de verificar.")
    elif resposta_usuario.lower() == resposta_correta.lower():
        messagebox.showinfo("Resultado", "Correto! Parabéns!")
        return True
    else:
        chances_restantes_label["text"] = f"Chances Restantes: {int(chances_restantes_label['text'].split(':')[1]) - 1}"
        if int(chances_restantes_label["text"].split(":")[1]) == 0:
            messagebox.showerror("Resultado", f"Acabaram suas chances. A resposta correta é '{resposta_correta}'.")
        else:
            return False

def obter_dica(palavra, idioma_alvo, dica_label):
    dicas_possiveis = [
        f"Começa com '{vocabulario[palavra][idioma_alvo][0]}'",
        f"Tem {len(vocabulario[palavra][idioma_alvo])} letras"
    ]
    dica = random.choice(dicas_possiveis)
    dica_label.config(text=f"Dica: {dica}")

def praticar_vocabulario(idioma_alvo):
    palavra = random.choice(list(vocabulario.keys()))
    chances_restantes = 4

    janela_pratica = tk.Toplevel()
    janela_pratica.title("Praticar Vocabulário")
    janela_pratica.geometry("300x250")  # Tamanho fixo da janela
    janela_pratica.configure(bg="#BFEFFF")  # Cor de fundo azul claro

    pergunta_label = tk.Label(janela_pratica, text=f"Qual é a tradução da palavra '{palavra}' em {idioma_alvo}?", font=("Arial", 10))
    pergunta_label.pack(pady=10)

    resposta_entry = tk.Entry(janela_pratica, width=30, font=("Arial", 12))
    resposta_entry.pack(pady=10)
    resposta_entry.focus()

    chances_restantes_label = tk.Label(janela_pratica, text=f"Chances Restantes: {chances_restantes}", font=("Arial", 10))
    chances_restantes_label.pack(pady=5)

    dica_label = tk.Label(janela_pratica, text="", font=("Arial", 10))
    dica_label.pack(pady=5)

    def verificar():
        nonlocal chances_restantes
        if chances_restantes > 0:
            if verificar_resposta(palavra, idioma_alvo, resposta_entry.get(), chances_restantes_label, dica_label):
                janela_pratica.destroy()
        if chances_restantes == 1:
            verificar_resposta(palavra, idioma_alvo, resposta_entry.get(), chances_restantes_label, dica_label)
            janela_pratica.destroy()
        chances_restantes -= 1

    verificar_resposta_btn = tk.Button(janela_pratica, text="Verificar Resposta", width=15, font=("Arial", 12),
                                      command=verificar, bg="#9ACD32", fg="black")  # Cor de fundo verde oliva
    verificar_resposta_btn.pack(pady=5)

    dica_btn = tk.Button(janela_pratica, text="Obter Dica", width=15, font=("Arial", 12),
                         command=lambda: obter_dica(palavra, idioma_alvo, dica_label), bg="#FFD700", fg="black")  # Cor de fundo amarelo
    dica_btn.pack(pady=5)

def selecionar_idioma():
    def iniciar_pratica(idioma):
        janela_idioma.destroy()
        praticar_vocabulario(idioma)

    bandeiras = {
        "inglês": "🇺🇸",
        "espanhol": "🇪🇸",
        "francês": "🇫🇷",
        "alemão": "🇩🇪",
        "italiano": "🇮🇹",
        "japonês": "🇯🇵",
        "coreano": "🇰🇷"
    }

    janela_idioma = tk.Toplevel()
    janela_idioma.title("Selecionar Idioma")
    janela_idioma.geometry("300x400")  # Tamanho fixo da janela, ajustado para ser igual à janela principal
    janela_idioma.configure(bg="#BFEFFF")  # Cor de fundo azul claro

    instrucao_label = tk.Label(janela_idioma, text="Selecione o idioma que deseja praticar:", font=("Arial", 12))
    instrucao_label.pack(pady=10)

    for idioma, bandeira in bandeiras.items():
        idioma_btn = tk.Button(janela_idioma, text=f"{bandeira} {idioma.title()}", width=15, font=("Arial", 12),
                               command=lambda idioma=idioma: iniciar_pratica(idioma), bg="#9ACD32", fg="black", relief=tk.RAISED)  # Cor de fundo verde oliva
        idioma_btn.pack(pady=5)


def aplicativo():
    root = tk.Tk()
    root.title("Aplicativo de Estudo de Novas Línguas")
    root.geometry("300x400")  # Tamanho fixo da janela
    root.configure(bg="#BFEFFF")  # Cor de fundo azul claro

   # Carregar a imagem da logo
    logo_img = Image.open("./logoo.png")
    logo_img = logo_img.resize((200, 200))  # Redimensionar a imagem sem especificar o método de suavização

    # Converter a imagem para um objeto PhotoImage
    logo_img = ImageTk.PhotoImage(logo_img)

    # Exibir a imagem da logo em um widget Label
    logo_label = tk.Label(root, image=logo_img, bg="#BFEFFF")
    logo_label.image = logo_img  # Mantém uma referência para a imagem
    logo_label.pack(pady=20) 

  

    boas_vindas_label = tk.Label(root, text="Estudo de Novas Línguas!", font=("Arial", 12), bg="#BFEFFF", padx=10, pady=10)
    boas_vindas_label.pack(pady=20)

    selecionar_idioma_btn = tk.Button(root, text="Selecionar Idioma", width=20, font=("Arial", 12),
                                      command=selecionar_idioma, bg="#9ACD32", fg="black", relief=tk.RAISED)  # Cor de fundo verde oliva
    selecionar_idioma_btn.pack(pady=10)

    root.mainloop()

# Chamar a função principal
aplicativo()

