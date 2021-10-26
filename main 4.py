import pygame
import abc
import random

WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE = (0,0,255)

class Drawable(metaclass = abc.ABCMeta):
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y
		
	def getLoc(self):
		return (self.__x, self.__y)
		
	def setLoc(self,p):
		self.__x = p[0]
		self.__y = p[1]
	
	
	@abc.abstractmethod
	def draw(self,surface):
		pass
	
class Rectangle(Drawable):
    def __init__(self,width, height, color, x=0,y=0):
      super().__init__(x,y) 
      self.width = width
      self.height = height
      self.color = color

    def getX(self):
      return super().getLoc()[0]

    def getY(self):
      return super().getLoc()[1]

    def draw(self, surface):
      x = self.getX()
      y = self.getY()
      pygame.draw.rect(surface, self.color, (x, y, self.width, self.height))

class Snowflake(Drawable):
  def __init__(self, x=0, y=0):
      super().__init__(x,y) # use drawable constructor
    
  def getX(self):
      return super().getLoc()[0]

  def getY(self):
    return super().getLoc()[1]

  def draw(self, surface):
    x = self.getX()
    y = self.getY()
    pygame.draw.line(surface, WHITE, (x - 5, y), (x + 5, y))
    pygame.draw.line(surface, WHITE, (x, y - 5), (x, y + 5))
    pygame.draw.line(surface, WHITE, (x - 5, y - 5), (x + 5, y + 5))
    pygame.draw.line(surface, WHITE, (x - 5, y + 5), (x + 5, y - 5)) 
    
def main():
    pygame.init()


    DISPLAY= pygame.display.set_mode((500,400),0,32)
    DISPLAY.fill(WHITE)

    # snow_list = []

    # for i in range(50):
    #     x = random.randrange(0, 400)
    #     y = random.randrange(0, 400)
    #     snow_list.append([x, y])
    clock = pygame.time.Clock()

    
    random_x = random.randint(0,400) 
    random_y = random.randint(0,400)

    drawable_stuff = []
    green_rect = Rectangle(400,200,GREEN,0,200)
    #green_rect.draw(DISPLAY)
    blue_rect = Rectangle(400,200, BLUE, 0,0)
    drawable_stuff.append(green_rect)
    drawable_stuff.append(blue_rect)
    randomdrop =[0,0]
    while True:

      for stuff in drawable_stuff:
        stuff.draw(DISPLAY)
        if isinstance(stuff,Snowflake):
          x,y= stuff.getLoc()
          if (y<randomdrop[drawable_stuff.index(stuff)]):
            stuff = stuff.setLoc((x,y+5))
      newSnow= Snowflake(random.randint(0,400),0)
      drawable_stuff.append(newSnow)
      randomdrop.append(random.randint(200,400))

      clock.tick(15)
      pygame.display.update()

    
      

main()

#       snows = [] 

# for i in range(0, 100):
#         random_x = random.randint(0,400)  


  #  for snow in snows:
  #       snow.draw(DISPLAY)
  #       pygame.display.update()
  #       CLOCK.tick(15)