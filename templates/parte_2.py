import pygame

# Inicializando o Pygame
pygame.init()

# Definindo a taxa de quadros (FPS)
FPS = 60

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PYLADY_WIDTH = 50
PYLADY_HEIGHT = 50
PYLADY_IMG = "img/pylady.png"
PYLADY_SPEED = 5

# Carregando a imagem da PyLady
pylady_image = pygame.image.load(PYLADY_IMG)

PROJECTILE_WIDTH = 3
PROJECTILE_HEIGHT = 5
PROJECTILE_PYLADY_IMG = "img/projectile_pylady.png"
PROJECTILE_PYLADY_SPEED = 10

# Carregando a imagem do projétil
projectile_pylady_image = pygame.image.load(PROJECTILE_PYLADY_IMG)

# Definindo o título da janela
pygame.display.set_caption("PyLadies Invaders")

# Definindo a cor de fundo
BACKGROUND_COLOR = (0, 0, 0)  # Preto


def draw_pylady(screen, pylady_x, pylady_y):
    screen.blit(pylady_image, (pylady_x, pylady_y))


def move_pylady(pylady_x, x):
    if x < 0:
        pylady_x = 0  # Não permite que a PyLady saia da tela pela esquerda
    elif x >= SCREEN_WIDTH - PYLADY_WIDTH:
        pylady_x = SCREEN_WIDTH - PYLADY_WIDTH  # Não permite que a PyLady saia da tela pela direita
    else:
        pylady_x = x  # Atualiza a posição da PyLady

    return pylady_x


def draw_projectile(screen, projectile_x, projectile_y, projectile_active):
    if projectile_active:
        screen.blit(projectile_pylady_image, (projectile_x, projectile_y))


def move_projectile(projectile_y, projectile_active):
    if projectile_active:
        projectile_y -= PROJECTILE_PYLADY_SPEED  # Move o projétil para cima
        if projectile_y < 0:
            projectile_active = False  # Desativa o projétil quando sair da tela
    return projectile_y, projectile_active


def handle_events(pylady_x, pylady_y, projectile_x, projectile_y, projectile_active):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Verificando eventos do teclado
    pressed_keys = pygame.key.get_pressed()

    # Movendo a PyLady
    if pressed_keys[pygame.K_LEFT]:
        pylady_x = move_pylady(pylady_x, pylady_x - PYLADY_SPEED)
    if pressed_keys[pygame.K_RIGHT]:
        pylady_x = move_pylady(pylady_x, pylady_x + PYLADY_SPEED)

    # Criando o projétil
    if pressed_keys[pygame.K_SPACE] and not projectile_active:
        projectile_active = True
        projectile_x = pylady_x + (PYLADY_WIDTH // 2)
        projectile_y = pylady_y - PROJECTILE_HEIGHT

    return pylady_x, pylady_y, projectile_x, projectile_y, projectile_active


def draw_elements(screen, pylady_x, pylady_y, projectile_x, projectile_y, projectile_active):
    screen.fill(BACKGROUND_COLOR)  # Preenche a tela com a cor de fundo
    draw_pylady(screen, pylady_x, pylady_y)  # Desenha a PyLady
    draw_projectile(screen, projectile_x, projectile_y, projectile_active)  # Desenha o projétil
    pygame.display.flip()  # Atualiza a tela


def run():
    # Definindo o clock do jogo
    clock = pygame.time.Clock()

    # Criando a janela do jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Definindo a posição inicial da PyLady
    pylady_x = (SCREEN_WIDTH - PYLADY_WIDTH) // 2  # Centraliza horizontalmente
    pylady_y = SCREEN_HEIGHT - PYLADY_HEIGHT  # Posiciona na parte inferior

    # Definindo a posição inicial do projétil
    projectile_x = pylady_x + (PYLADY_WIDTH // 2)  # Posiciona o projétil na mesma posição horizontal da PyLady
    projectile_y = pylady_y - PROJECTILE_HEIGHT  # Posiciona o projétil logo acima da PyLady

    # Variável para controlar se o projétil está ativo
    projectile_active = False

    while True:
        pylady_x, pylady_y, projectile_x, projectile_y, projectile_active = handle_events(
            pylady_x,
            pylady_y,
            projectile_x,
            projectile_y,
            projectile_active
        )  # Lê os eventos do teclado
        projectile_y, projectile_active = move_projectile(projectile_y, projectile_active)  # Atualiza a posição do projétil, caso ele esteja ativo
        draw_elements(screen, pylady_x, pylady_y, projectile_x, projectile_y, projectile_active)  # Desenha os elementos do jogo
        clock.tick(FPS)  # Controla a taxa de quadros do jogo


if __name__ == "__main__":
    run()  # Inicia o jogo
    pygame.quit()  # Encerra o Pygame ao sair do jogo
