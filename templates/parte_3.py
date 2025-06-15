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

PROJECTILE_WIDTH = 3
PROJECTILE_HEIGHT = 5
PROJECTILE_PYLADY_IMG = "img/projectile_pylady.png"
PROJECTILE_PYLADY_SPEED = 10

# Definindo o título da janela
pygame.display.set_caption("PyLadies Invaders")

# Definindo a cor de fundo
BACKGROUND_COLOR = (0, 0, 0)  # Preto


class PyLady:
    def __init__(self, width=PYLADY_WIDTH, height=PYLADY_HEIGHT, img=PYLADY_IMG):
        self.x = (SCREEN_WIDTH - PYLADY_WIDTH) // 2  # Posição horizontal da PyLady
        self.y = SCREEN_HEIGHT - PYLADY_HEIGHT  # Posição vertical da PyLady
        self.width = width  # Largura da PyLady
        self.height = height  # Altura da PyLady
        self.image = pygame.image.load(img)  # Carrega a imagem da PyLady

    def move(self, x):
        if x < 0:
            self.x = 0  # Não permite que a PyLady saia da tela pela esquerda
        elif x >= SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width  # Não permite que a PyLady saia da tela pela direita
        else:
            self.x = x  # Atualiza a posição da PyLady

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Desenha a PyLady na tela


class ProjectilePyLady:
    def __init__(self, x=0, width=PROJECTILE_WIDTH, height=PROJECTILE_HEIGHT, img=PROJECTILE_PYLADY_IMG):
        self.x = x  # Posição horizontal do projétil
        self.y = SCREEN_HEIGHT - PYLADY_HEIGHT - PROJECTILE_HEIGHT  # Posição vertical do projétil
        self.width = width  # Largura do projétil
        self.height = height  # Altura do projétil
        self.image = pygame.image.load(img)  # Carrega a imagem do projétil
        self.active = True  # Estado do projétil (ativo ou não)

    def move(self):
        if self.active:
            self.y -= PROJECTILE_PYLADY_SPEED  # Move o projétil para cima
            if self.y < 0:
                self.active = False  # Desativa o projétil quando sair da tela

    def show(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))  # Desenha o projétil na tela


class Game:
    def __init__(self):
        # Inicializando o Pygame
        pygame.init()

        # Definindo o clock do jogo
        self.clock = pygame.time.Clock()

        # Criando a janela do jogo
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PyLadies Invaders")

        self.pylady = PyLady()  # Cria uma instância da PyLady
        self.projectile_pylady = None  # Será inicializado quando o projétil for disparado

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def handle_input(self):
        # Lendo os eventos do teclado
        pressed_keys = pygame.key.get_pressed()

        # Movendo a PyLady
        if pressed_keys[pygame.K_LEFT]:
            self.pylady.move(self.pylady.x - PYLADY_SPEED)
        if pressed_keys[pygame.K_RIGHT]:
            self.pylady.move(self.pylady.x + PYLADY_SPEED)

        # Criando o projétil
        if pressed_keys[pygame.K_SPACE] and not self.projectile_pylady:
            self.projectile_pylady = ProjectilePyLady(self.pylady.x + PYLADY_WIDTH // 2)  # Cria uma nova instância do projétil

    def update(self):
        if self.projectile_pylady:
            self.projectile_pylady.move()  # Atualiza a posição do projétil, se ele estiver ativo
            if not self.projectile_pylady.active:
                self.projectile_pylady = None  # Reseta o projétil se ele não estiver ativo

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)  # Preenche a tela com a cor de fundo

        self.pylady.show(self.screen)  # Desenha a PyLady

        if self.projectile_pylady:
            self.projectile_pylady.show(self.screen)  # Desenha o projétil, se ele estiver ativo

        pygame.display.flip()  # Atualiza a tela

    def run(self):
        while True:
            self.handle_events()  # Lê os eventos do teclado
            self.handle_input()  # Lida com a entrada do usuário
            self.update()  # Atualiza o estado do jogo
            self.draw()  # Desenha os elementos do jogo
            self.clock.tick(FPS)  # Controla a taxa de quadros do jogo


if __name__ == "__main__":
    game = Game()  # Cria uma instância do jogo
    game.run()  # Inicia o jogo
    pygame.quit()  # Encerra o Pygame ao sair do jogo