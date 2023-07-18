import pygame


fillColors = {}
tpColors = {}

def Awake():
    global fillColors, tpColors
    fillPath = "src\\img\\combat_probs\\circles\\fill\\"
    tpPath = "src\\img\\combat_probs\\circles\\tp\\"

    fillGreen = pygame.image.load(f"{fillPath}green.PNG")
    fillRed = pygame.image.load(f"{fillPath}red.PNG")
    fillBlue = pygame.image.load(f"{fillPath}blue.PNG")
    fillYellow = pygame.image.load(f"{fillPath}yellow.PNG")
    fillPurple = pygame.image.load(f"{fillPath}purple.PNG")

    tpGreen = pygame.image.load(f"{tpPath}green.PNG")
    tpRed = pygame.image.load(f"{tpPath}red.PNG")
    tpBlue = pygame.image.load(f"{tpPath}blue.PNG")
    tpYellow = pygame.image.load(f"{tpPath}yellow.PNG")
    tpPurple = pygame.image.load(f"{tpPath}purple.PNG")

    fillColors = {
            "red": fillRed,
            "green": fillGreen,
            "blue": fillBlue,
            "yellow": fillYellow,
            "purple": fillPurple,
        }
    
    tpColors = {
            "red": tpRed,
            "green": tpGreen,
            "blue": tpBlue,
            "yellow": tpYellow,
            "purple": tpPurple,
        }