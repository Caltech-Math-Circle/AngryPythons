import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake-like Projectile Motion")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define a function to calculate a parabolic trajectory
def parabolic_trajectory(start_pos, initial_velocity, angle, time):
    g = 9.81  # acceleration due to gravity
    x = start_pos[0] + initial_velocity * math.cos(math.radians(angle)) * time
    y = start_pos[1] - (initial_velocity * math.sin(math.radians(angle)) * time - 0.5 * g * time**2)
    return int(x), int(y)

# Define a function to calculate the slope of the tangent at a point on the trajectory
def tangent_slope(start_pos, initial_velocity, angle, time):
    g = 9.81
    vx = initial_velocity * math.cos(math.radians(angle))
    vy = -initial_velocity * math.sin(math.radians(angle)) - g * time
    return vy / vx

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

    # Draw snake-like projectile at current time step
    if t <= 200:
        start_pos = (100, height - 20)
        initial_velocity = 40
        angle = 45

        time = t / 10
        pos = parabolic_trajectory(start_pos, initial_velocity, angle, time)
        pygame.draw.line(screen, GREEN, start_pos, pos, 5)

        slope = tangent_slope(start_pos, initial_velocity, angle, time)
        x1 = pos[0] - 20
        y1 = pos[1] - 20 * slope
        x2 = pos[0] + 20
        y2 = pos[1] + 20 * slope
        pygame.draw.line(screen, GREEN, (x1, y1), (x2, y2), 5)

        t += time_step
        pygame.display.flip()
    else:
        pygame.quit()
        sys.exit()