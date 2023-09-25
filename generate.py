import pyrosim.pyrosim as pyrosim

X   = 0
Y   = 0
Z   = 0.5

LENGTH  = 1
WIDTH   = 1
HEIGHT  = 1


pyrosim.Start_SDF("boxes.sdf")

DIMS = 3
for x in range(DIMS):
    X = x
    for y in range(DIMS):
        Y = y
        for z in range(DIMS):
            pyrosim.Send_Cube(name="Box"+str(x)+str(y)+str(z), pos=[X, Y, Z+z] , size=[LENGTH * pow(0.9, z), WIDTH * pow(0.9, z), HEIGHT * pow(0.9, z)])


pyrosim.End()
