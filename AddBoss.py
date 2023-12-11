import BossFactory, SpecialMoveFactory

boss1 = BossFactory.Boss(
    name= "Patrick Ster",
    title= "",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
)

boss2 = BossFactory.Boss(
    name= "Mohammed",
    title= "Islam's Final Stance",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
)

boss3 = BossFactory.Boss(
    name= "Marco",
    title= "The True Fart Lord",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
)

boss4 = SpecialMoveFactory.SpecialBoss(
    name= "Artorias",
    title= "Wolf of the Abyss",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
    activeTime=11.5,
    voiceTime=7.0,
    updateSpeedSpecial = 1
)

boss5 = SpecialMoveFactory.SpecialBoss(
    name= "Raiden Shogun",
    title= "The Electro Archon",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
    activeTime=6,
    voiceTime=2.2,
    updateSpeedSpecial = 1
)

boss6 = SpecialMoveFactory.SpecialBoss(
    name= "Mordekaiser",
    title= "The Bastion of Iron",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
    activeTime=6,
    voiceTime=0.1,
    updateSpeedSpecial = 1
)

boss7 = BossFactory.PreBoss(
    name= "BLANK",
    title= "",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
)

boss8 = SpecialMoveFactory.SpecialBoss(
    name= "Aatrox",
    title= "The World Ender",
    dmg= 200,
    maxLoss= 200,
    weakenAfter= 5,
    activeTime=10.6,
    voiceTime=4.0,
    updateSpeedSpecial = 0.35
)

bossList = [boss1, boss2, boss3, boss4, boss5, boss6, boss7, boss8]