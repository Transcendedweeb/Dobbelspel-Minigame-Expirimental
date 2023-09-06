import BossFactory, pygame

class SpecialBoss(BossFactory.Boss):
    def __init__(self, name, title, dmg, specialTimer, maxLoss, weakenAfter, activeTime, voiceTime):
        super().__init__(name, title, maxLoss, weakenAfter, dmg, specialTimer)

        self.activeTime = activeTime*30
        self.voiceTime = voiceTime*30

    
    def GetMapLine(self):
        super().GetMapLine()
        if self.line in ["s", "S"]:
            self.initMove = True


    def Awake(self):
        super().Awake()
        self.specialMove = pygame.image.load(f"src\\img\\bosses\\{self.name}\\special\\special.PNG")
        self.specialMoveVoice = pygame.mixer.Sound(f"src\\audio\\{self.name}\\voice\\voiceS.MP3")
        self.initMove = False
        self.moveCurrentTime = 0

    def Update(self):
        super().Update()
        print(self.initMove, self.moveCurrentTime)
        if self.initMove:
            self.moveCurrentTime+=1

            if self.moveCurrentTime > self.voiceTime:
                self.voiceTime = 1000000
                self.specialMoveVoice.play()

            if self.moveCurrentTime > self.activeTime:
                self.moveCurrentTime = 0
                self.voiceTime = 0
                self.initMove = False
            else: self.screen.blit(self.specialMove, (0,0))