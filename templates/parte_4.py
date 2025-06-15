import enum
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

INVADER_WIDTH = 25
INVADER_HEIGHT = 18
INVADER_IMG = "img/invader.png"
PROJECTILE_INVADER_IMG = "img/projectile_invader.png"
PROJECTILE_INVADER_SPEED = 5

INVADER_X_SPEED = 10
INVADER_Y_SPEED = 5

INVADER_TIME_X = 500
INVADER_TIME_Y = 2000
INVADER_TIME_SHOOT = 1000

MOVE_INVADERS_X = pygame.USEREVENT + 1
MOVE_INVADERS_Y = pygame.USEREVENT + 2

# Definindo a cor de fundo
BACKGROUND_COLOR = (0, 0, 0)  # Preto


class Direction(enum.Enum):
    LEFT = "left"
    RIGHT = "right"


class Object:
    def __init__(self, img, width, height, x=0, y=0):
        self.x = x  # Posição horizontal do objeto
        self.y = y  # Posição vertical do objeto
        self.width = width  # Largura do objeto
        self.height = height  # Altura do objeto
        self.image = pygame.image.load(img)  # Carrega a imagem do objeto

    def move(self, x, y):
        self.x = x
        self.y = y

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Desenha o objeto na tela

    def collision(self, other):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
            pygame.Rect(other.x, other.y, other.width, other.height)
        )


class Invader(Object):
    def __init__(self, x, y, img=INVADER_IMG):
        super().__init__(img, INVADER_WIDTH, INVADER_HEIGHT, x, y)  # Chama o construtor da classe base

    def move_y(self):
        self.move(self.x, self.y + INVADER_Y_SPEED)

        if self.y >= SCREEN_HEIGHT + INVADER_HEIGHT:
            self.active = False

    def move_x(self, direction):
        if direction == Direction.LEFT:
            self.move(self.x - INVADER_X_SPEED, self.y)
        elif direction == Direction.RIGHT:
            self.move(self.x + INVADER_X_SPEED, self.y)  


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

        pygame.time.set_timer(MOVE_INVADERS_X, INVADER_TIME_X)  # Movimenta os invasores horizontalmente a cada meio segundo
        pygame.time.set_timer(MOVE_INVADERS_Y, INVADER_TIME_Y)  # Movimenta os invasores verticalmente a cada 2 segundos

        # Criando a janela do jogo
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Definindo o título da janela        
        pygame.display.set_caption("PyLadies Invaders")

        self.pylady = PyLady()  # Cria uma instância da PyLady
        self.projectile_pylady = None  # Será inicializado quando o projétil for disparado

        self.direction = Direction.LEFT  # Direção inicial dos invasores

        self.invaders = []  # Lista para armazenar os invasores
        for y in range(5):  # Gera 5 linhas de invasores
            # Adiciona uma margem de 150 pixels na tela e calcula o número de colunas de 50 pixels que cabem na tela
            for x in range((SCREEN_WIDTH - 150) // 50):
                # Cria um novo invasor considerando 100 pixels de margem horizontal e 50 pixels de espaçamento vertical
                invader = Invader(x * INVADER_WIDTH * 2 + 100, y * 50 + 50)
                self.invaders.append(invader)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == MOVE_INVADERS_X:
                self.move_invaders_x()

            if event.type == MOVE_INVADERS_Y:
                self.move_invaders_y()

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

    def move_invaders_y(self):
        for invader in self.invaders:
            invader.move_y()  # Move o invasor verticalmente

    def move_invaders_x(self):
        for invader in self.invaders:
            invader.move_x(self.direction)

        if self.invaders:
            if self.invaders[-1].x >= SCREEN_WIDTH - INVADER_WIDTH:
                self.direction = Direction.LEFT
            elif self.invaders[0].x <= 0:
                self.direction = Direction.RIGHT

    def check_collision(self):
        # Verifica se um invasor colidiu com a PyLady
        for invader in self.invaders:
            if invader.collision(self.pylady):
                self.invaders.remove(invader)
                exit()  # Encerra o jogo se um invasor colidir com a PyLady

        # Verifica se o projétil da PyLady colidiu com algum invasor
            if self.projectile_pylady and invader.collision(self.projectile_pylady):
                self.invaders.remove(invader)
                self.projectile_pylady.active = False
                self.projectile_pylady = None

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

        for invader in self.invaders:  # Desenha todos os invasores
            invader.show(self.screen)

        pygame.display.flip()  # Atualiza a tela

    def run(self):
        while True:
            self.handle_events()  # Lê os eventos do teclado
            self.handle_input()  # Lida com a entrada do usuário
            self.update()  # Atualiza o estado do jogo
            self.check_collision()  # Verifica colisões entre o projétil e os invasores
            self.draw()  # Desenha os elementos do jogo
            self.clock.tick(FPS)  # Controla a taxa de quadros do jogo


if __name__ == "__main__":
    game = Game()  # Cria uma instância do jogo
    game.run()  # Inicia o jogo
    pygame.quit()  # Encerra o Pygame ao sair do jogo