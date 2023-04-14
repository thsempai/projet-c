import pgzrun 
from pgzhelper import*
from random import randint

WIDTH = 800
HEIGHT = 600

background = Actor("water", anchor=["left", "top"])

titanic = "musique.mp3"
music.play(titanic)

sound = "scream.wav"
scream = pygame.mixer.Sound(sound)

all_bricks = []

for x in range(1, 8):
    for y in range(2, 10):
        brick = Actor("swimmer")
        brick.scale = 0.2
        brick.pos = [x * 105, y * 40]
        all_bricks.append(brick)

player = Actor("titanic")
player.pos = [WIDTH/2, 550]
player.scale = 0.1

ball = Actor("shark1")
ball.pos = [WIDTH/2, 500]
ball.speed = [0, 0]
ball.scale = 1.8
ball.images = ["shark1", "shark2", "shark3", "shark4"]
ball.fps = 5

blood = Actor("blood2")
blood.pos = [900, 900]
blood.scale = 0.8

lives = []

for y in range(3):
    life = Actor("celine", anchor=[25, 10])
    life.scale = 0.04
    life.pos = [25 * (y+1), 10]
    lives.append(life)

game_over = Actor("gameover")
game_over.pos = [1000, 1000]
game_over.scale = 2

game_win = Actor("win")
game_win.pos = [2000, 2000]
game_win.scale = 0.8

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]
    ball.angle = ball.angle_to(pos)

def on_mouse_down(pos):

    if player.collidepoint(pos): 
        ball.speed = [3, -3]

def invert_horizontal_speed():
    ball.speed[0] = ball.speed[0] * -1

def invert_vertical_speed():
    ball.speed[1] = ball.speed[1] * -1

def reset_ball():
    ball.pos = [WIDTH/2, 500]
    ball.speed = [0, 0]

    on_mouse_down(ball.pos)

def update():
    new_x = ball.pos[0] + ball.speed[0]
    new_y = ball.pos[1] + ball.speed [1]
    ball.pos = [new_x, new_y]
    ball.animate()

    if ball.right > WIDTH or ball.left < 0:
        invert_horizontal_speed()

    if ball.top < 0 :
        invert_vertical_speed()

    if ball.bottom > HEIGHT : 
        lives.remove(lives[-1])
        reset_ball()

    if ball.colliderect(player):
        invert_vertical_speed()
    
    for brick in all_bricks:
        if ball.colliderect(brick):
            all_bricks.remove(brick)
            invert_vertical_speed()
            pygame.mixer.Sound.play(scream)
            blood.pos = brick.pos

    if len(lives) == 0 :
        return

    if len(all_bricks) == 0 :
        return

def draw():
    screen.clear()
    
    background.draw()
    
    for brick in all_bricks:
        brick.draw()
   
    player.draw()
   
    ball.draw()
   
    blood.draw()
    
    for life in lives:
        life.draw()
    
    if len(lives) == 0 :
        screen.clear()
        game_over.pos = [WIDTH/2, HEIGHT/2]
        game_over.draw()

    if len(all_bricks) == 0 :
        screen.clear()
        game_win.pos = [WIDTH/2, HEIGHT/2]
        game_win.draw()

pgzrun.go()