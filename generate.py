import pyrosim.pyrosim as pyrosim


X   = 0
Y   = 0
Z   = 0.5

LENGTH  = 1
WIDTH   = 1
HEIGHT  = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[X-2, Y+2, Z] , size=[LENGTH, WIDTH, HEIGHT])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[X, Y, Z] , size=[LENGTH, WIDTH, HEIGHT])
    pyrosim.End()


def main():
    Create_World()
    Create_Robot()


if __name__ == "__main__":
    main()
