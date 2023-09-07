import BossFactory, pygame, CreateGif

class SpecialBoss(BossFactory.Boss):
    def __init__(self, name, title, dmg, specialTimer, maxLoss, weakenAfter, activeTime, voiceTime, updateSpeedSpecial):
        super().__init__(name, title, maxLoss, weakenAfter, dmg, specialTimer)

        self.activeTime = activeTime*30
        self.voiceTime = voiceTime*30
        self.updateSpeedSpecial = updateSpeedSpecial
        self.hardVoiceTime = self.voiceTime

    
    def GetMapLine(self):
        super().GetMapLine()
        if self.line in ["s", "S"]:
            self.initMove = True


    def PlaySound(self, hit):
        if self.initMove: return
        else: super().PlaySound(hit)


    def Awake(self):
        super().Awake()
        self.specialMove = f"src\\img\\bosses\\{self.name}\\special\\"
        self.specialGroup = pygame.sprite.Group()
        self.specialSprite = CreateGif.Sprite(0,0, self.specialMove)
        self.specialGroup.add(self.specialSprite)

        self.specialMoveVoice = pygame.mixer.Sound(f"src\\audio\\{self.name}\\voice\\voiceS.MP3")
        self.initMove = False
        self.moveCurrentTime = 0

    def Update(self):
        super().Update()
        if self.initMove:
            self.moveCurrentTime+=1

            if self.moveCurrentTime > self.voiceTime:
                self.voiceTime = 1000000
                self.specialMoveVoice.play()

            if self.moveCurrentTime > self.activeTime:
                self.specialSprite.current_sprite = 0
                self.moveCurrentTime = 0
                self.voiceTime = self.hardVoiceTime
                self.initMove = False
            else: 
                self.specialGroup.draw(self.screen)
                self.specialGroup.update(self.updateSpeedSpecial)