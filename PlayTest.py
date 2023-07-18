import pygame, AddBoss, Circles
from sys import exit
from keyboard import is_pressed

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.toggle_fullscreen
pygame.display.set_caption('Dobbelspel Test Envi')
clock = pygame.time.Clock()
pygame.font.init()
Circles.Awake()

class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.gamestate = 0
        self.level = -1
        self.bossStart = False

    def ExitCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def Stanby(self):
        self.ExitCheck()
        screen.fill((255, 255, 255))
        if is_pressed("space"): 
            self.level+=1
            self.boss = AddBoss.bossList[self.level]
            self.boss.SetScreen(self.screen)
            self.gamestate = 1

        pygame.display.update()

    def BossFight(self):
        self.ExitCheck()

        self.boss.Update()
        pygame.display.update()

    def StateManager(self):
        if self.gamestate == 0:
            self.Stanby()

        else:
            self.BossFight()

gameState = GameState(screen)
while True:
    clock.tick(30)
    gameState.StateManager()