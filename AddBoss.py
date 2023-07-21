import BossFactory

testBoss = BossFactory.Boss(
    name= "Test", 
    title= "The True Boss", 
    character= "src\\img\\bosses\\Test.PNG",
    hitpoints= 1000,
    dmg= 5,
    armor= -75,
    bossLevel= 1, 
    specialTimer= 1,
    music= "src\\audio\\testBoss\\testBoss.mp3"
)

bossList = [testBoss]