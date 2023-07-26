import BossFactory

testBoss = BossFactory.Boss(
    name= "Test", 
    title= "The True Boss", 
    character= "src\\img\\bosses\\Test.PNG",
    music= "src\\audio\\testBoss\\testBoss.mp3",
    dmg= 5,
    specialTimer= 1,
    maxLoss= 100,
    weakenAfter= 2
)

bossList = [testBoss]