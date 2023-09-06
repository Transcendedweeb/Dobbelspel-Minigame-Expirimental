import BossFactory, SpecialMoveFactory

testBoss = SpecialMoveFactory.SpecialBoss(
    name= "Raiden Shogun",
    title= "The True Boss",
    dmg= 75,
    specialTimer= 1,
    maxLoss= 20,
    weakenAfter= 5,
    activeTime=5,
    voiceTime=2
)

bossList = [testBoss]