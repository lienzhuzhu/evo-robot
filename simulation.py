import pybullet as p
import pybullet_data
import time

from world import WORLD
from robot import ROBOT
import constants as c



class SIMULATION:

    def __init__(self):
        self.physics_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()
        

    def Run(self):
        for t in range(c.TIMESTEPS):
            p.stepSimulation()

            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)

            #time.sleep(1/2400.)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
