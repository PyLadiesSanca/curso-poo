# PyLadies Invaders: Introdução ao Pygame usando POO

Nesse tutorial iremos construir o jogo PyLadies Invaders, onde nossa PyLady luta heroicamente contra os invasores alienígenas!

Vamos utilizar a biblioteca Pygame, e exercitar alguns conceitos de Programação Orientada à Objetos (POO).


## O que é o Pygame?
Pygame é uma biblioteca popular para desenvolvimento de jogos em Python. Ela fornece funcionalidades para criar janelas, desenhar gráficos, tocar sons e gerenciar eventos de entrada do usuário.

## Criando o ambiente de desenvolvimento
Para começar, você precisa ter o Python instalado em seu computador. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

Depois de instalar o Python, você pode verificar se ele está instalado corretamente executando o seguinte comando no terminal:

```bash
python --version
```
Se você estiver usando o Windows, pode ser necessário usar `python3` em vez de `python`.

Após isso, crie um diretório para o seu projeto e navegue até ele no terminal. Por exemplo:

```bash
mkdir pyladies-invaders
cd pyladies-invaders
```

Para criar projetos em Python, é muito importante ter um ambiente virtual configurado. Assim, bibliotecas utilizadas em um projeto não irão interferir em projetos futuros.

Você pode criar um ambiente virtual com o seguinte comando:

```bash
python -m venv venv
```

Para ativar o ambiente virtual, use:
- No Windows:
```bash
venv\Scripts\activate
```

- No macOS/Linux:
```bash
source venv/bin/activate
```

Depois de ativar o ambiente virtual, você pode instalar o Pygame usando o pip:

```bash
pip install pygame
```

Crie um arquivo chamado `main.py` no diretório do projeto. Esse será o ponto de entrada do nosso jogo.

Para executar o código, você pode usar o seguinte comando no terminal:

```bash
python main.py
```

Se você estiver usando o Windows, pode ser necessário usar `python3` em vez de `python`.

Caso precise parar o código em execução, você pode usar `Ctrl + C` no terminal.

------

# Parte 1: Criando o jogo de forma simples
Iremos começar criando o jogo de uma forma simples, para termos uma introdução ao funcionamento do Pygame e como ele lida com eventos e gráficos.


## Criando uma janela de jogo
Vamos criar uma janela de jogo simples para começar. A seguir, você verá como configurar o Pygame e criar uma janela onde o jogo será exibido.

Iremos exibí-la por 5 segundos antes de fechá-la. Para isso, vamos utilizar o método `pygame.time.delay()`.

```python
import pygame

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

# Aguardando 5 segundos
pygame.time.delay(5000)

# Fechando o Pygame
pygame.quit()
```

## Loop principal do jogo
Para manter a janela aberta e responder a eventos, precisamos de um loop principal do jogo. Esse loop irá verificar eventos, atualizar o estado do jogo e desenhar os elementos na tela.

No Pygame temos diversos eventos que podemos capturar, como o fechamento da janela e teclas pressionadas. Vamos criar um loop que irá manter a janela aberta e responder ao evento de fechar a janela.

Para isso, remova as últimas duas linhas do código anterior (`pygame.time.delay(5000)` e `pygame.quit()`) e adicione o seguinte código:

```python
# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

### Lendo um evento do teclado
Para tornar o jogo interativo, precisamos ler eventos do teclado. Isso nos permitirá mover a PyLady e disparar projéteis.

No Pygame, podemos capturar quando uma tecla é pressionada ou liberada. Vamos adicionar um evento para verificar se a tecla "espaço" foi pressionada e trocar a cor de fundo da tela quando isso acontecer.

Adicione o seguinte código ao seu script, dentro do loop do jogo:

```python
    # Verificando eventos do teclado
    pressed_keys = pygame.key.get_pressed()

    # Verificando se a tecla "espaço" foi pressionada
    if pressed_keys[pygame.K_SPACE]:
        # Trocar a cor de fundo
        BACKGROUND_COLOR = (255, 255, 255)  # Branco

        # Preenchendo a tela com a cor de fundo
        screen.fill(BACKGROUND_COLOR)

    # Atualizando a tela
    pygame.display.flip()
```

### Desenhando a PyLady
Agora que temos uma janela de jogo e eventos do teclado, vamos adicionar a PyLady. Iremos chamá-la de `pylady`.

Para desenhar a PyLady, precisamos de uma imagem que a represente. Crie uma pasta `img` dentro do seu projeto. Você pode baixar a imagem da PyLady [aqui](img/pylady.png) e salvá-la na pasta `img` com o nome `pylady.png`.

O tamanho da imagem é 50x50 pixels, então vamos posicioná-la na parte inferior da tela, centralizada horizontalmente.

Para isso, iremos utilizar o tamanho da tela e a largura da imagem para calcular a posição inicial da PyLady.

No Pygame, o sistema de coordenadas começa no canto superior esquerdo da tela, onde o eixo x aumenta para a direita e o eixo y aumenta para baixo.

Portanto, para centralizar a PyLady horizontalmente, precisamos dividir a largura total da tela por 2. Para posicioná-la na parte inferior, vamos subtrair a altura da imagem da altura total da tela.

Adicione as inicializações da PyLady ao seu script, na parte onde você já configurou o Pygame e a janela do jogo:

```python
PYLADY_WIDTH = 50
PYLADY_HEIGHT = 50
PYLADY_IMG = "img/pylady.png"

# Carregando a imagem da PyLady
pylady_image = pygame.image.load(PYLADY_IMG)

# Definindo a posição inicial da PyLady
pylady_x = (SCREEN_WIDTH - PYLADY_WIDTH) // 2  # Centraliza horizontalmente
pylady_y = SCREEN_HEIGHT - PYLADY_HEIGHT  # Posiciona na parte inferior
```

Após definir a PyLady, vamos desenhá-la na tela. Para isso, utilizaremos o método `blit` do Pygame, que desenha uma superfície (neste caso, a imagem da PyLady) em outra superfície (a tela do jogo).

Adicione o seguinte código dentro do loop principal do jogo, logo após a leitura dos eventos e antes de atualizar a tela:

```python
    # Desenhando a PyLady na tela
    screen.blit(pylady_image, (pylady_x, pylady_y))
```

### Movendo a PyLady
Para tornar o jogo interativo, precisamos permitir que o jogador mova a PyLady para a esquerda e para a direita usando as teclas de seta.

Para isso, vamos adicionar eventos de teclado que irão atualizar a posição da PyLady com base nas teclas pressionadas.

Vamos definir uma velocidade para a movimentação da PyLady. Adicione a seguinte linha logo após a definição da PyLady:

```python
PYLADY_SPEED = 5  # Velocidade de movimentação da PyLady
```

Vamos adicionar o seguinte código dentro do loop principal do jogo, entre a leitura dos eventos e o desenho da PyLady, para permitir a movimentação da PyLady:

```python
    # Movendo a PyLady para a esquerda
    if pressed_keys[pygame.K_LEFT]:
        pylady_x -= PYLADY_SPEED  # Move 5 pixels para a esquerda

    # Movendo a PyLady para a direita
    if pressed_keys[pygame.K_RIGHT]:
        pylady_x += PYLADY_SPEED  # Move 5 pixels para a direita
```

Para corrigir a PyLady aparecendo diversas vezes conforme vamos movimentando, precisamos adicionar uma linha para limpar a tela antes de desenhar a PyLady novamente. Isso pode ser feito logo antes de desenhar a PyLady, preenchendo a tela com a cor de fundo:

```python
    # Preenchendo a tela com a cor de fundo
    screen.fill(BACKGROUND_COLOR)
```

### Atirando com a PyLady
Para adicionar a mecânica de tiro, vamos permitir que o jogador dispare projéteis pressionando a tecla "espaço". Vamos desenhar um projétil que se move para cima a partir da posição da PyLady.

Iremos definir a velocidade do projétil e sua imagem. Você pode baixar a imagem
[aqui](img/projectile_pylady.png) e salvá-la na pasta `img` com o nome `projectile_pylady.png`.

Vamos adicionar o seguinte código para definir a imagem do projétil e sua posição inicial, logo após a definição da PyLady:

```python
PROJECTILE_WIDTH = 3
PROJECTILE_HEIGHT = 5
PROJECTILE_PYLADY_IMG = "img/projectile_pylady.png"
PROJECTILE_PYLADY_SPEED = 10

# Carregando a imagem do projétil
projectile_pylady_image = pygame.image.load(PROJECTILE_PYLADY_IMG)

# Definindo a posição inicial do projétil
projectile_x = pylady_x + (PYLADY_WIDTH // 2)  # Posiciona o projétil na mesma posição horizontal da PyLady
projectile_y = SCREEN_HEIGHT - PYLADY_HEIGHT - PROJECTILE_HEIGHT  # Posiciona o projétil logo acima da PyLady
```

#### Exibindo e movendo o projétil na tela
Para que o projétil seja exibido na tela e se mova corretamente, precisamos:

1. Detectar quando a tecla "espaço" for pressionada para disparar.

2. Atualizar a posição do projétil a cada quadro.

3. Gerenciar o estado do projétil (se está ativo ou pronto para ser disparado).

* 1. Detectando o disparo do projétil
Para detectar quando a tecla "espaço" é pressionada, vamos adicionar uma variável que controla se o projétil está ativo ou não. Quando a tecla for pressionada, o projétil será disparado e começará a se mover para cima.

```python
# Variável para controlar se o projétil está ativo
projectile_active = False
```

Agora, vamos modificar o código que lê os eventos do teclado para verificar se a tecla "espaço" foi pressionada e ativar o projétil:

```python
    # Verificando se a tecla "espaço" foi pressionada
    if pressed_keys[pygame.K_SPACE] and not projectile_active:
        projectile_active = True  # Ativa o projétil
        projectile_x = pylady_x + (PYLADY_WIDTH // 2)  # Centraliza o projétil na PyLady
        projectile_y = pylady_y - PROJECTILE_HEIGHT  # Posiciona o projétil logo acima da PyLady
```

No entanto, diferente da PyLady, o projétil deve se mover para cima continuamente.

* 2. Atualizando a posição do projétil
Os elementos do jogo, incluindo o projétil, precisam ser atualizados a cada quadro. Para isso, o Pygame possui o mecanismo de clock, onde é passado uma taxa de atualização de quadros (FPS) para controlar a velocidade do jogo.

Defina o FPS no começo do seu script:

```python
# Definindo a taxa de quadros (FPS)
FPS = 60
```

Vamos adicionar o seguinte código logo após a inicialização do Pygame, para definir o clock do jogo:

```python
# Definindo o clock do jogo
clock = pygame.time.Clock()
```

Dentro do loop principal do jogo, vamos atualizar a taxa de quadros e controlar a velocidade do projétil.
```python
    # Atualizando o clock do jogo
    clock.tick(FPS)  # Controla a taxa de quadros do jogo
```

Podemos então atualizar a posição do projétil a cada quadro. Para isso, vamos utilizar a velocidade definida para o projétil e verificar se ele está ativo. Se estiver ativo, vamos mover sua posição vertical para cima.

Adicione o seguinte código logo após a verificação de eventos do teclado e antes de desenhar a PyLady:

```python
    # Atualizando a posição do projétil
    if projectile_active:
        projectile_y -= PROJECTILE_PYLADY_SPEED  # Move o projétil para cima

        # Verifica se o projétil saiu da tela
        if projectile_y < 0:
            projectile_active = False  # Desativa o projétil quando sair da tela
```

Desse modo, o projétil se moverá para cima quando disparado e será desativado quando sair da tela.

* 3. Desenhando o projétil na tela
Adicione o seguinte código logo após desenhar a PyLady:

```python
    # Desenhando o projétil na tela
    if projectile_active:
        screen.blit(projectile_pylady_image, (projectile_x, projectile_y))
```

Quando você pressionar a tecla "espaço", o projétil será disparado e se moverá para cima. Ao sair da tela, ele será reposicionado na posição inicial, pronto para ser disparado novamente.

## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_1.py](templates/parte_1.py):

------

# Parte 2: Refatorando o código com funções
Até agora, o nosso código está espalhado e repetitivo. Para melhorar a organização, podemos encapsular a lógica de cada elemento do jogo em funções. Isso nos permitirá visualizar melhor o fluxo do jogo e facilitar a manutenção.

Precisamos de funções para cada uma das responsabilidades do jogo, como desenhar a PyLady, mover a PyLady, desenhar o projétil, mover o projétil e lidar com os eventos do teclado.

Veremos abaixo como essa abordagem se torna complexa rapidamente, e como a Programação Orientada a Objetos (POO) pode nos ajudar a organizar melhor o código.

## Funções da PyLady
Para a PyLady, precisamos de funções para desenhar a PyLady na tela e para mover a PyLady de acordo com os eventos do teclado.

### Desenhando a PyLady
Podemos criar uma função `draw_pylady()` que será responsável por desenhar a PyLady na tela. Essa função receberá a tela e a posição da PyLady como parâmetros.

```python
def draw_pylady(screen, pylady_x, pylady_y):
    screen.blit(pylady_image, (pylady_x, pylady_y))
```

### Movendo a PyLady
Vamos criar uma função `move_pylady()` que será responsável por atualizar a posição da PyLady para o valor recebido como parâmetro.

Será necessário receber a posição atual e a posição alvo, fazer a verificação para não permitir que a PyLady saia da tela e retornar a nova posição.

```python
def move_pylady(pylady_x, x):
    if x < 0:
        pylady_x = 0  # Não permite que a PyLady saia da tela pela esquerda
    elif x >= SCREEN_WIDTH - PYLADY_WIDTH:
        pylady_x = SCREEN_WIDTH - PYLADY_WIDTH  # Não permite que a PyLady saia da tela pela direita
    else:
        pylady_x = x  # Atualiza a posição da PyLady

    return pylady_x
```

## Funções do projétil
Para o projétil, precisamos de funções para desenhar o projétil na tela e para mover o projétil de acordo com sua velocidade.

### Desenhando o projétil
Vamos criar uma função `draw_projectile()` que será responsável por desenhar o projétil na tela. Essa função receberá a tela, a posição do projétil e um booleano indicando se o projétil está ativo.

```python
def draw_projectile(screen, projectile_x, projectile_y, projectile_active):
    if projectile_active:
        screen.blit(projectile_image, (projectile_x, projectile_y))
```

### Movendo o projétil
Vamos criar uma função `move_projectile()` que será responsável por atualizar a posição do projétil de acordo com a velocidade do projétil. Se o projétil estiver ativo, ele será movido para cima e, caso saia da tela, será desativado.

Essa função receberá a posição do projétil e um booleano indicando se o projétil está ativo, e retornará a nova posição do projétil e o estado do projétil (ativo ou não).

```python
def move_projectile(projectile_y, projectile_active):
    if projectile_active:
        projectile_y -= PROJECTILE_PYLADY_SPEED  # Move o projétil para cima
        if projectile_y < 0:
            projectile_active = False  # Desativa o projétil quando sair da tela
    return projectile_y, projectile_active
```
## Funções do jogo
Para organizar o código do jogo, vamos criar funções que serão responsáveis por lidar com os eventos do teclado e desenhar os elementos do jogo na tela.

### Lendo os eventos do teclado
Vamos criar uma função `handle_events()` que será responsável por ler os eventos do teclado e atualizar a posição da PyLady e o estado do projétil.

Essa função precisará receber a posição atual da PyLady, a posição atual e o estado do projétil e retornar a nova posição da PyLady, a nova posição e o estado atualizado do projétil.

```python
def handle_events(pylady_x, pylady_y, projectile_x, projectile_y, projectile_active):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Verificando eventos do teclado
    pressed_keys = pygame.key.get_pressed()

    # Movendo a PyLady
    if pressed_keys[pygame.K_LEFT]:
        move_pylady(pylady_x, pylady_x - PYLADY_SPEED)
    if pressed_keys[pygame.K_RIGHT]:
        move_pylady(pylady_x, pylady_x + PYLADY_SPEED)

    # Criando o projétil
    if pressed_keys[pygame.K_SPACE] and not projectile_active:
        projectile_active = True
        projectile_x = pylady_x + (PYLADY_WIDTH // 2)
        projectile_y = pylady_y - PROJECTILE_HEIGHT
        
    return pylady_x, pylady_y, projectile_x, projectile_y, projectile_active
```

### Desenhando os elementos do jogo
Vamos criar uma função `draw_elements()` que será responsável por desenhar todos os elementos do jogo na tela.

Essa função irá chamar as funções `draw_pylady()` e `draw_projectile()` para desenhar a PyLady e o projétil, respectivamente, portanto ela receberá a tela, a posição da PyLady e a posição e estado do projétil como parâmetros.

```python
def draw_elements(screen, pylady_x, pylady_y, projectile_x, projectile_y, projectile_active):
    screen.fill(BACKGROUND_COLOR)  # Preenche a tela com a cor de fundo
    draw_pylady(screen, pylady_x, pylady_y)  # Desenha a PyLady
    draw_projectile(screen, projectile_x, projectile_y, projectile_active)  # Desenha o projétil
    pygame.display.flip()  # Atualiza a tela
```

### Loop principal do jogo
Vamos criar uma função `run()` que conterá o loop principal do jogo. Essa função irá gerenciar eventos, atualizar o estado do jogo e desenhar os elementos na tela.

Iremos mover as variáveis de inicialização do jogo (`clock` e `screen`) e o estado do jogo (posição da PyLady, posição do projétil e estado do projétil) para dentro da função `run()`, para que elas sejam gerenciadas dentro do loop principal.

```python
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
```

Por fim, vamos chamar a função `run()` no final do nosso script para iniciar o jogo:

```python
if __name__ == "__main__":
    run()  # Inicia o jogo
    pygame.quit()  # Encerra o Pygame ao sair do jogo
```
## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_2.py](templates/parte_2.py):

## Problemas com a abordagem de funções
Como podemos ver, a abordagem de funções nos permite organizar melhor o código, mas ainda assim ele pode se tornar complexo e difícil de manter à medida que o jogo cresce.

Cada objeto do jogo (como a PyLady e o projétil) tem seus próprios atributos e comportamentos, e encapsular essa lógica em funções pode levar a um código confuso e difícil de entender, dado que as funções podem ter muitos parâmetros e a lógica pode se espalhar por várias partes do código.

Considerando que o jogo pode ter muitos elementos, como inimigos, efeitos sonoros, vidas e outros, a abordagem de funções pode se tornar difícil de gerenciar e escalar.

Por isso, a Programação Orientada a Objetos (POO) é uma abordagem mais adequada para organizar o código de jogos, pois permite encapsular a lógica de cada elemento em classes, tornando o código mais modular e fácil de entender.

------

# Parte 3: Introdução à Programação Orientada a Objetos (POO)
A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em objetos, que são instâncias de classes. Cada objeto pode ter seus próprios atributos (dados) e métodos (funções).

No Pygame, podemos utilizar a POO para organizar melhor o código do jogo, encapsulando a lógica de cada elemento em classes. Isso nos permitirá criar instâncias desses elementos e gerenciar seu estado de forma mais eficiente.

## Criando classes para os elementos do jogo
Criaremos classes para a PyLady e o projétil. Cada classe terá seus próprios atributos e métodos para gerenciar o estado e o comportamento dos elementos do jogo.

### Classe PyLady
Vamos criar uma classe `PyLady` que representará a PyLady. Essa classe terá atributos para a posição, imagem e velocidade da PyLady, além de métodos para desenhar e mover a PyLady.

```python
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
```

### Classe ProjectilePyLady
Vamos criar uma classe `ProjectilePyLady` que representará o projétil disparado pela PyLady. Essa classe terá atributos para a posição, imagem e velocidade do projétil, além de métodos para desenhar e mover o projétil.

```python
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
```

### Classe Game
Agora, vamos criar uma classe `Game` que será responsável por gerenciar o estado do jogo, incluindo a PyLady e o projétil. Essa classe terá métodos para lidar com eventos, atualizar o estado do jogo e desenhar os elementos na tela.

```python
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
```

## Iniciando o jogo
Para iniciar o jogo, precisamos criar uma instância da classe `Game` e chamar o método `run()`.
```python
if __name__ == "__main__":
    game = Game()  # Cria uma instância do jogo
    game.run()  # Inicia o jogo
    pygame.quit()  # Encerra o Pygame ao sair do jogo
```
## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_3.py](templates/parte_3.py).

# Vantagens da POO
A Programação Orientada a Objetos (POO) nos permite organizar o código de forma mais modular e reutilizável. Algumas das vantagens incluem:

- **Encapsulamento**: Cada classe encapsula seus próprios dados e comportamentos, tornando o código mais fácil de entender e manter.
- **Reutilização**: Podemos criar instâncias de classes e reutilizar seu código em diferentes partes do jogo, evitando duplicação de código.
- **Abstração**: Podemos abstrair a lógica de cada elemento do jogo em classes, tornando o código mais legível e fácil de entender.
- **Escalabilidade**: À medida que o jogo cresce, podemos adicionar novas classes e funcionalidades sem complicar o código existente.
- **Organização**: O código fica mais organizado, com cada classe responsável por uma parte específica do jogo, facilitando a navegação e compreensão do código.

------

# Parte 4: Adicionando inimigos e colisões
Agora que temos a PyLady e o projétil funcionando, vamos adicionar inimigos ao jogo. Os inimigos serão representados por uma classe `Invader`, e iremos implementar a lógica de colisão entre o projétil e os invasores.

## Classe Invader
Antes de criar a classe `Invader`, vamos analisar as classes que já temos até agora:

Tanto a classe `PyLady` quanto a classe `ProjectilePyLady` possuem atributos e métodos semelhantes, como `x`, `y`, `width`, `height`, `image`, `move()` e `show()`. Podemos criar uma classe base chamada `Object` que conterá esses atributos e métodos comuns, e as classes `PyLady`, `ProjectilePyLady` e `Invader` herdarão dessa classe base.

```python
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
```

Agora podemos criar a classe `Invader` que herda da classe `Object`. A classe `Invader` implementará métodos específicos para movimentação, dado que os invasores se movem horizontalmente e trocam de direção quando atingem as bordas da tela, além de moverem verticalmente após certo tempo.

Primeiramente, vamos criar um Enum para definir as direções possíveis de movimento dos invasores:

```python
import enum

class Direction(enum.Enum):
    LEFT = "left"
    RIGHT = "right"
```

Inicialize a direção dos invasores no construtor da classe `Game`, logo após a inicialização da PyLady:

```python
        self.direction = Direction.LEFT  # Direção inicial dos invasores
```

Agora, vamos definir as constantes necessárias para os invasores:

```python
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
```

Após isso, podemos definir a classe `Invader`:

```python
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
```

### Inicializando os invasores
Para gerenciar os invasores, vamos adicionar uma lista de invasores na classe `Game`. Essa lista conterá todas as instâncias de `Invader` que serão criadas no jogo.

Dentro do construtor da classe `Game`, vamos inicializar a lista de invasores logo após a inicialização da PyLady e criar alguns invasores para começar o jogo.

```python
        self.invaders = []  # Lista para armazenar os invasores
        for y in range(5):  # Gera 5 linhas de invasores
            # Adiciona uma margem de 150 pixels na tela e calcula o número de colunas de 50 pixels que cabem na tela
            for x in range((SCREEN_WIDTH - 150) // 50):
                # Cria um novo invasor considerando 100 pixels de margem horizontal e 50 pixels de espaçamento vertical
                invader = Invader(x * INVADER_WIDTH * 2 + 100, y * 50 + 50)
                self.invaders.append(invader)
```

### Desenhando os invasores
Dentro do método `draw()` da classe `Game`, vamos adicionar um loop para desenhar todos os invasores na tela. Para isso, vamos iterar sobre a lista de invasores e chamar o método `show()` de cada instância.

Adicione o seguinte código dentro do método `draw()` da classe `Game`, logo após desenhar a PyLady e o projétil:

```python
        for invader in self.invaders:  # Desenha todos os invasores
            invader.show(self.screen)
```

### Movendo os invasores
Como os invasores se movem em um intervalo de tempo, podemos configurar um temporizador para controlar o movimento dos invasores. Dentro do construtor da classe `Game`, vamos inicializar dois temporizadores para controlar o movimento dos invasores.

Para isso, crie duas constantes no início do arquivo para definir os eventos de movimento dos invasores:

```python
MOVE_INVADERS_X = pygame.USEREVENT + 1
MOVE_INVADERS_Y = pygame.USEREVENT + 2
```

Iremos configurar esses eventos no construtor da classe `Game`, após definir o clock do jogo:

```python
        pygame.time.set_timer(MOVE_INVADERS_X, 500)  # Movimenta os invasores horizontalmente a cada meio segundo
        pygame.time.set_timer(MOVE_INVADERS_Y, 2000)  # Movimenta os invasores verticalmente a cada 2 segundos
```

Agora, dentro do método `handle_events()` da classe `Game`, vamos verificar se os eventos de movimento dos invasores foram acionados e chamar os métodos correspondentes para mover os invasores. Adicione o seguinte código após a leitura do evento de fechamento da janela:


```python
            if event.type == MOVE_INVADERS_X:
                self.move_invaders_x()

            if event.type == MOVE_INVADERS_Y:
                self.move_invaders_y()
```

### Movendo os invasores verticalmente
Vamos criar o método `move_invaders_y()` na classe `Game`, que irá mover todos os invasores verticalmente. Esse método irá iterar sobre a lista de invasores e chamar o método `move_y()` de cada instância.

```python
    def move_invaders_y(self):
        for invader in self.invaders:
            invader.move_y()  # Move o invasor verticalmente
```
### Movendo os invasores horizontalmente
Vamos criar o método `move_invaders_x()` na classe `Game`, que irá mover todos os invasores horizontalmente. Esse método irá iterar sobre a lista de invasores e chamar o método `move_x()` de cada instância, passando a direção correta.

```python
    def move_invaders_x(self):
        for invader in self.invaders:
            invader.move_x(self.direction)

        if self.invaders:
            if self.invaders[-1].x >= SCREEN_WIDTH - INVADER_WIDTH:
                self.direction = Direction.LEFT
            elif self.invaders[0].x <= 0:
                self.direction = Direction.RIGHT

```

### Verificando colisões
Para verificar colisões entre o projétil e os invasores, podemos adicionar um método `collision()` na classe `Object`, dado que poderemos ter colisões entre diferentes objetos do jogo, como a PyLady, o projétil e os invasores.

Para verificar se dois objetos colidem, podemos utilizar o método `colliderect()` do Pygame, que verifica se dois retângulos colidem.

Adicione o seguinte método na classe `Object`:

```python
    def collision(self, other):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
            pygame.Rect(other.x, other.y, other.width, other.height)
        )
```

Agora, podemos criar um método `check_collisions()` na classe `Game` que irá verificar se o projétil colidiu com algum invasor. Se houver uma colisão, o invasor será removido da lista de invasores e o projétil será desativado.

Caso um invasor colida com a PyLady, ele também será removido da lista de invasores, e o jogo poderá ser finalizado ou uma ação específica poderá ser tomada (como perder uma vida).

```python
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
```

### Chamando o método de verificação de colisões
Vamos chamar o método `check_collision()` dentro do loop do método `run()` da classe `Game`, logo após atualizar a posição do projétil. Isso garantirá que as colisões sejam verificadas a cada quadro do jogo.

```python
            self.check_collision()  # Verifica colisões entre o projétil e os invasores
```

## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_4.py](templates/parte_4.py).

------

# Parte 5: Refatorando o código com herança
Agora que temos os invasores funcionando e a lógica de colisão implementada, podemos refatorar o código para utilizar herança e tornar o código mais modular e reutilizável.

## Refatorando a classe PyLady
Podemos refatorar a classe `PyLady` para que ela herde da classe `Object`, assim como fizemos com a classe `Invader`. Isso nos permitirá reutilizar o código comum entre os objetos do jogo.

Iremos modificar o construtor da classe `PyLady` para chamar o construtor da classe `Object` e passar os parâmetros necessários. Podemos remover o método `show()` da classe `PyLady`, pois ele já está implementado na classe `Object`. Manteremos o método `move()` para atualizar a posição da PyLady.

```python
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
```

## Refatorando a classe ProjectilePyLady
Podemos refatorar a classe `ProjectilePyLady` para que ela também herde da classe `Object`. Assim como fizemos com a classe `PyLady`, iremos modificar o construtor da classe `ProjectilePyLady` para chamar o construtor da classe `Object` e passar os parâmetros necessários, além de remover o método `show()`.

```python
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
```
## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_4.py](templates/parte_4.py).

------

# Parte 6: Adicionando o projétil dos invasores
Agora que temos os invasores funcionando e a lógica de colisão implementada, vamos adicionar o projétil disparado pelos invasores. Esse projétil será semelhante ao projétil disparado pela PyLady, mas terá sua própria classe e lógica de movimento.

## Classe ProjectileInvader
Iremos criar uma classe `ProjectileInvader` que representará o projétil disparado pelos invasores. Essa classe herdará da classe `Object`, assim como fizemos com as classes `PyLady` e `ProjectilePyLady`.

```python
class ProjectileInvader(Object):
    def __init__(self, x, y, image=PROJECTILE_INVADER_IMG):
        self.active = True
        super().__init__(image, PROJECTILE_WIDTH, PROJECTILE_HEIGHT, x, y)

    def move(self):
        if self.active:
            self.y += PROJECTILE_INVADER_SPEED
            if self.y > SCREEN_HEIGHT:
                self.active = False
```

Dentro do construtor da classe `Game`, vamos inicializar uma lista para armazenar os projéteis disparados pelos invasores, logo após a inicialização da lista de invasores:

```python
        self.projectiles_invaders = []  # Lista para armazenar os projéteis disparados pelos invasores
```

### Disparando o projétil dos invasores
Iremos sortear um invasor aleatório para disparar o projétil a cada 2 segundos. Para isso, vamos criar um evento de disparo de projétil dos invasores.

Adicione o seguinte código no início do arquivo, logo após a definição dos eventos de movimento dos invasores:

```python
INVADERS_SHOOT = pygame.USEREVENT + 3
```

Agora, dentro do construtor da classe `Game`, vamos configurar o temporizador para disparar o projétil dos invasores a cada 2 segundos:

```python
        pygame.time.set_timer(INVADERS_SHOOT, INVADER_TIME_SHOOT)  # Dispara o projétil dos invasores a cada 2 segundos
```

Dentro do método `handle_events()` da classe `Game`, vamos verificar se o evento de disparo dos invasores foi acionado e chamar o método `invader_shoot()` para disparar o projétil.

Adicione o seguinte código após a verificação do evento de fechamento da janela:

```python
            if event.type == INVADERS_SHOOT:
                self.invader_shoot()  # Dispara o projétil dos invasores
```

Agora, vamos implementar o método `invader_shoot()` na classe `Game`, que irá sortear um invasor aleatório e disparar o projétil a partir da posição do invasor.

Importe a biblioteca `random` no início do arquivo, caso ainda não tenha feito isso:

```python
import random
```

Adicione o método `invader_shoot()` na classe `Game`:

```python
    def invader_shoot(self):
        invader_to_shoot = random.choice(self.invaders)  # Seleciona um invasor aleatório da lista de invasores
        self.projectiles_invaders.append(
            ProjectileInvader(
                invader_to_shoot.x + INVADER_WIDTH // 2,
                invader_to_shoot.y + INVADER_HEIGHT,
            )
        )
```

### Movendo os projéteis dos invasores
Atualize o método `update()` da classe `Game` para mover os projéteis disparados pelos invasores. Adicione o seguinte código logo após atualizar a posição do projétil da PyLady:

```python
        for projectile in self.projectiles_invaders:
            projectile.move()  # Move o projétil dos invasores
            if not projectile.active:
                self.projectiles_invaders.remove(projectile)  # Remove o projétil se não estiver ativo
```

### Desenhando os projéteis dos invasores
Dentro do método `draw()` da classe `Game`, vamos adicionar um loop para desenhar todos os projéteis disparados pelos invasores. Para isso, vamos iterar sobre a lista de projéteis dos invasores e chamar o método `show()` de cada instância.

Adicione o seguinte código dentro do método `draw()`, logo após desenhar os invasores:

```python
        for projectile_invader in self.projectiles_invaders:  # Desenha todos os projéteis dos invasores
            projectile_invader.show(self.screen)
```

## Verificando colisões com os projéteis dos invasores
Para verificar colisões entre os projéteis dos invasores e a PyLady, podemos reutilizar o método `check_collision()` que já implementamos anteriormente. Vamos adicionar a verificação de colisão entre os projéteis dos invasores e a PyLady.

Caso um projétil dos invasores colida com a PyLady, iremos remover o projétil da lista de projéteis dos invasores e, se necessário, implementar alguma lógica para lidar com a colisão (como diminuir a vida da PyLady ou encerrar o jogo).

Adicione o seguinte código dentro do método `check_collision()` da classe `Game`, logo após verificar a colisão entre o projétil da PyLady e os invasores:

```python
        # Verifica se um projétil dos invasores colidiu com a PyLady
        for projectile_invader in self.projectiles_invaders:
            if projectile_invader.collision(self.pylady):
                self.projectiles_invaders.remove(projectile_invader)  # Remove o projétil dos invasores
                exit()  # Encerra o jogo, por exemplo
```

## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_6.py](templates/parte_6.py).

------

# Parte 7: Adicionando vidas e pontuação
Agora que temos os invasores e os projéteis funcionando, vamos adicionar um sistema de vidas e pontuação ao jogo. Isso tornará o jogo mais interessante e desafiador.

## Adicionando vidas
Vamos adicionar uma classe `Life` que representará as vidas da PyLady. Essa classe terá atributos para a posição, imagem e número de vidas restantes, além de métodos para desenhar as vidas na tela.

Primeiro iremos definir as constantes necessárias para as vidas:

```python
LIFE_WIDTH = 30
LIFE_HEIGHT = 22
LIFE_IMG = "img/life.png"
LIFE_QTD = 3
```

Em seguida, crie a classe `Life`:

```python
class Life(Object):
    def __init__(self, x, y, image=LIFE_IMG):
        super().__init__(image, LIFE_WIDTH, LIFE_HEIGHT, x, y)
```

### Inicializando as vidas
Dentro do construtor da classe `Game`, vamos inicializar uma lista para armazenar as vidas da PyLady. Essa lista conterá instâncias da classe `Life`, representando cada vida restante.

```python
        # Posição inicial das vidas
        base_x = SCREEN_WIDTH - LIFE_WIDTH * LIFE_QTD - 30  # Adiciona uma margem de 30 pixels à direita

        self.lives = []
        for i in range(LIFE_QTD):
            self.lives.append(Life(base_x + i * LIFE_WIDTH, 10)) # Adiciona as vidas na parte superior direita da tela
```

### Desenhando as vidas
Dentro do método `draw()` da classe `Game`, vamos adicionar um loop para desenhar todas as vidas na tela. Para isso, vamos iterar sobre a lista de vidas e chamar o método `show()` de cada instância.

Adicione o seguinte código dentro do método `draw()`, logo após desenhar a PyLady:

```python
        for life in self.lives:  # Desenha todas as vidas
            life.show(self.screen)
```

### Removendo vidas
Quando um projétil dos invasores colidir com a PyLady, iremos remover uma vida da lista de vidas. Se não houver mais vidas restantes, o jogo será encerrado.

Modifique o método `check_collision()` da classe `Game` para remover uma vida quando um projétil dos invasores colidir com a PyLady. Troque o `exit()` por uma lógica que verifica se ainda há vidas restantes:

```python
                if self.lives:  # Verifica se ainda há vidas restantes
                    self.lives.pop()  # Remove uma vida
```

### Verificando se o jogo terminou
Para verificar se o jogo terminou, podemos adicionar uma condição no final do método `run()` da classe `Game`, dentro do loop do jogo. Se não houver mais vidas restantes, o jogo será encerrado.
```python
            if not self.lives:  # Verifica se não há mais vidas
                exit()  # Encerra o jogo
```

## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_7.py](templates/parte_7.py).

------

# Parte 8: Adicionando sons
Agora que temos as vidas e a pontuação funcionando, vamos adicionar sons ao jogo para torná-lo mais envolvente. O Pygame possui suporte a reprodução de sons, o que nos permitirá adicionar efeitos sonoros para ações como disparar projéteis, colisões e outras interações.

## Carregando os sons
Primeiro, precisamos definir as constantes para os arquivos de som que iremos utilizar. Vamos adicionar as seguintes constantes no início do arquivo:

```python
HIT_INVADER_SOUND = "sounds/hit_invader.ogg"
HIT_PYLADY_SOUND = "sounds/hit_pylady.ogg"
EXPLOSION_SOUND = "sounds/explosion.ogg"
VICTORY_SOUND = "sounds/victory.ogg"
GAME_RUN_SOUND = "sounds/game_run.ogg"
```

## Criando a classe Sound
Vamos criar uma classe `Sound` que será responsável por carregar e reproduzir os sons do jogo. Essa classe terá métodos para carregar os sons e reproduzi-los quando necessário.

```python
class Sound:
    def __init__(self, sound_path, channel_number, volume=0.3):
        self.sound = pygame.mixer.Sound(sound_path)
        self.channel = pygame.mixer.Channel(channel_number)
        self.channel.set_volume(volume)

    def play(self, loops=0):
        self.channel.play(self.sound, loops=loops)

    def stop(self):
        self.channel.stop()
```

## Inicializando os sons
Dentro do construtor da classe `Game`, vamos inicializar os sons que iremos utilizar no jogo. Vamos criar instâncias da classe `Sound` para cada som que definimos anteriormente.

```python
        self.sound_hit_invader = Sound(HIT_INVADER_SOUND, 0)
        self.sound_hit_pylady = Sound(HIT_PYLADY_SOUND, 1)
        self.sound_victory = Sound(VICTORY_SOUND, 3)
        self.sound_explosion = Sound(EXPLOSION_SOUND, 2)
        self.sound_game_run = Sound(GAME_RUN_SOUND, 6, 0.1)
```

## Reproduzindo os sons
Agora, vamos reproduzir os sons em momentos específicos do jogo. Por exemplo, podemos reproduzir o som de disparo quando a PyLady dispara um projétil, o som de colisão quando um projétil colide com um invasor ou a PyLady, e o som de vitória quando todos os invasores são derrotados.

### Reproduzindo os sons de colisão
Dentro do método `check_collision()` da classe `Game`, vamos reproduzir o som de colisão quando um projétil da PyLady colide com um invasor e quando um projétil dos invasores colide com a PyLady.

#### Colisão do projétil do Invader com a PyLady
Adicione `self.sound_hit_pylady.play()` logo após remover o projétil dos invasores e antes de verificar se ainda há vidas restantes:

```python
                self.sound_hit_pylady.play()  # Reproduz o som de colisão da PyLady
```

#### Colisão do projétil da PyLady com o Invader
Adicione `self.sound_hit_invader.play()` logo após desativar o projétil da PyLady.

```python
                self.sound_hit_invader.play()  # Reproduz o som de colisão do invasor
```

### Reproduzindo o som de fim de jogo
Quando o jogo termina, seja por derrota ou vitória, podemos reproduzir um som específico. Vamos adicionar o som de fim de jogo no final do método `run()` da classe `Game`.

```python
        if not self.invaders:  # Verifica se não há mais invasores
            self.sound_victory.play()  # Reproduz o som de vitória
            pygame.time.delay(2000)  # Aguarda 2 segundos antes de encerrar o jogo
            exit()  # Encerra o jogo
            if not self.invaders:  # Verifica se não há mais invasores
                self.sound_victory.play()  # Reproduz o som de vitória
                pygame.time.delay(2000)  # Aguarda 2 segundos antes de encerrar o jogo
                exit()  # Encerra o jogo

            if not self.lives:  # Verifica se não há mais vidas
                self.sound_explosion.play()  # Reproduz o som de fim de jogo
                pygame.time.delay(2000)  # Aguarda 2 segundos antes de encerrar o jogo
                exit()  # Encerra o jogo

```

## Reproduzindo o som de fundo do jogo
Para adicionar o som de fundo do jogo, podemos reproduzir o som em loop no início do método `run()` da classe `Game`. Isso garantirá que o som de fundo seja reproduzido enquanto o jogo estiver em execução.

Adicione o seguinte código no início do método `run()` da classe `Game`, antes do loop principal:

```python
        self.sound_game_run.play(-1)  # Reproduz o som de fundo do jogo em loop
```

## Resumo do código até agora
O código completo até agora deve se parecer com o arquivo [parte_8.py](templates/parte_8.py).

------

# Extras

## Adicionando pontuação
Para adicionar pontuação ao jogo, podemos criar uma variável para armazenar a pontuação e exibi-la na tela. A pontuação será incrementada sempre que um invasor for destruído.

## Adicionando tela de início e fim
Para tornar o jogo mais interessante, podemos adicionar uma tela de início e uma tela de fim. A tela de início será exibida antes do jogo começar, e a tela de fim será exibida quando o jogo terminar, seja por vitória ou derrota.