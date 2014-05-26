from cs1graphics import *
from math import *
from time import sleep


def curveFormula(x):
    #polynomial formula for a pre-defined curve
    return x**1.2 - 1.2*x + 2

def drawCurve(world, pathSize, xpos, ypos, direction):
    #draws a curve to a Canvas
    xpath = 0
    ypath = 0
    for i in range(pathSize):
        xpath+=.5
        p = Circle(1,Point(xpos+xpath, ypos+(direction*curveFormula(xpath))))
        #print p.getReferencePoint().getY()
        world.add(p)

def drawHill(world,pathSize,xpos,ypos):
    #draws a hill by drawing two curves
    xpath = 0
    ypath = 0
    for i in range(pathSize/2):
        xpath+=.5
        p = Circle(1,Point(xpos-xpath, ypos+(curveFormula(xpath))))
        world.add(p)

    #xpos=p.getReferencePoint().getX()
    #ypos=p.getReferencePoint().getY()
    xpath = 0
    ypath = 0
    for i in range(pathSize/2):
        xpath+=.5
        p = Circle(1,Point(xpos+xpath, ypos+(curveFormula(xpath))))
        world.add(p)
    

        
def main():
    world = Canvas(600,600)
    #drawCurve(world,50,100,300,-1)
    #drawCurve(world,50,100,300,1)
    drawHill(world,150,100,300)

main()


        
    
