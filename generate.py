import pyrosim.pyrosim as pyrosim

LENGTH  = 1
WIDTH   = 2
HEIGHT  = 3


pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[LENGTH, WIDTH, HEIGHT])

pyrosim.End()
