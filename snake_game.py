#!/bin/env python3

import pygame
import random

### @linuztx python snake game ###
## 2024 ##

# Initialize Pygame
pygame.init()

# Set screen dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Set title
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake block size
block_size = 10

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

# Function to display score on the screen
def display_score(score):
    value = font_style.render(f"Your Score: {score}", True, white)
    screen.blit(value, [0, 0])

# Function to draw the snake on the screen
def draw_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])

# Function to display the message when the game ends
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Function to generate the food
def generate_food(snake_list):
    while True:
        foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        if (foodx, foody) not in snake_list:
            return foodx, foody

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx, foody = generate_food(snake_list)

    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_list)
            snake_length += 1

        # Draw snake and food
        draw_snake(block_size, snake_list)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        # Display score
        display_score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Control frame rate
        clock.tick(15)

    pygame.quit()
    quit()

# Start the game
game_loop()
