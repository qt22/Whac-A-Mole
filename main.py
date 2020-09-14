# only one rat appear at one time
import pygame
import random
import copy
import math
pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
hole_w = 500
hole_h = 280
rat_w = 720
rat_h = 350
hammer_w = 100
hammer_h = 200
# these are the variables for all the images (length of the widths and heights)
# and also the width and the height of the window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("attack_on_rats")
# the name of the window
grass = pygame.image.load('grass.png')
hole = pygame.image.load('hole1.png')
rat = pygame.image.load('rat1.png')
hammer = pygame.image.load('hammer1.png')
grass = pygame.transform.scale(grass, (WINDOW_WIDTH, WINDOW_HEIGHT))
hole = pygame.transform.scale(hole, (hole_w, hole_h))
rat = pygame.transform.scale(rat, (rat_w, rat_h))
hammer = pygame.transform.scale(hammer, (hammer_w, hammer_h))
# load all images that the game needs
# adjust the size of the images
black = [0,0,0]
red = [255, 0, 0]
white = [255, 255, 255]
hole_pos = []  # list of all holes' positions
hole_d0 = 0  # x_space between two holes
hole_d1 = 0  # y_space between two holes
rat_pos = [] # list of all rats' positions

for i in range(9):
   hole_pos.append([math.floor(2 / 15 * WINDOW_WIDTH) + hole_d0,
                    math.floor(7 / 80 * WINDOW_HEIGHT) + hole_d1])
   # the first hole
   hole_d0 += WINDOW_WIDTH / 4
   # holes on the first line
   if 2 / 15 * WINDOW_WIDTH + hole_d0 >= 2 / 3 * WINDOW_WIDTH:
       hole_d0 = 0
       hole_d1 += 5 / 16 * WINDOW_HEIGHT
   # holes on the second line and the third line
   # the distance between holes and edges are in ratio of the width or height of the window
for i in range(9):
   rat_pos.append([hole_pos[i][0]-85, hole_pos[i][1]-65])
   # rats positions are related to hole positions
rat0 = random.randint(0, 8)  # random the rat appear positions
check = 3  # the player has three chances to miss the hit
time0 = 0  # the timer for preparing time
time1 = 0  # the timer for checking the hit and also the appear timer
time2 = 0  # the timer for the game
copy_rat_pos = []
copy_rat_pos = copy.deepcopy(rat_pos)
# copy the rat positions because the rat positions will be changed
# I use deepcopy to make sure the copy doesn't change while the original changes so it can come back
speed = 0  # the frequency of the rat appear time (becomes less and less)
check0 = False  # check whether the player hits the rat or not
clock = pygame.time.Clock()
quit = False
while not quit:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           quit = True

   hammer_pos = pygame.mouse.get_pos()
   hammer_pos = [hammer_pos[0], hammer_pos[1]]
   # the positions of the mouse and where to blit hammer

   window.blit(grass, (0, 0))
   # the background of the game
   clock0 = math.floor(time2/30)
   clock0 = str(clock0)
   # clock0 is the timer for the game
   # it shows you how long the player survives
   check = str(check)
   # check is the chances that the player can miss
   font = pygame.font.SysFont("monospace", 50)
   title1 = font.render(clock0, 1, black)
   title2 = font.render(check, 1, red)
   clock0 = int(clock0)
   check = int(check)
   window.blit(title1, (150, 80))
   # blit the timer at the left top
   window.blit(title2, (150, 300))
   # blit the miss chances at the left side
   for i in range(9):
       window.blit(hole, (hole_pos[i][0], hole_pos[i][1]))
   if time2 % 60 == 0:
       speed += 2
# the speed increases by two every two seconds 
# which means the frequency decreases by two every two seconds
   if time0 >= 60:
       window.blit(rat, (rat_pos[rat0][0], rat_pos[rat0][1]))
       window.blit(hammer, (hammer_pos[0]-50, hammer_pos[1]-30))
       # blit the rats and the hammer
       time1 += 1 # after the prepare time, the timer starts for the rat appear time
       for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN:
               if rat_pos[rat0][0]+275 <= hammer_pos[0] <= rat_pos[rat0][0]+360 \
                and rat_pos[rat0][1]+50 <= hammer_pos[1] <= rat_pos[rat0][1]+220:
                   # if the mouse is clicked in the area which the rat is in
                   rat_pos[rat0][0] += 2000
                   # rat x_pos add 2000 so the rat is offscreen now so the player cannot see it
                   check0 = True
                   # the player hits the rat correctly
       if 60-speed > time1 >= 59-speed and check0 == False:
           check -= 1
# the player doesn't hit the rat or hit it in the wrong position so the player loses 1 miss chance
   if check <= 0:
        quit = True
# if the player uses all three miss chances, the game will end.
   if time1 >= 60-speed:
        rat_pos = copy.deepcopy(copy_rat_pos)
        # because one position is added by 2000 so I need to make the list back
        rat0 = random.randint(0, 8)
        # re-random the position of rats
        time1 = 1
        # the timer of the rat appear time goes back
        check0 = False
        # it was true before so it is needed to change back to false

   if event.type == pygame.QUIT:
        quit = True

   time0 += 1
   time2 += 1
   pygame.display.update()
   clock.tick()

pygame.init() # start a new window for the result
window2 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# the size of the window is the same as the original one
pygame.display.set_caption('attack_on_rats')
# the title is the same too
clock = pygame.time.Clock()
quit = False
while not quit:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          quit = True
  window2.fill(black)
  font = pygame.font.SysFont("monospace", 70)
  title = font.render("GAME OVER", 0, white)
  # the result of the game
  window2.blit(title, (400, 200))# game over
  pygame.display.update()
  clock.tick(60)
pygame.quit()










