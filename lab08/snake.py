import pygame
import time
import random

# initialize pygame
pygame.init()

# set game window size
screen_width = 800
screen_height = 600

# set block size for snake and food
block_size = 20

# set game screen
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# set game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# set game fonts
font_style = pygame.font.SysFont(None, 30)
score_sound = pygame.mixer.Sound('data/score.wav')


def display_score(score, level):
    score_text = font_style.render(f"Score: {score}  Level: {level}", True, blue)
    game_screen.blit(score_text, [0, 0])


def generate_food(snake_list):
    # generate random coordinates for food
    food_x = round(random.randrange(block_size, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(block_size, screen_height - block_size) / block_size) * block_size
    
    # check if the food would spawn on top of the snake
    while [food_x, food_y] in snake_list:
        food_x = round(random.randrange(block_size, screen_width - block_size) / block_size) * block_size
        food_y = round(random.randrange(block_size, screen_height - block_size) / block_size) * block_size
    
    return food_x, food_y

            
def set_game_speed(level):
    # set game speed based on level
    if level == 1:
        speed = 10
    elif level == 2:
        speed = 12.5
    elif level == 3:
        speed = 15
    elif level == 4:
        speed = 17.5
    elif level == 5:
        speed = 20
    elif level == 6:
        speed = 22.5
    elif level == 7:
        speed = 25
    elif level == 8:
        speed = 27.5
    elif level == 9:
        speed = 30
    else:
        speed = 35
    return speed


def snake_game():
    # set initial snake position and length
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_length = 1
    snake_list = []
    
    # set initial food position and weight
    food_x, food_y = generate_food(snake_list)
    food_pos = [food_x, food_y]
    
    # set initial score and level
    score = 0
    level = 1
    
    # set game over state
    game_over = False
    
    # set initial game speed
    speed = set_game_speed(level)
    
    # set game clock
    clock = pygame.time.Clock()
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if window is closed
                game_over = True
            
            elif event.type == pygame.KEYDOWN:
                # set snake movement based on arrow key input
                if event.key == pygame.K_LEFT:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                  snake_y_change = block_size
                  snake_x_change = 0
                
        # check if snake has hit a wall
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_over = True
        
        # update snake position
        snake_x += snake_x_change
        snake_y += snake_y_change
        
        # check if snake has hit the food
        if snake_x == food_x and snake_y == food_y:
            # add food weight to score
            score += 1
            # generate new food
            food_x, food_y = generate_food(snake_list)
            food_pos = [food_x, food_y]
            # increase snake length
            snake_length += 1
            score_sound.play()
        
        # update snake list with new position
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # check if snake has collided with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True
        
        # set game speed based on level
        speed = set_game_speed(level)
        
        # set game screen color
        game_screen.fill(black)
        
        
        # draw snake and food
        for block in snake_list:
            pygame.draw.rect(game_screen, green, [block[0], block[1], block_size, block_size])
        pygame.draw.rect(game_screen, red, [food_pos[0], food_pos[1], block_size, block_size])
        
        # display score and update screen
        display_score(score, level)
        pygame.display.update()
        
        # check for level up
        if score >= level * 10:
            level += 1
        
        # set game clock speed and tick
        clock.tick(speed)
        
    if game_over:
        game_screen.fill(pygame.Color(0,0,0))
        font_go = pygame.font.SysFont('Times New Roman', 60)
        text_go = font_go.render('Game Over', True, pygame.Color('red'))
        game_screen.blit(text_go, (screen_width/2 - text_go.get_width()/2, screen_height/2 - text_go.get_height()/2))
        font_score = pygame.font.SysFont('Arial', 30)
        text_score = font_score.render('Final Score: ' + str(score), True, pygame.Color('red'))
        game_screen.blit(text_score, (screen_width/2 - text_score.get_width()/2, screen_height/2 + text_score.get_height()/2))
        pygame.mixer.init()
        game_over_sound = pygame.mixer.Sound('data/gameover.wav')

    pygame.display.flip()
    game_over_sound.play()
    # Wait for 4 seconds before closing the game window
    time.sleep(4)
    
    # quit pygame and close window
    pygame.quit()
    quit()

# start game
snake_game()