import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import pybullet_data
import time
import math
import random


GRAVITY = -9.8 * 4
TIMESTEPS = 1000 * 5
PI = np.pi


### BEGIN MATH ###

BackLeg_amplitude       = PI/2
BackLeg_frequency       = 10
BackLeg_phaseOffset     = 0

FrontLeg_amplitude      = PI/3
FrontLeg_frequency      = 10
FrontLeg_phaseOffset    = PI/3


x = np.linspace(0, 2*PI*TIMESTEPS/1000, TIMESTEPS)
BackLeg_targetAngles    = BackLeg_amplitude  * np.sin(BackLeg_frequency  * x + BackLeg_phaseOffset)
FrontLeg_targetAngles   = FrontLeg_amplitude * np.sin(FrontLeg_frequency * x + FrontLeg_phaseOffset)

np.save("data/BackLeg_targetAngles.npy", BackLeg_targetAngles)
np.save("data/FrontLeg_targetAngles.npy", FrontLeg_targetAngles)
#exit()

### END MATH ###


physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)


p.setGravity(0, 0, GRAVITY)


### LOAD DESCRIPTION FILES ###
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("./body.urdf")

p.loadSDF("./world.sdf")


pyrosim.Prepare_To_Simulate(robot_id)


BackLeg_sensor_values = np.zeros(TIMESTEPS)
FrontLeg_sensor_values = np.zeros(TIMESTEPS)

for i in range(TIMESTEPS):
    p.stepSimulation()
    BackLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    FrontLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = BackLeg_targetAngles[i],
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLeg_targetAngles[i],
        maxForce = 500
    )

    time.sleep(1/2400.)

#np.save("data/BackLeg.npy", BackLeg_sensor_values)
#np.save("data/FrontLeg.npy", FrontLeg_sensor_values)

p.disconnect()
