import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import pybullet_data
import time
import math
import random

GRAVITY = -9.8
TIMESTEPS = 1000
PI = math.pi


### Helper Functions ###

def random_angle(angle_range):
    a, b = angle_range
    return a + (b - a) * random.random()

#angles = (-PI/2., PI/2.)
angles2 = (-1, 1)
#angles = (-0.5, 0.5)
#angles = (-0.25, 0.25)
angles1 = (-0.15, 0.15)


physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, GRAVITY)
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("./body.urdf")

p.loadSDF("./world.sdf")


pyrosim.Prepare_To_Simulate(robot_id)
backLeg_sensor_values = np.zeros(TIMESTEPS)
frontLeg_sensor_values = np.zeros(TIMESTEPS)

for i in range(TIMESTEPS):
    p.stepSimulation()
    backLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random_angle(angles2),
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random_angle(angles1),
        maxForce = 500
    )

    time.sleep(1/60.0)

#np.save("data/backLeg.npy", backLeg_sensor_values)
#np.save("data/frontLeg.npy", frontLeg_sensor_values)

p.disconnect()
