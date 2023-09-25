import pyrosim.pyrosim as pyrosim

X   = 0
Y   = 0
Z   = 0.5

LENGTH  = 1
WIDTH   = 1
HEIGHT  = 1


pyrosim.Start_SDF("boxes.sdf")

pyrosim.Send_Cube(name="Box", pos=[X, Y, Z] , size=[LENGTH, WIDTH, HEIGHT])
pyrosim.Send_Cube(name="Box2", pos=[X, Y, Z] , size=[LENGTH, WIDTH, HEIGHT])

pyrosim.End()
