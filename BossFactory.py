import pygame, Circles, pynput

class Boss:
    def __init__(self, name, title, character, maxLoss, weakenAfter, dmg, specialTimer, music):
        self.name = name
        self.title = title
        self.character = character
        self.dmg = dmg
        self.specialTimer = specialTimer
        self.music = music
        self.comboArray = [weakenAfter + num * weakenAfter for num in range(5)]
        self.maxLoss = maxLoss

        self.screen = None
        self.hitpoints = 1000
        self.frames = 0
        self.mapCounter = 0
        self.isWaiting = False
        self.hitList = []
        self.visualTimers = []
        self.fadeActive = True
        self.fadeAlpha = 255
        self.fadeSurface = pygame.Surface((1920, 1080), pygame.SRCALPHA)
        self.currentCombo = 0
        self.rawCombo = 0
        self.loss = maxLoss/5
        self.Awake()


    def LoadUi(self):
        self.FadeEffect()
        self.LoadBossUi()
        
        pygame.draw.rect(self.screen, (100, 100, 100 ), ((100, 100), (200, 20)))
        pygame.draw.rect(self.screen, (0, 255, 0), ((100, 100), (200, 20)))

    
    def LoadBossUi(self):
        pygame.draw.rect(self.screen, (100, 100, 100 ), ((360, 900), (1200, 30)))
        self.TextRenderer(pygame.font.Font('src\\fonts\\OptimusPrinceps.TTF', 30), f"{self.name}, {self.title}", (255, 255, 255), justify= (960, 880))

        widthBar = (1200*self.hitpoints)/1000
        pygame.draw.rect(self.screen, (200, 0,0 ), ((360, 900), (widthBar, 30)))


    def SetScreen(self, screen):
        self.screen = screen


    def PlayMusic(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()

    
    def FadeEffect(self):
        if not self.fadeActive: return
        pygame.draw.rect(self.fadeSurface, (0,0,0,self.fadeAlpha), (0,0,1920,1080))
        self.screen.blit(self.fadeSurface, (0,0))
        self.fadeAlpha-=2
        if self.fadeAlpha < 1: self.fadeActive = False


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
        try:    
            if lines[0] == "k":
                line = lines[1:]
                lineList = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.split("_")]
                lineList[3] = lineList[3]*30
                self.hitList.insert(0, lineList)
                self.AddOuterRing(lineList)
            elif lines[0] in ["", " ", "#"]: return
            else: self.CalculateWaitTime(float(lines[0]))
        except: pass


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
        while True:
            with pynput.keyboard.Listener(on_release = self.RemoveInput) as listener:
                listener.join()


    def RemoveInput(self, key):
        try:
            if key.char in ["1","2","3","4"]:
                iKey = int(key.char)
                if self.hitList != [] and iKey == self.hitList[len(self.hitList)-1][0]: 
                    self.hitList = self.hitList[:-1]
                    self.hitpoints-=self.loss
                    self.ChangeCombo(True)
                else: self.ChangeCombo(False)
        except AttributeError: pass


    def ChangeCombo(self, confirm):
        if confirm and self.rawCombo == self.maxLoss: return
        elif confirm: self.rawCombo+=1
        elif self.rawCombo != 0: self.rawCombo-=1

        if self.rawCombo == self.comboArray[0]:
            self.loss = self.maxLoss/5
            self.combo = "d"
        elif self.rawCombo == self.comboArray[1]:
            self.loss = self.maxLoss - (self.maxLoss / 5)*3
            self.combo = "c"
        elif self.rawCombo == self.comboArray[2]:
            self.loss = self.maxLoss - (self.maxLoss / 5)*2
            self.combo = "b"
        elif self.rawCombo == self.comboArray[3]:
            self.loss = self.maxLoss - (self.maxLoss / 5)
            self.combo = "a"
        elif self.rawCombo == self.comboArray[4]:
            self.loss = self.maxLoss
            self.combo = "s"

                    
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
        self.LoadUi()

        self.PlaceHits()

        if not self.isWaiting: self.GetMapLine()
        else:
            self.frames+=1
            if self.frames >= self.wait:
                self.frames = 0
                self.wait = 0
                self.isWaiting = False

        self.UpdateHitTime()