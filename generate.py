import pyrosim.pyrosim as pyrosim

X   = 0
Y   = 0
Z   = 0.5

LENGTH  = 1
WIDTH   = 1
HEIGHT  = 1


pyrosim.Start_SDF("boxes.sdf")

for i in range(10):
    pyrosim.Send_Cube(name="Box"+str(i), pos=[X, Y, Z+i] , size=[LENGTH, WIDTH, HEIGHT])

pyrosim.End()
