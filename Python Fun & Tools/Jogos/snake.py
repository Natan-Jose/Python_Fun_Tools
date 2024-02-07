import pygame
import time
import random

pygame.init()

# Definindo as dimensões do jogo
largura, altura = 800, 600
tamanho_celula = 20

# Definindo cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# Inicializando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Inicializando o relógio
relogio = pygame.time.Clock()

# Função que desenha a cobra na tela
def desenhar_cobra(tamanho_celula, cobra):
    for i, segmento in enumerate(cobra):
        if i == 0:  # Desenha a cabeça com uma cor diferente
            pygame.draw.rect(tela, (0, 0, 255), [segmento[0], segmento[1], tamanho_celula, tamanho_celula])
            pygame.draw.rect(tela, preto, [segmento[0], segmento[1], tamanho_celula, tamanho_celula], 1)  # Adiciona borda
        else:
            pygame.draw.rect(tela, verde, [segmento[0], segmento[1], tamanho_celula, tamanho_celula])

# Função principal do jogo
def jogo():
    jogo_ativo = True
    game_over = False

    # Inicializando a posição inicial da cobra
    cobra = [[largura // 2, altura // 2]]
    cobra_dir = 'RIGHT'

    # Inicializando a posição da comida
    comida = [random.randrange(1, (largura // tamanho_celula)) * tamanho_celula,
              random.randrange(1, (altura // tamanho_celula)) * tamanho_celula]

    # Inicializando a velocidade da cobra
    velocidade = tamanho_celula

    # Inicializando a pontuação
    pontuacao = 0

    while jogo_ativo:
        while game_over:
            tela.fill(branco)
            fonte = pygame.font.SysFont(None, 75)
            mensagem = fonte.render('Game Over! Pontuação: {}'.format(pontuacao), True, vermelho)
            tela.blit(mensagem, [largura // 2 - mensagem.get_width() // 2, altura // 2 - mensagem.get_height() // 2])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jogo_ativo = False
                    game_over = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        jogo_ativo = False
                        game_over = False
                    elif evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not cobra_dir == 'RIGHT':
                    cobra_dir = 'LEFT'
                elif evento.key == pygame.K_RIGHT and not cobra_dir == 'LEFT':
                    cobra_dir = 'RIGHT'
                elif evento.key == pygame.K_UP and not cobra_dir == 'DOWN':
                    cobra_dir = 'UP'
                elif evento.key == pygame.K_DOWN and not cobra_dir == 'UP':
                    cobra_dir = 'DOWN'

        # Verificando se a cobra comeu a comida
        if len(cobra) > 0 and cobra[0] == comida:
            pontuacao += 1  # Aumenta a pontuação
            comida = [random.randrange(1, (largura // tamanho_celula)) * tamanho_celula,
                      random.randrange(1, (altura // tamanho_celula)) * tamanho_celula]

            # Adicionando um novo segmento no final da cobra
            ultimo_segmento = cobra[-1]
            cobra.append([ultimo_segmento[0], ultimo_segmento[1]])

        # Movimentando a cobra
        if len(cobra) > 0:
            # Criando uma cópia da cabeça da cobra
            nova_cabeca = [cobra[0][0], cobra[0][1]]

            # Movendo a cabeça da cobra na direção apropriada
            if cobra_dir == 'LEFT':
                nova_cabeca[0] -= velocidade
            elif cobra_dir == 'RIGHT':
                nova_cabeca[0] += velocidade
            elif cobra_dir == 'UP':
                nova_cabeca[1] -= velocidade
            elif cobra_dir == 'DOWN':
                nova_cabeca[1] += velocidade

            # Adicionando a nova cabeça no início da cobra
            cobra.insert(0, nova_cabeca)

            # Removendo o último segmento da cobra
            cobra.pop()

        # Verificando colisões com as bordas da tela
        if len(cobra) > 0 and (cobra[0][0] < 0 or cobra[0][0] >= largura or cobra[0][1] < 0 or cobra[0][1] >= altura):
            game_over = True

        # Verificando colisões com o próprio corpo
        for segmento in cobra[1:]:
            if len(cobra) > 0 and cobra[0] == segmento:
                game_over = True

        # Desenhando na tela
        tela.fill(branco)
        pygame.draw.rect(tela, vermelho, [comida[0], comida[1], tamanho_celula, tamanho_celula])
        desenhar_cobra(tamanho_celula, cobra)

        # Exibindo a pontuação na tela
        fonte_pontuacao = pygame.font.SysFont(None, 30)
        texto_pontuacao = fonte_pontuacao.render('Pontuação: {}'.format(pontuacao), True, preto)
        tela.blit(texto_pontuacao, (10, altura - 30))

        pygame.display.update()

        # Definindo a taxa de atualização
        relogio.tick(10)

    pygame.quit()

# Iniciando o jogo
jogo()
