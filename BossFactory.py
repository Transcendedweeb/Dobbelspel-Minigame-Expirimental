import pygame, keyboard, Circles

class Boss:
    def __init__(self, name, title, character, hitpoints, dmg, armor, bossLevel, specialTimer, music):
        self.name = name
        self.title = title
        self.character = character
        self.hitpoints = hitpoints
        self.dmg = dmg
        self.armor = armor
        self.bossLevel = bossLevel
        self.specialTimer = specialTimer
        self.music = music

        self.screen = None
        self.frames = 0
        self.mapCounter = 0
        self.isWaiting = False
        self.hitList = []
        self.visualTimers = []
        self.Awake()


    def LoadPlayerAssets(self):
        pygame.draw.rect(self.screen, (100, 100, 100 ), ((100, 100), (200, 20)))
        pygame.draw.rect(self.screen, (0, 255, 0), ((100, 100), (200, 20)))


    def SetScreen(self, screen):
        self.screen = screen


    def PlayMusic(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()


    def TextRenderer(self, font, text, color, location= None, justify = False):
        renderObject = font.render(text, True, color)
        if(justify): self.JustifyText(renderObject, justify)
        else: self.screen.blit(renderObject, location)


    def JustifyText(self, renderObj, location):
        textRect = renderObj.get_rect(center=(location))
        self.screen.blit(renderObj, textRect)


    def CalculateWaitTime(self, time):
        self.wait = (time*30) / 1
        self.isWaiting = True


    def AddOuterRing(self, circle):
        posy = circle[1] + 80
        posx = circle[2] + 80
        time = circle[3]
        color = circle[4]
        radius = 200
        decreaseBy = (radius - 70) / time
        array = [posx, posy, color, radius, decreaseBy]
        self.visualTimers.insert(0, array)  


    def GetMapLine(self):
        with open(f"src\\game_maps\\{self.name}.TXT") as file:
            lines = file.readlines()
            try:
                lines = lines[self.mapCounter].strip()
                self.mapCounter+=1
                file.close()
            except:
                file.close()
                return
            
        if lines[0] == "k":
            line = lines[1:]
            lineList = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.split("_")]
            lineList[3] = lineList[3]*30
            self.hitList.insert(0, lineList)
            self.AddOuterRing(lineList)
        else: self.CalculateWaitTime(float(lines[0]))


    def CreateHit(self, number, posY, posX, color, nextHit):
        if nextHit: self.screen.blit(Circles.fillColors[color], (posX,posY))
        else: self.screen.blit(Circles.tpColors[color], (posX,posY))

        self.TextRenderer(pygame.font.Font('src\\fonts\\Library 3 am.otf', 70), number, (255, 255, 255), justify= (posX+78, posY+78))


    def PlaceHits(self):
        for e, element in enumerate(self.hitList):
            outerCircle = self.visualTimers[e]
            pygame.draw.circle(self.screen, outerCircle[2], (outerCircle[0], outerCircle[1]), outerCircle[3], 5)

            hit = True if e == len(self.hitList)-1 else False
            if element[0] == 1.0: self.CreateHit("1", element[1], element[2], element[4], hit)
            elif element[0] == 2.0: self.CreateHit("2", element[1], element[2], element[4], hit)
            elif element[0] == 3.0: self.CreateHit("3", element[1], element[2], element[4], hit)
            else: self.CreateHit("4", element[1], element[2], element[4], hit)


    def CheckInput(self):
        if any(keyboard.is_pressed(key) for key in ['1', '2', '3', '4']):
            key = int(keyboard.read_key())
            if self.hitList != [] and key == self.hitList[len(self.hitList)-1][0]: 
                self.hitList = self.hitList[:-1]


    def UpdateOuterRing(self, index):
        circle = self.visualTimers[index] # [posx, posy, color, radius, decreaseBy]
        circle[3] = circle[3] - circle[4]


    def UpdateHitTime(self):
        for e, array in enumerate(self.hitList):
            array[3] = array[3] - 1
            self.UpdateOuterRing(e)
            if array[3] <= 0: 
                self.hitList.remove(array)
                self.visualTimers.pop(e)
        



    def Awake(self):
        self.character = pygame.image.load(self.character)

    def Update(self):
        self.screen.blit(self.character, (0,0))
        self.LoadPlayerAssets()

        pygame.draw.rect(self.screen, (100, 100, 100 ), ((360, 900), (1200, 30)))
        pygame.draw.rect(self.screen, (200, 0,0 ), ((360, 900), (1200, 30)))
        self.TextRenderer(pygame.font.Font('src\\fonts\\OptimusPrinceps.TTF', 30), f"{self.name}, {self.title}", (255, 255, 255), justify= (960, 880))

        self.PlaceHits()


        if not self.isWaiting: self.GetMapLine()
        else:
            self.frames+=1
            if self.frames >= self.wait:
                self.frames = 0
                self.wait = 0
                self.isWaiting = False

        self.CheckInput()
        self.UpdateHitTime()