#import and initalize the pygame library
import pygame # we use pygame for writting videoGames
import os # os provides function for creating and removing a folder

class Game:
    def __init__(self):
        self.weight = 1000 #playground weight
        self.height =  750 #playground height
        # set-up the drawing window 
        self.drawing_window =  pygame.display.set_mode((self.weight,self.height))
        self.football_club =[]
        #download image of background                   #file name #images.png        
        self.backGround = pygame.image.load(os.path.join("Images","playground.png"))
        # adapt picture to drawing_window
        self.backGround = pygame.transform.scale(self.backGround,(1000,750))
        self.click = [] #remove
    # run until user press Quit!
    def run (self):
        run = True 
        
        #creating an object to help track time
        clock = pygame.time.Clock()
        # control when program ends
        while run: 
          #EVENT - the main module for dealing with user input in game
          for event in pygame.event.get(): # control event in game(later) 
            #speed
            clock.tick(60)
            # when user click button QUIT, program ends  
            if event.type == pygame.QUIT:
                  run = False
          #defining mouse position
          mouse_position = pygame.mouse.get_pos() # get_pos()...position is in tuple (x,y)
          if event.type == pygame.MOUSEBUTTONDOWN:
               self.click.append(mouse_position)
               print(self.click)
          self.draw()   
        pygame.quit()
    # we have to drawing Game surface
    def draw(self):
      #blit takes a background and draw in onto the screen with position (x,y)
      # 0,0 -> means, draw in center
      self.drawing_window.blit(self.backGround,(0,0))
      for x in self.click:
        pygame.draw.circle(self.drawing_window,(255,0,0),(x[0],x[1]),5,0)#color,0,0->center
      # update image
      pygame.display.update()
      
g = Game()
g.run()