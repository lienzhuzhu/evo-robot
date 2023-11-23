import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import pybullet_data
import time
import math
import random

GRAVITY = -9.8
TIMESTEPS = 1000
PI = np.pi


### BEGIN MATH ###

amplitude = PI / 4
frequency = 1.
phaseOffset = 0.

def scale_value(target_range, old_range, val):
    a, b = target_range
    c, d = old_range
    return a + (b - a) * (val - c) / (d - c)


x = np.linspace(0, 2*PI, TIMESTEPS)
#targetAngles = scale_value( (-PI/4., PI/4.) , (-1., 1.), np.sin(x) )
targetAngles = amplitude * np.sin(frequency * x + phaseOffset)
np.save("data/targetAngles.npy", targetAngles)

### END MATH ###


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
        targetPosition = targetAngles[i],
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[i],
        maxForce = 500
    )

    time.sleep(1/1200.)

#np.save("data/backLeg.npy", backLeg_sensor_values)
#np.save("data/frontLeg.npy", frontLeg_sensor_values)

p.disconnect()
