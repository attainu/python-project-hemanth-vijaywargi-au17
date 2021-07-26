import pygame
from sys import exit

pygame.init()   # Starting the Engine 

screen = pygame.display.set_mode((800,600)) # Creating a Window and giving it a Width & Height
pygame.display.set_caption("Snakes & Ladders")
icon = pygame.image.load(r"Assets\Images\icon.png")
pygame.display.set_icon(icon)
woodSurface = pygame.image.load(r"Assets\Images\woodSurface.png")
board = pygame.image.load(r"Assets\Images\board.jpg")

orange = pygame.image.load(r"Assets\Images\orange.png")
red = pygame.image.load(r"Assets\Images\red.png")
green = pygame.image.load(r"Assets\Images\green.png")
blue = pygame.image.load(r"Assets\Images\blue.png")



clock = pygame.time.Clock() # Creating a clock

def move(player,x,y):
    screen.blit(player,(x,y))

# screen.blit(blue,(20,550))    # (posx,posy) Add 60 pixels on x to move right , subtract 60 pixels on y to go up 
# screen.blit(red,(20,490))
# screen.blit(orange,(20,430))
# screen.blit(green,(20,370))

x = 120

while True:
    for event in pygame.event.get():    # Event Loop
        if event.type == pygame.QUIT:   
            pygame.quit()   # Quits Pygame (Stops the Engine)
            exit()  # Exits the Program
    
    screen.blit(woodSurface,(0,0))
    screen.blit(board,(100,0))
    if x < 650:
        x += 5
    move(blue,x,550)
    



    pygame.display.update() # Keeps Updating the display with updated Elements
    clock.tick(60)  # Setting a FrameRate for the Game
    
    




