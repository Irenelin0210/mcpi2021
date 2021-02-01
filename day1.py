from mcpi.minecraft import Minecraft
mc=Minecraft.create()

print(mc.player.getTilePos())


mc.player.setTilePos(200,12,200)















from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z, =mc.player.getTilePos()
mc.setBlock(x+1,y,z,95,3)
mc.setBlock(x-1,y,z,95,3)
mc.setBlock(x,y,z+1,95,3)
mc.setBlock(x,y,z-1,95,3)
mc.setBlock(x+1,y,z+1,95,3)
mc.setBlock(x+1,y,z-1,95,3)
mc.setBlock(x-1,y,z-1,95,3)
mc.setBlock(x-1,y,z+1,95,3)






x,y,z, =mc.player.getTilePos()
mc.setBlocks(x+1000,y,z+1000,x-1000,y,z-1000,46)



















t = 0
while True:
    t = t+1
    mc.postToChat(t)












from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
    x,y,z, = mc.player.getTilePos()
    mc.postToChat('X:'+ str(x)+  'Y:' +str(y)+ 'Z:' +str(z))
    
    
    
    
    

mc.setBlock(x+10,y,z+10,95,3)
mc.setBlock(x+10,y+1,z+10,95,3)
mc.setBlock(x+10,y+2,z+10,95,3)
mc.setBlock(x+10,y+3,z+10,95,3)
mc.setBlock(x+10,y+4,z+10,95,3)
mc.setBlock(x+10,y+5,z+10,95,3)
mc.setBlock(x+10,y+6,z+10,95,3)
mc.setBlock(x+10,y+7,z+10,95,3)
mc.setBlock(x+10,y+8,z+10,95,3)
















from mcpi.minecraft import Minecraft
mc=Minecraft.create()


import random
import time 
x,y,z =mc.player.getTilePos()

while True:
    r=random.randrange(0,16)
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,95,r)
    time.sleep(0.1)


























