from pygame import *
from random import *
init()

image_generator = font.Font(None, 50)
window = display.set_mode((600, 500))
clock = time.Clock()

class Player():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 10, 100)
        self.hitbox.center = (x, y)
        self.speed = speed
        self.score = 0
        self.score_img = image_generator.render(str(self.score), False, (255, 255, 255))
    def move(self):
        button_list = key.get_pressed()
        if button_list[K_w] == True:
            self.hitbox.y -= self.speed
        elif button_list[K_s] == True:
            self.hitbox.y += self.speed
        if self.hitbox.top < 0:
            self.hitbox.top = 0
        elif self.hitbox.bottom > 500:
            self.hitbox.bottom = 500
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = ball.speed
            ball.randomx = randint(1, 3)
            ball.randomy = randint(1, 3)
    def autopilot(self):
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed
            ball.randomx = randint(1, 2)
            ball.randomy = randint(1, 2)
        if self.hitbox.centery > ball.hitbox.centery:
            self.hitbox.centery -= self.speed
        elif self.hitbox.centery < ball.hitbox.centery:
              self.hitbox.centery += self.speed

class Ball():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 50, 50)
        self.hitbox.center = (x, y)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.randomx = 1
        self.randomy = 1
    def move(self):
        self.hitbox.x += self.speed_x * self.randomx
        self.hitbox.y += self.speed_y * self.randomy
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        elif self.hitbox.bottom > 500:
            self.speed_y = -self.speed
        elif self.hitbox.left < 0:
            self.speed_x = self.speed
            self.hitbox.center = (300, 250)
            draw.rect(window, (0, 255, 0), ball.hitbox)
            display.update()
            time.wait(2000)
            self.randomx = 1
            self.randomy = 1
            player2.score += 1
            player2.score_img = image_generator.render(str(player2.score), False, (255, 255, 255))
        elif self.hitbox.right > 600:
            self.speed_x = -self.speed
            self.hitbox.center = (300, 250)
            draw.rect(window, (0, 255, 0), ball.hitbox)
            display.update()
            time.wait(2000)
            self.randomx = 1
            self.randomy = 1
            player1.score += 1
            player1.score_img = image_generator.render(str(player1.score), False, (255, 255, 255))


player1 = Player(10, 300, 10)
player2 = Player(590, 300, 6)
ball = Ball(300, 300, 4)

while True:
    window.fill((0, 0, 0))
    event_list = event.get()
    for evente in event_list:
        if evente.type == QUIT:
            exit()
    ball.move()
    player1.move()
    player2.autopilot()
    draw.rect(window, (255, 0, 0), player1.hitbox)
    draw.rect(window, (255, 0, 0), player2.hitbox)
    draw.rect(window, (0, 255, 0), ball.hitbox)
    window.blit(player1.score_img, (10, 10))
    window.blit(player2.score_img, (570, 10))
    display.update()
    clock.tick(60)