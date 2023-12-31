"""
# run with
python pyangrybirds.py

# make sure you already have pygame installed, via
# pip install pygame
"""

import pygame
import math
import sys
import pdb

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Parabolic Trajectories Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

snake_icon = pygame.image.load('snake_icon.png')
snake_icon = pygame.transform.scale(snake_icon, (50, 30)) 

# Define a function to calculate a parabolic trajectory
def parabolic_trajectory(start_pos, initial_velocity, angle, time):
    g = 9.81  # acceleration due to gravity
    x = start_pos[0] + initial_velocity * math.cos(math.radians(angle)) * time
    y = start_pos[1] - (initial_velocity * math.sin(math.radians(angle)) * time - 0.5 * g * time**2)
    return int(x), int(y)


# Define a function to calculate the tangent at a point on the trajectory
def tangent_at_point(start_pos, initial_velocity, angle, time):
    g = 9.81
    vx = initial_velocity * math.cos(math.radians(angle))
    vy = -initial_velocity * math.sin(math.radians(angle)) - g * time
    return math.atan2(vy, vx)


# Define a function to calculate the first derivative (tangent) at a point on the trajectory
def first_derivative(start_pos, initial_velocity, angle, time):
    g = 9.81
    vx = initial_velocity * math.cos(math.radians(angle))
    vy = initial_velocity * math.sin(math.radians(angle)) - g * time
    return vx, vy
  

# Main game loop
running = True
t = 0
time_step = 0.1  # Time step for drawing the trajectory

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw the ground
    pygame.draw.rect(screen, GREEN, (0, height - 10, width, 10))

    # Draw trajectory and first derivative at current time step
    if t <= 100:
        start_pos = (100, height - 20)
        initial_velocity = 100
        angle = 45

        time = t / 10
        pos = parabolic_trajectory(start_pos, initial_velocity, angle, time)
        pygame.draw.circle(screen, BLUE, pos, 5)

        # Calculate the position for the snake icon
        icon_rect = snake_icon.get_rect(center=pos)

        # # Draw the snake icon
        screen.blit(snake_icon, icon_rect)

        derivative = first_derivative(start_pos, initial_velocity, angle, time)
        # pdb.set_trace();
        end_x = pos[0] + 1 * derivative[0]
        end_y = pos[1] - 1 * derivative[1] # remember it's pixel space?
        pygame.draw.line(screen, BLUE, pos, (end_x, end_y))


        t += time_step
        pygame.display.flip()
    else:
        pygame.quit()
        sys.exit()

