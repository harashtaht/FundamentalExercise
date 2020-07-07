### Overall Gameplay ###

'''
In Alien Invasion, the player controls a ship that appears at the bottom center of the screen.
The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
The player shoots and destroys the aliens.
If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet.
If any alien hits the player's ship or reaches the bottom of the screen,
the player loses a ship.
If the player loses three ships, the game ends.
'''

import pygame

import sys

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1000,600)) # originally 1200, 800
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()