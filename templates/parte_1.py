import pygame

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definindo a taxa de quadros (FPS)
FPS = 60

# Definindo o clock do jogo
clock = pygame.time.Clock()

# Criando a janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Definindo o título da janela
pygame.display.set_caption("PyLadies Invaders")

# Definindo a cor de fundo
BACKGROUND_COLOR = (0, 0, 0)  # Preto

# Preenchendo a tela com a cor de fundo
screen.fill(BACKGROUND_COLOR)

# Atualizando a tela
pygame.display.flip()

PYLADY_WIDTH = 50
PYLADY_HEIGHT = 50
PYLADY_IMG = "img/pylady.png"
PYLADY_SPEED = 5  # Velocidade de movimentação da PyLady

# Carregando a imagem da PyLady
pylady_image = pygame.image.load(PYLADY_IMG)

# Definindo a posição inicial da PyLady
pylady_x = (SCREEN_WIDTH - PYLADY_WIDTH) // 2  # Centraliza horizontalmente
pylady_y = SCREEN_HEIGHT - PYLADY_HEIGHT  # Posiciona na parte inferior

PROJECTILE_WIDTH = 3
PROJECTILE_HEIGHT = 5
PROJECTILE_PYLADY_IMG = "img/projectile_pylady.png"
PROJECTILE_PYLADY_SPEED = 10

# Carregando a imagem do projétil
projectile_pylady_image = pygame.image.load(PROJECTILE_PYLADY_IMG)

# Definindo a posição inicial do projétil
projectile_x = pylady_x + (PYLADY_WIDTH // 2)  # Posiciona o projétil na mesma posição horizontal da PyLady
projectile_y = SCREEN_HEIGHT - PYLADY_HEIGHT - PROJECTILE_HEIGHT  # Posiciona o projétil logo acima da PyLady
projectile_active = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificando eventos do teclado
    pressed_keys = pygame.key.get_pressed()

    # Movendo a PyLady para a esquerda
    if pressed_keys[pygame.K_LEFT]:
        pylady_x -= PYLADY_SPEED  # Move 5 pixels para a esquerda

    # Movendo a PyLady para a direita
    if pressed_keys[pygame.K_RIGHT]:
        pylady_x += PYLADY_SPEED  # Move 5 pixels para a direita
    # Verificando se a tecla "espaço" foi pressionada

    if pressed_keys[pygame.K_SPACE] and not projectile_active:
        projectile_active = True  # Ativa o projétil
        projectile_x = pylady_x + (PYLADY_WIDTH // 2)  # Centraliza o projétil na PyLady
        projectile_y = pylady_y - PROJECTILE_HEIGHT  # Posiciona o projétil logo acima da PyLady

    if projectile_active:
        projectile_y -= PROJECTILE_PYLADY_SPEED  # Move o projétil para cima

        # Verifica se o projétil saiu da tela
        if projectile_y < 0:
            projectile_active = False  # Desativa o projétil quando sair da tela

    # Preenchendo a tela com a cor de fundo
    screen.fill(BACKGROUND_COLOR)

    # Desenhando a PyLady na tela
    screen.blit(pylady_image, (pylady_x, pylady_y))

    # Desenhando o projétil na tela
    if projectile_active:
        screen.blit(projectile_pylady_image, (projectile_x, projectile_y))

    # Atualizando a tela
    pygame.display.flip()

    # Atualizando o clock do jogo
    clock.tick(FPS)  # Controla a taxa de quadros do jogo
