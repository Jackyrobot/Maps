import random
size(510,510)
background(255)

def drawStreets():
    theList = [10,60,110,160,210,260,310,360,410,460]
    for y in theList:
        for x in theList:
            noStroke()        
            fill(210)
            rect(x, y, 44, 44)
            
def drawIcon(x, y, iconSize):
    y = y + 10
    fill(255,30,30)
    triangle(x - iconSize/2, y + iconSize/10, x + iconSize/2, y + iconSize/10, x, y + iconSize)
    fill(255,30,30)
    ellipse(x, y, iconSize, iconSize)
    fill(255,0,0)
    ellipse(x, y, iconSize/2, iconSize/2)
    
drawStreets()

i = 0
while i < 50:
    drawIcon((random.random()*500)+5, (random.random()*500)+5, (random.random()*40)+10)
    i = i + 1

Font1 = createFont("Verdana Bold", 45)
textAlign(CENTER, CENTER)
fill(0,255,0)
textFont(Font1)
text("Global Impact",255,255)