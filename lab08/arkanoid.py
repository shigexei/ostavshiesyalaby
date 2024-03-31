import pygame 
import random
import time
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#walls
wallW = 100
wallH = 20
wall1 = pygame.Rect(600, 400, wallW,wallH)
wall2 = pygame.Rect(300, 400, wallW, wallH)
 
#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

speed_increase_rate = 1
shrink_rate = 0.25


#Catching sound
collision_sound = pygame.mixer.Sound('data/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
print(block_list)

bonus_brick_list = [pygame.Rect(random.randrange(0, W - 100), 600, 100, 50) for _ in range(3)]
bonus_color = pygame.Color(255, 255, 0)  # Yellow color for bonus bricks
perks = ["speed_up", "paddle_expand"]

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

start_time = time.time()
last_speed_increase_time = start_time
last_shrink_time = start_time

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # print(next(enumerate(block_list)))
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    for bonus_brick in bonus_brick_list:
        pygame.draw.rect(screen, bonus_color, bonus_brick)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))
    pygame.draw.rect(screen, pygame.Color(0,255,0), wall1)
    pygame.draw.rect(screen, pygame.Color(0,255,0), wall2)
    current_time = time.time()
    if current_time - last_speed_increase_time > 10:
        last_speed_increase_time = current_time
        ballSpeed += speed_increase_rate
    if current_time - last_shrink_time > 10:
        last_shrink_time = current_time
        paddleW -= int(shrink_rate * paddleW)
        paddle.width = max(paddleW, 20)


    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    if ball.colliderect(wall1):
        dx, dy = detect_collision(dx, dy, ball, wall1)
    if ball.colliderect(wall2):
        dx, dy = detect_collision(dx, dy, ball, wall2)
    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
    bonus_hit_index = ball.collidelist(bonus_brick_list)
    
    if bonus_hit_index != -1:
        bonus_hit_rect = bonus_brick_list.pop(bonus_hit_index)
        bonus_perk = perks[random.randint(0, len(perks) - 1)]
        if bonus_perk == "speed_up":
            ballSpeed += 2
        elif bonus_perk == "paddle_expand":
            paddleW += 50
            paddle.width = paddleW
        game_score += 10
        collision_sound.play()

        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)