import pyrosim.pyrosim as pyrosim

X   = 0
Y   = 0
Z   = 1.5

LENGTH  = 1
WIDTH   = 2
HEIGHT  = 3


pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box", pos=[X, Y, Z] , size=[LENGTH, WIDTH, HEIGHT])

pyrosim.End()
