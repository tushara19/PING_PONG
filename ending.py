import pygame
BLACK = (0,0,0)
WHITE = (255, 255, 255)


class Ending(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        
        self.rect = self.image.get_rect()

    def winner(self, screen, win):
        
        font = pygame.font.Font(None, 74)
        text = font.render("winner is " + win, 1, "red")
        screen.blit(text, (40,6))
      

        
        
        
        


    