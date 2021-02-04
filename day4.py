from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1,5)
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z+4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z-4

import random
for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x + i
    mc.setBlock(x,y,z,35,r)
    
    for j in range(10):
        r = random.randrange(0,16)
        z = z + 1
        mc.setBlock(x,y,z,35,r)
        
r = random.randrange(0, 16)
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data == r:
            mc.postToChat('你找到我了>////<')
            mc.setBlock(hit.pos,57)
            break
        
    elif data < r:
        mc.postToChat('找大一點的ID')
    elif data > r:
        mc.postToChat('找小一點的ID')
        
         
        myID = mc.getPlayerEntityId('Irene0210')
        mc.postToTitle(myID, 'hello')
        
        
        
        
        
list2d = [[1,0,1,1,1,1,1],
          [1,0,0,0,0,0,1],
          [1,0,1,1,1,0,1],
          [1,0,0,0,0,1,1],
          [1,0,1,1,0,0,1],
          [1,0,0,0,1,0,1],
          [1,1,1,1,1,0,1]]
x,y,z = mc.player.getTilePos()
startX = x
startZ = z

for j in range(4):
    for list1d in list2d:
        
        for i in list1d:
            mc.setBlock(x,y,z,i)
            x = x + 1
            
        x = startX
        z = z+1
        
    z = startZ
    y = y+1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        