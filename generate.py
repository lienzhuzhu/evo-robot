import pyrosim.pyrosim as pyrosim

LENGTH  = 1
WIDTH   = 1
HEIGHT  = 1


pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[LENGTH, WIDTH, HEIGHT])

pyrosim.End()
