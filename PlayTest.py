import pygame, AddBoss, Circles, threading
from sys import exit
from keyboard import is_pressed

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.toggle_fullscreen
pygame.display.set_caption('Dobbelspel Test Envi')
clock = pygame.time.Clock()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)
Circles.Awake()

class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.gamestate = 0
        self.level = 0
        self.bossStart = False
        self.bgFailed = pygame.image.load("src\\img\\end_boss_bg\\failed.PNG")
        self.bgVictory = pygame.image.load("src\\img\\end_boss_bg\\victory.PNG")

    def ExitCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def Stanby(self):
        self.ExitCheck()
        screen.fill((255, 255, 255))
        if is_pressed("space"):
            if self.level == 7: return
            self.boss = AddBoss.bossList[self.level]
            self.boss.SetScreen(self.screen)
            self.boss.PlayMusic()
            bossThread = threading.Thread(target=self.boss.CheckInput)
            bossThread.daemon = True
            bossThread.start()
            self.gamestate = 20

        pygame.display.update()

    def BossFight(self):
        self.ExitCheck()

        self.boss.Update()
        self.gamestate = self.boss.CheckVictory(self.gamestate)
        pygame.display.update()

    def FinalBoss(self):
        self.level+=1
        self.boss = AddBoss.bossList[self.level]
        self.boss.SetScreen(self.screen)
        self.boss.PlayMusic()
        bossThread = threading.Thread(target=self.boss.CheckInput)
        bossThread.daemon = True
        bossThread.start()
        self.level-=1
        self.gamestate = 20

        pygame.display.update()

    def BossDefeat(self):
        self.ExitCheck()
        self.screen.blit(self.bgFailed, (0,0))
        if is_pressed("1"):
            self.gamestate = 0

        pygame.display.update()

    def BossVictory(self):
        self.ExitCheck()
        self.screen.blit(self.bgVictory, (0,0))
        if is_pressed("1"):
            self.level+=1
            self.gamestate = 0
        
        pygame.display.update()

    def StateManager(self):
        if self.gamestate == 0: self.Stanby()

        elif self.gamestate == 1: self.BossVictory()

        elif self.gamestate == 2: self.BossDefeat()

        elif self.gamestate == 20: self.BossFight()

        elif self.gamestate == 21: self.FinalBoss()

gameState = GameState(screen)
while True:
    clock.tick(30)
    gameState.StateManager()