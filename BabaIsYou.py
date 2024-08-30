import pygame
TILESIZE = 36 # Size of each tile 24x24
GRIDWIDTH = 33 # Amount of tiles across x
GRIDHEIGHT = 18 # Amount of tiles across y
WIDTH = TILESIZE * GRIDWIDTH # Width of screen
HEIGHT = TILESIZE * GRIDHEIGHT #Length of screen
FPS = 60 # FPS
TITLE = "BABA IS PHU" # Title
#RC LIST = {COLUMN, ROW}
#Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
wait = []
pygame.init() # Start pygame
pygame.mixer.init() # Start pygame(if you want sound/music)
#grid(column, row)
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #Creates screen
pygame.display.set_caption(TITLE) #Creates caption
clock = pygame.time.Clock() #Creates clock
babaSpriteRaw = pygame.image.load("babaSprite.png").convert_alpha()
babaSprite = pygame.transform.scale(babaSpriteRaw, (36, 36))
emptySpriteRaw = pygame.image.load("empty.png").convert_alpha()
emptySprite = pygame.transform.scale(emptySpriteRaw, (36, 36))
wallSprite = pygame.transform.scale(pygame.image.load("WALL.png").convert_alpha(),(36,36))
rockSprite = pygame.transform.scale(pygame.image.load("ROCK-1.png").convert_alpha(),(36,36))
flagSprite = pygame.transform.scale(pygame.image.load("FLAG_0-1.png").convert_alpha(),(36,36))
isSprite = pygame.transform.scale(pygame.image.load("Text_IS_0-1.png").convert_alpha(),(36,36))
babaWordSprite = pygame.transform.scale(pygame.image.load("Text_BABA_0-1.png").convert_alpha(),(36,36))
wallWordSprite = pygame.transform.scale(pygame.image.load("Text_WALL_0.png").convert_alpha(),(36,36))
youWordSprite = pygame.transform.scale(pygame.image.load("Text_YOU_0.png").convert_alpha(),(36,36))
stopWordSprite = pygame.transform.scale(pygame.image.load("Text_STOP_0.png").convert_alpha(),(36,36))
rockWordSprite = pygame.transform.scale(pygame.image.load("Text_ROCK_0.png").convert_alpha(),(36,36))
pushWordSprite = pygame.transform.scale(pygame.image.load("Text_PUSH_0.png").convert_alpha(),(36,36))
flagWordSprite = pygame.transform.scale(pygame.image.load("Text_FLAG_0.png").convert_alpha(),(36,36))
winWordSprite = pygame.transform.scale(pygame.image.load("Text_WIN_0.png").convert_alpha(),(36,36))
levelchange = 0
def levels():
    global level
    global baba
    global block1
    global wall1
    global isBlock
    global win
    global winBlock
    global flagBlock
    global babaBlock
    global youBlock
    global rockBlock
    global pushBlock
    global wallBlock
    global stopBlock
    global gridhistory
    global grid
    global levelchange
    level += 1
    levelchange = 1
    for i in grid:

        grid[i] = 'empty'

    if level == 2:


        block1 = Block([(7,10)],'block')
        wall1 = Block([(7,10)],'wall')
        babaBlock = Block([(9,14)],"babaWord")
        isBlock = Block([(5,15),(9,15)],"is")  
        youBlock = Block([(5,16)],"youWord")  
        flagBlock = Block([(5,14)],"flagWord")
        winBlock = Block([(9,16)],"winWord")  
        baba = Block([(7,10)],'baba')
        win = Block([(7,20)],'flag')
    if level == 3:
        block1 = Block([(6,13),(7,13),(8,13)],'block')
        wall1 = Block([(7,10)],'wall')
        babaBlock = Block([(5,14)],"babaWord")
        isBlock = Block([(5,15),(9,15),(4,15)],"is")  
        youBlock = Block([(5,16)],"youWord")  
        flagBlock = Block([(9,14)],"flagWord")
        winBlock = Block([(9,16)],"winWord")  
        rockBlock = Block([(4,14)],'blockWord')
        pushBlock = Block([(4,16)],'pushWord')
        baba = Block([(7,10)],'baba')
        win = Block([(7,20)],'flag')
    if level == 4:
        block1 = Block([(6,13),(7,13),(8,13)],'block')
        wall1 = Block([(7,10)],'wall')
        babaBlock = Block([(5,14)],"babaWord")
        isBlock = Block([(5,15),(9,15),(7,11)],"is")  
        youBlock = Block([(5,16)],"youWord")  
        flagBlock = Block([(9,14)],"flagWord")
        winBlock = Block([(9,16)],"winWord")  
        rockBlock = Block([(6,10)],'blockWord')
        pushBlock = Block([(8,11)],'pushWord')
        baba = Block([(7,10)],'baba')
        win = Block([(7,20)],'flag')
    if level == 5:
        wall1 = Block([(6,13),(7,13),(8,13)],'wall')
        block1 = Block([(7,10)],'block')
        babaBlock = Block([(5,14)],"babaWord")
        isBlock = Block([(5,15),(9,15),(7,11)],"is")  
        youBlock = Block([(5,16)],"youWord")  
        flagBlock = Block([(9,14)],"flagWord")
        winBlock = Block([(9,16)],"winWord")  
        wallBlock = Block([(6,11)],'wallWord')
        stopBlock = Block([(8,11)],'stopWord')
        baba = Block([(7,10)],'baba')
        win = Block([(7,20)],'flag')
    if level == 6:
        wall1 = Block([(6,13),(7,13),(8,13)],'wall')
        block1 = Block([(7,15)],'block')
        babaBlock = Block([(5,14),(8,11)],"babaWord")
        isBlock = Block([(5,15),(9,15),(7,11),(4,15)],"is")  
        youBlock = Block([(5,16)],"youWord")  
        wallBlock = Block([(4,14)],'wallWord')
        stopBlock = Block([(4,16)],'stopWord')
        rockBlock = Block([(6,10)],'blockWord')
        flagBlock = Block([(9,14)],"flagWord")
        winBlock = Block([(9,16)],"winWord")  
        baba = Block([(7,10)],'baba')
        win = Block([(7,20)],'flag')
    if level == 7:
        wall1 = Block([(5,9),(6,9),(7,9),(6,14),(8,9),(9,9),(4,10),(4,11),(4,12),(4,13),(4,14),(4,15),(4,16),(4,17),(5,19),(6,19),(7,19),(8,19),(8,20),(8,21),(7,21),(6,21),(5,21),(4,21),(3,21),(3,20),(3,19),(3,18),(9,14),(9,15),(9,16),(9,17),(9,18),(5,14),(5,10)],'wall')
        block1 = Block([(8,15)],'block')
        babaBlock = Block([(6,13),(9,12)],"babaWord")
        isBlock = Block([(9,11),(10,13),(7,13),(3,16)],"is")  
        youBlock = Block([(8,13)],"youWord")  
        wallBlock = Block([(3,15)],'wallWord')
        stopBlock = Block([(3,17)],'stopWord')
        rockBlock = Block([(8,10)],'blockWord')
        flagBlock = Block([(10,12)],"flagWord")
        winBlock = Block([(10,14)],"winWord")  
        baba = Block([(7,10)],'baba')
        win = Block([(7,20)],'flag')
    if level == 8:
        wall1 = Block([(14,10),(15,10),(7,0),(8,0),(9,0),(10,0),(17,6),(17,4)],'wall')
        block1 = Block([(12,12),(14,12),(14,13),(12,13),(11,13),(10,13),(10,14),(10,15),(10,16),(10,17),(11,17),(12,17),(14,17),(15,17),(15,16),(15,15),(15,14),(15,13),(13,6),(12,6),(11,6),(11,5),(11,4),(11,3),(13,9),(12,9),(12,10),(12,11),(14,8),(16,8),(16,9),(14,9),(16,10),(16,11),(15,11),(14,11),(15,5),(14,6),(14,7),(16,4),(16,5),(16,7),(17,7),(7,6),(7,5),(5,4),(5,5),(7,1),(7,2),(7,3),(6,3),(5,3),(4,3),(3,3),(2,3),(1,3),(0,3),(0,4),(0,5),(0,6),(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(10,2),(11,2),(12,2),(13,2),(14,2),(15,2),(16,2),(17,0),(16,0),(15,0),(14,0),(13,0),(12,0),(11,0)],'block')
        baba = Block([(13,10),(0,0),(17,5)],'baba')
        babaBlock = Block([(5,0)],"babaWord")
        isBlock = Block([(5,1),(13,14),(1,5),(6,1),(14,4)],'is')
        youBlock = Block([(5,2)],'youWord')
        flagBlock = Block([(4,0),(12,15)],"flagWord")
        win = Block([(3,5),(15,9)],'flag')
        rockBlock = Block([(1,4),(14,15)],'blockWord')
        stopBlock = Block([(1,6)],'stopWord')
        pushBlock = Block([(6,2)],'pushWord')
        wallBlock = Block([(14,3)],'wallWord')
        stopBlock = Block([(14,5)],'stopWord')
        winBlock = Block([(13,22)],'winWord')
    if level == 9:
        baba = Block([(9,16)],'baba')
        babaBlock = Block([(8,15)],"babaWord")
        isBlock = Block([(8,16)],'is')
        youBlock = Block([(8,17)],'youWord')
    print(level)


    


class Block(pygame.sprite.Sprite):
    def __init__(self, rclist, character):
        self.rclist = rclist
        self.character = character
        for i in rclist:

            grid[i] = character

    def charFunction(self,event):

        if 'you' in rule[self.character]:

                
            def place(placeList):
                    
                    
                for i in placeList:

                    grid[i[1]] = i[0]

                placeList.clear()
                if grid != gridhistory[-1]:

                    gridhistory.append(grid.copy())

                    drawChar()


            def moveF(event):
                global levelchange
                
                stopped= []
                pushing = 0
                placeList = []
                move = 0
                value1 = 0
                value2 = 0
                dedvalue = 0
                maxi = 0
                pushString = []
                pushString.clear()
                a = gridhistory[-1]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_5:
                        for i in gridhistory[-1]:
                            if gridhistory[-1][i] == 'baba':
                                print(i)
                    if event.key == pygame.K_7:
                        global level
                        level += 1
                    if event.key == pygame.K_6:


                        for i in background:
                            if 'win' in rule[background[i]]:
                                print(i)
                    if event.key == pygame.K_8:


                        for i in grid:
                            if 'you' in rule[grid[i]]:
                                print(i)
                    if event.key == pygame.K_w:

                        value1 =-1
                        value2 = 0
                        dedvalue = 0
                        maxi = 100
                        mini = 0
                        if levelchange == 1:
                            levelchange = 0
                    elif event.key == pygame.K_s:

                        value1 =1
                        value2 = 0
                        dedvalue = 0
                        maxi = GRIDHEIGHT - 1
                        mini = -100
                        if levelchange == 1:
                            levelchange = 0
                    elif event.key == pygame.K_d:

                        value1 =0
                        value2 = 1
                        dedvalue = 1
                        maxi = GRIDWIDTH - 1
                        mini = -100
                        if levelchange == 1:
                            levelchange = 0
                    elif event.key == pygame.K_a:

                        value1 =0
                        value2 = -1
                        dedvalue = 1
                        maxi = 100
                        mini = 0
                        if levelchange == 1:
                            levelchange = 0

                    for i in a:

                        if maxi> i[dedvalue] > mini:

                            if 'stop' not in rule[grid[(i[0]+value1,i[1]+value2)]] :


                                if 'you' in rule[a[i]]:
                                    
                                    if 'push' in rule[grid[(i[0]+value1,i[1]+value2)]]:
                                        
                                        l = -1


                                        while True:
                                            l += 1
                                            if (i[0]+value1+(l*value1),i[1]+value2+(l*value2)) in grid:
                                                    
                                                if 'push' in rule[grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))]]:

                                                    pushString.append((grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))],(i[0]+(value1*2)+(l*value1),i[1]+(value2*2)+(l*value2))))
                                                    print('push')

                                                elif 'you' in rule[grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))]]:
                                                    move = 1

                                                    print('you')

                                                elif 'empty' in rule[grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))]] or 'win' in rule[grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))]] or 'idle' in rule[grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))]]:

                                                    move = 1
                                                    break
                                                else:
                                                    print(grid[(i[0]+value1+(l*value1),i[1]+value2+(l*value2))])
                                                    print('stop')
                                                    move = 0
                                                    break
                                            else:
                                                move = 0
                                                break
                                        if maxi > i[dedvalue] > mini + 1:
                                            if move == 1:

                                                for m in pushString:
                                                    
                                                    placeList.append(m)




                                                if 'win' in rule[grid[(i[0]+value1,i[1]+value2)]]:
                                                    
                                                    levels()
                                                    
                                                        



                                                placeList.append(((grid[(i[0],i[1])]),(i[0]+value1,i[1]+value2)))
                                                for l in pushString:

                                                    
                                                    if l[1] == (i[0],i[1]):
                                                        pushing = 1
                                                if (i[0]-value1,i[1]-value2) not in grid or 'you' not in rule[grid[(i[0]-value1,i[1]-value2)]] and pushing == 0:

                                                    placeList.append((background[(i[0],i[1])],(i[0],i[1])))
                                                if pushing == 1:
                                                    pushing = 0





                                        else:
                                            stopped.append(i)
                                    else:
                                        if maxi > i[dedvalue] > mini:
                                            if 'win' in rule[grid[(i[0]+value1,i[1]+value2)]]:
                                                

                                                levels()
                                                break



                                            placeList.append(((grid[(i[0],i[1])]),(i[0]+value1,i[1]+value2)))
                                            for l in pushString:

                                                
                                                if l[1] == (i[0],i[1]):

                                                    pushing = 1
                                            if (i[0]-value1,i[1]-value2) not in grid or 'you' not in rule[grid[(i[0]-value1,i[1]-value2)]] and pushing == 0:

                                                placeList.append((background[(i[0],i[1])],(i[0],i[1])))
                                            if pushing == 1:

                                                pushing = 0


             
                            else:
                                stopped.append(i)
                    place(placeList)

                    for i in stopped:
                        if maxi> i[dedvalue] > mini + 1 and 'empty' in rule[grid[(i[0]+value1,i[1]+value2)]]:


                            placeList.append((grid[(i[0],i[1])],(i[0]+value1,i[1]+value2)))
                            placeList.append(('empty',(i[0],i[1])))
                    place(placeList)
            moveF(event)
        if 'is' in rule[self.character]:
            rule['baba'] = ['idle']
            rule['wall'] = ['idle']
            rule['block'] = ['idle']
            rule['flag'] = ['idle']
            a = gridhistory[-1]
            
            for i in a:

                if 'is' in rule[a[i]]:

                    if 'noun' in rule[a[(i[0],i[1] - 1)]]:
                        if 'adjective' in rule[a[(i[0],i[1]+1)]]:
                            if a[(i[0],i[1] + 1)].strip("Word") not in rule[a[(i[0],i[1] - 1)].strip("Word")]:
                                rule[a[(i[0],i[1] - 1)].strip("Word")].append(a[(i[0],i[1] + 1)].strip("Word"))
                                try:
                                    rule[a[(i[0],i[1] - 1)].strip("Word")].remove('idle')
                                except:
                                    pass
                                for l in background:
                                    if background[l] == a[(i[0],i[1] - 1)].strip("Word"):
                                        background[l] = 'empty'
                        if 'noun' in rule[a[(i[0],i[1]+1)]]:
                            for g in background:
                                background[g] = 'empty'
                            for l in gridhistory[-1]:
                                if gridhistory[-1][l] == a[(i[0],i[1] - 1)].strip("Word"):
                                    gridhistory[-1][l] = a[(i[0],i[1] +1)].strip("Word")
                                    drawChar()
                    if 'noun' in rule[a[(i[0]-1,i[1])]]:
                        if 'adjective' in rule[a[(i[0]+1,i[1])]]:
                            if a[(i[0]+1,i[1] )].strip("Word") not in rule[a[(i[0]-1,i[1] )].strip("Word")]:
                                rule[a[(i[0]-1,i[1] )].strip("Word")].append(a[(i[0]+1,i[1] )].strip("Word"))
                                rule[a[(i[0]-1,i[1] )].strip("Word")].remove('idle')
                                for l in background:
                                    if background[l] == a[(i[0]-1,i[1] )].strip("Word"):
                                        background[l] = 'empty'
                        if 'noun' in rule[a[(i[0]+1,i[1])]]:
                            for g in background:
                                background[g] = 'empty'
                            for l in gridhistory[-1]:
                                if gridhistory[-1][l] == a[(i[0]-1,i[1] )].strip("Word"):
                                    gridhistory[-1][l] = a[(i[0]+1,i[1] )].strip("Word")
                                    drawChar()
                                



    
    
        
class Character(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.rclist = rclist
        self.spriteIcon = spriteIcon
        for i in rclist:
            
            grid[i] = 'you'


    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'you':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)

    def debug(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print(gridhistory)
            if event.key == pygame.K_2:
                print(len(gridhistory))
            if event.key == pygame.K_3:
                for i in gridhistory[-1]:
                    if gridhistory[-1][i] == 'stop':
                        print(i)
            if event.key == pygame.K_4:
                for i in background:
                    if background[i] == 'flag':
                        print(i)
    def place(self,emptyList,youList,pushList,winString):
        for i in emptyList:
            if i not in youList:
                grid[i] = 'empty'
        for i in youList:
            grid[i] = 'you'
        for i in pushList:
            grid[i[1]] = i[0]
        for i in winString:
            wait.append(i)
        for i in wait:
            if wait[wait.index(i)] != 'null':
                if grid[i[1]] == 'empty':
                    grid[i[1]] = i[0]
                    wait[wait.index(i)] = 'null'
                        
            


                    




        


grid = {}
for i in range(18):
    for j in range(33):
        grid[(i,j)] = 'empty'

gridhistory = []

class Stop(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.spriteIcon = spriteIcon
        self.rclist = rclist
        for i in rclist:
            
            grid[i] = 'stop'


    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'stop':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)
    

class Win(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.spriteIcon = spriteIcon
        self.rclist = rclist
        for i in rclist:
            
            grid[i] = 'win'


    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'win':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)
    



class Push(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.rclist = rclist
        self.spriteIcon = spriteIcon
        for i in rclist:

            grid[i] = 'push'


        
    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'push':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)

    

class Is(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.rclist = rclist
        self.spriteIcon = spriteIcon
        for i in rclist:
            
            grid[i] = 'is'


        
    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'is':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)

                        

                        
class BabaWord(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.rclist = rclist
        self.spriteIcon = spriteIcon
        for i in rclist:
            
            grid[i] = 'babaword'


        
    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'babaword':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)

class YouWord(pygame.sprite.Sprite):
    def __init__(self,rclist,spriteIcon):
        self.rclist = rclist
        self.spriteIcon = spriteIcon
        for i in rclist:
            
            grid[i] = 'youword'


        
    def drawChar(self):
        for i in gridhistory[-1]:
            if gridhistory[-1][i] == 'youword':

                pygame.draw.rect(screen, sprite[self.spriteIcon], [i[1] * 36,i[0] * 36,36,36],0)

                
                

block1 = Block([(7,10)],'block')
wall1 = Block([(7,10)],'wall')
babaBlock = Block([(5,14)],"babaWord")
isBlock = Block([(5,15),(9,15)],"is")  
youBlock = Block([(5,16)],"youWord")  
flagBlock = Block([(9,14)],"flagWord")
winBlock = Block([(9,16)],"winWord")  
baba = Block([(7,10)],'baba')
win = Block([(7,20)],'flag')

#LEVEL 1
level = 1

        

# wall1 = Block([(5,9),(5,10),(5,11),(5,12),(5,13),(5,14),(5,15),(5,16),(5,17),(5,18),(5,19),(5,20),(9,9),(9,10),(9,11),(9,12),(9,13),(9,14),(9,15),(9,16),(9,17),(9,18),(9,19),(9,20)],'wall')
# block1 = Block([(6,15),(7,15),(8,15)],'block')
# win = Block([(7,19)],'flag')
# isBlock = Block([(3,10),(3,19),(11,10),(11,19)],'is')
# babaBlock = Block([(3,9)],'babaWord')
# youBlock = Block([(3,11)],'youWord')
# wallBlock = Block([(3,18)],'wallWord')
# stopBlock = Block([(3,20)],'stopWord')
# rockBlock = Block([(11,9)],'blockWord')
# pushBlock = Block([(11,11)],'pushWord')
# flagBlock = Block([(11,18)],'flagWord')
# winBlock = Block([(11,20)],'winWord')
gridhistory.append(grid.copy())
background = {}
for i in range(18):
    for j in range(33):
        background[(i,j)] = 'empty'
rule = {
    "baba":["you"],
    "wall":["stop"],
    "block":["push"],
    "flag":["win"],
    "empty":["empty"],
    "is":["is","push"],
    "babaWord":['noun','push'],
    "youWord":['adjective','push'],
    'wallWord':['noun','push'],
    'stopWord':['adjective','push'],
    'blockWord':['noun','push'],
    'pushWord':['adjective','push'],
    'flagWord':['noun','push'],
    'winWord':['adjective','push']
    
    
}
sprite = {
    'baba': babaSprite,
    'wall': wallSprite,
    'block': rockSprite,
    'flag': flagSprite,
    'is':isSprite,
    'babaWord':babaWordSprite,
    'youWord':youWordSprite,
    'empty':emptySprite,
    'wallWord':wallWordSprite,
    'stopWord':stopWordSprite,
    'blockWord': rockWordSprite,
    'pushWord': pushWordSprite,
    'flagWord': flagWordSprite,
    'winWord': winWordSprite
    
}
running = True 


def drawChar():



        for i in gridhistory[-1]:

            screen.blit(sprite[gridhistory[-1][i]],(i[1]*36,i[0]*36))
            # pygame.draw.rect(screen, sprite[gridhistory[-1][i]], (i[1] * 36,i[0] * 36,36,36),0)
            if 'win' in rule[gridhistory[-1][i]] or 'idle' in rule[gridhistory[-1][i]]:

                background[i] = gridhistory[-1][i]
            



drawChar()



while running:
    #keeps it running at correct speed
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if len(gridhistory) > 1:
                    for i in gridhistory[-2]:
                        if grid[i] != gridhistory[-2][i]:
                            grid[i] = gridhistory[-2][i]
                        if levelchange == 1:
                            level -= 1
                            levelchange = 0
                    gridhistory.pop(-1)
                    
                drawChar()
        
        baba.charFunction(event)
        wall1.charFunction(event)
        block1.charFunction(event)
        win.charFunction(event)
        isBlock.charFunction(event)




    #Draw / Render on backside



    #After drawing everything, flip display
    pygame.display.flip()
