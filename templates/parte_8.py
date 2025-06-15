import enum
import random
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
INVADERS_SHOOT = pygame.USEREVENT + 3

LIFE_WIDTH = 30
LIFE_HEIGHT = 22
LIFE_IMG = "img/life.png"
LIFE_QTD = 3

HIT_INVADER_SOUND = "sounds/hit_invader.ogg"
HIT_PYLADY_SOUND = "sounds/hit_pylady.ogg"
EXPLOSION_SOUND = "sounds/explosion.ogg"
VICTORY_SOUND = "sounds/victory.ogg"
GAME_RUN_SOUND = "sounds/game_run.ogg"


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


class PyLady(Object):
    def __init__(self, image=PYLADY_IMG):
        x = (SCREEN_WIDTH - PYLADY_WIDTH) // 2
        y = SCREEN_HEIGHT - PYLADY_HEIGHT

        super().__init__(image, PYLADY_WIDTH, PYLADY_HEIGHT, x, y)

    def move(self, x):
        if x < 0:
            self.x = 0  # Não permite que a PyLady saia da tela pela esquerda
        elif x >= SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width  # Não permite que a PyLady saia da tela pela direita
        else:
            self.x = x  # Atualiza a posição da PyLady


class ProjectilePyLady(Object):
    def __init__(self, x, image=PROJECTILE_PYLADY_IMG):
        y = SCREEN_HEIGHT - PYLADY_HEIGHT - PROJECTILE_HEIGHT
        self.active = True
        super().__init__(image, PROJECTILE_WIDTH, PROJECTILE_HEIGHT, x, y)

    def move(self):
        if self.active:
            self.y -= PROJECTILE_PYLADY_SPEED
            if self.y < 0:
                self.active = False


class ProjectileInvader(Object):
    def __init__(self, x, y, image=PROJECTILE_INVADER_IMG):
        self.active = True
        super().__init__(image, PROJECTILE_WIDTH, PROJECTILE_HEIGHT, x, y)

    def move(self):
        if self.active:
            self.y += PROJECTILE_INVADER_SPEED
            if self.y > SCREEN_HEIGHT:
                self.active = False


class Life(Object):
    def __init__(self, x, y, image=LIFE_IMG):
        super().__init__(image, LIFE_WIDTH, LIFE_HEIGHT, x, y)

class Sound:
    def __init__(self, sound_path, channel_number, volume=0.3):
        self.sound = pygame.mixer.Sound(sound_path)
        self.channel = pygame.mixer.Channel(channel_number)
        self.channel.set_volume(volume)

    def play(self, loops=0):
        self.channel.play(self.sound, loops=loops)

    def stop(self):
        self.channel.stop()


class Game:
    def __init__(self):
        # Inicializando o Pygame
        pygame.init()

        # Definindo o clock do jogo
        self.clock = pygame.time.Clock()

        pygame.time.set_timer(MOVE_INVADERS_X, INVADER_TIME_X)  # Movimenta os invasores horizontalmente a cada meio segundo
        pygame.time.set_timer(MOVE_INVADERS_Y, INVADER_TIME_Y)  # Movimenta os invasores verticalmente a cada 2 segundos
        pygame.time.set_timer(INVADERS_SHOOT, INVADER_TIME_SHOOT)  # Dispara o projétil dos invasores a cada 2 segundos

        self.sound_hit_invader = Sound(HIT_INVADER_SOUND, 0)
        self.sound_hit_pylady = Sound(HIT_PYLADY_SOUND, 1)
        self.sound_victory = Sound(VICTORY_SOUND, 3)
        self.sound_explosion = Sound(EXPLOSION_SOUND, 2)
        self.sound_game_run = Sound(GAME_RUN_SOUND, 6, 0.1)
    
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

        self.projectiles_invaders = []  # Lista para armazenar os projéteis disparados pelos invasores

        # Posição inicial das vidas
        base_x = SCREEN_WIDTH - LIFE_WIDTH * LIFE_QTD - 30  # Adiciona uma margem de 30 pixels à direita

        self.lives = []
        for i in range(LIFE_QTD):
            self.lives.append(Life(base_x + i * LIFE_WIDTH, 10)) # Adiciona as vidas na parte superior direita da tela

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == MOVE_INVADERS_X:
                self.move_invaders_x()

            if event.type == MOVE_INVADERS_Y:
                self.move_invaders_y()

            if event.type == INVADERS_SHOOT:
                self.invader_shoot()  # Dispara o projétil dos invasores

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
 
    def invader_shoot(self):
        invader_to_shoot = random.choice(self.invaders)  # Seleciona um invasor aleatório da lista de invasores
        self.projectiles_invaders.append(
            ProjectileInvader(
                invader_to_shoot.x + INVADER_WIDTH // 2,
                invader_to_shoot.y + INVADER_HEIGHT,
            )
        )

    def check_collision(self):
        # Verifica se um invasor colidiu com a PyLady
        for invader in self.invaders:
            if invader.collision(self.pylady):
                self.invaders.remove(invader)
                if self.lives:  # Verifica se ainda há vidas restantes
                    self.lives.pop()  # Remove uma vida

            # Verifica se o projétil da PyLady colidiu com algum invasor
            if self.projectile_pylady and invader.collision(self.projectile_pylady):
                self.invaders.remove(invader)
                self.projectile_pylady.active = False
                self.projectile_pylady = None
                self.sound_hit_invader.play()  # Reproduz o som de colisão do invasor

 
        # Verifica se um projétil dos invasores colidiu com a PyLady
        for projectile_invader in self.projectiles_invaders:
            if projectile_invader.collision(self.pylady):
                self.projectiles_invaders.remove(projectile_invader)  # Remove o projétil dos invasores
                self.sound_hit_pylady.play()  # Reproduz o som de colisão da PyLady
                if self.lives:  # Verifica se ainda há vidas restantes
                    self.lives.pop()  # Remove uma vida
 
    def update(self):
        if self.projectile_pylady:
            self.projectile_pylady.move()  # Atualiza a posição do projétil, se ele estiver ativo
            if not self.projectile_pylady.active:
                self.projectile_pylady = None  # Reseta o projétil se ele não estiver ativo

        for projectile in self.projectiles_invaders:
            projectile.move()  # Move o projétil dos invasores
            if not projectile.active:
                self.projectiles_invaders.remove(projectile)  # Remove o projétil se não estiver ativo

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)  # Preenche a tela com a cor de fundo

        self.pylady.show(self.screen)  # Desenha a PyLady

        for life in self.lives:  # Desenha todas as vidas
            life.show(self.screen)

        if self.projectile_pylady:
            self.projectile_pylady.show(self.screen)  # Desenha o projétil, se ele estiver ativo

        for invader in self.invaders:  # Desenha todos os invasores
            invader.show(self.screen)

        for projectile_invader in self.projectiles_invaders:  # Desenha todos os projéteis dos invasores
            projectile_invader.show(self.screen)

        pygame.display.flip()  # Atualiza a tela

    def run(self):
        self.sound_game_run.play(-1)  # Reproduz o som de fundo do jogo em loop

        while True:
            self.handle_events()  # Lê os eventos do teclado
            self.handle_input()  # Lida com a entrada do usuário
            self.update()  # Atualiza o estado do jogo
            self.check_collision()  # Verifica colisões entre o projétil e os invasores
            self.draw()  # Desenha os elementos do jogo
            self.clock.tick(FPS)  # Controla a taxa de quadros do jogo

            if not self.invaders:  # Verifica se não há mais invasores
                self.sound_victory.play()  # Reproduz o som de vitória
                pygame.time.delay(2000)  # Aguarda 2 segundos antes de encerrar o jogo
                exit()  # Encerra o jogo

            if not self.lives:  # Verifica se não há mais vidas
                self.sound_explosion.play()  # Reproduz o som de fim de jogo
                pygame.time.delay(2000)  # Aguarda 2 segundos antes de encerrar o jogo
                exit()  # Encerra o jogo

if __name__ == "__main__":
    game = Game()  # Cria uma instância do jogo
    game.run()  # Inicia o jogo
    pygame.quit()  # Encerra o Pygame ao sair do jogo