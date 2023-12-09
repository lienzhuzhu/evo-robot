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
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0, 0, c.GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()
        

    def Run(self):
        for t in range(c.TIMESTEPS):
            p.stepSimulation()

            self.robot.Sense(t)


            #pyrosim.Set_Motor_For_Joint(
            #    bodyIndex = robot_id,
            #    jointName = "Torso_BackLeg",
            #    controlMode = p.POSITION_CONTROL,
            #    targetPosition = BackLeg_targetAngles[i],
            #    maxForce = 500
            #)

            #pyrosim.Set_Motor_For_Joint(
            #    bodyIndex = robot_id,
            #    jointName = "Torso_FrontLeg",
            #    controlMode = p.POSITION_CONTROL,
            #    targetPosition = FrontLeg_targetAngles[i],
            #    maxForce = 500
            #)

            time.sleep(1/2400.)
