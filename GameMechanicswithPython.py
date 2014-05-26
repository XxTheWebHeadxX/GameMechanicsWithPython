from cs1graphics import *
from math import *
from time import sleep


def curveFormula(x):
    #polynomial formula for a pre-defined curve
    return x**1.5 - 1.5*x

def drawCurve(world, pathSize, xpos, ypos, direction):
    #draws a curve to a Canvas
    xpath = 0
    ypath = 0
    for i in range(pathSize):
        xpath+=.5
        p = Circle(1,Point(xpos+xpath, ypos+(direction*curveFormula(xpath))))
        #print p.getReferencePoint().getY()
        world.add(p)

        
def main():
    world = Canvas(600,600)
    drawCurve(world,30,100,300,-1)
    drawCurve(world,30,100,300,1)

main()


        
    
