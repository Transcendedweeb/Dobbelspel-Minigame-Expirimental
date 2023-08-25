import pygame, os

def TotalFiles(dirName):
    list = os.listdir(dirName)
    number_files = len(list)
    return number_files

def GifLoader(dirName):
    array = []
    counter = 0
    for img in range(TotalFiles(dirName)-1):
        print(f"{dirName}\\{counter}.png")
        i = pygame.image.load(f"{dirName}\\{counter}.png")
        array.append(i)
        counter+=1
    return array