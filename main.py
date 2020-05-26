

def pyramid(firstCube,lastCube,step,dimensionsNumber) :

    """ Here you can found how many cube you have for a pyramid of a number of big cube.
    """
    a= 0 #initialization
    for i in range (firstCube,(lastCube+1),step): #loop
        a += (i**dimensionsNumber) 
    return a
 
 
 
#example

pyramid(1,11,2,3) #he first cube is 1x1x1, the second is 3x3x3, the third is 5x5x5 etc.. till 11x11x11 ( so firstCube = 1 ; lastcube = 11 ; step = 2 and its a 3d cube [if its 2d : 11x11] so dimensionsNumber = 3 )
# >>> 4356
