import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(231, 76, 60)
green = pygame.Color(46, 204, 113)
blue = pygame.Color(52, 152, 219)
purple = pygame.Color(155, 89, 182)

# Define display size
width, height = 800, 600
display = pygame.display.set_mode((width, height))

# Set the caption
pygame.display.set_caption("Cool Snake Game")

# Set the clock
clock = pygame.time.Clock()

# Define snake variables
snake_block = 20

# Define fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def show_score(score, high_score):
    score_text = score_font.render("Score: " + str(score), True, white)
    high_score_text = score_font.render("High Score: " + str(high_score), True, white)
    display.blit(score_text, [0, 0])
    display.blit(high_score_text, [0, 40])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, purple, [x[0], x[1], snake_block, snake_block], border_radius=8)

# Function to display messages
def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Function to get the current high score
def get_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except:
        return 0

# Function to save the new high score
def save_high_score(score):
    high_score = get_high_score()
    if score > high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))

# Main function
def game_loop(snake_speed):
    game_over = False
    game_close = False

    # Starting position
    x1 = width / 2
    y1 = height / 2

    # Initial movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    # Get the high score
    high_score = get_high_score()

    while not game_over:

        while game_close:
            display.fill(black)
            show_message("You Lost! Press C to Play Again or Q to Quit", red)
            show_score(length_of_snake - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop(snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1_change += y1_change
        display.fill(black)

        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block], border_radius=8)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(length_of_snake - 1, high_score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    save_high_score(length_of_snake - 1)
    pygame.quit()
    quit()

# Main menu
def main_menu():
    menu = True

    while menu:
        display.fill(black)
        show_message("Choose Difficulty: E for Easy, M for Medium, H for Hard", blue)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game_loop(10)
                if event.key == pygame.K_m:
                    game_loop(20)
                if event.key == pygame.K_h:
                    game_loop(30)

main_menu()
