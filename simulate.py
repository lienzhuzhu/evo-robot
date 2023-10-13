import pyrosim.pyrosim as pyrosim
import numpy as numpy
import pybullet as p
import pybullet_data
import time
import math
import random

GRAVITY = -9.8
TIMESTEPS = 1000
PI = math.pi


def random_angle():
    angle = -PI/2.0 + random.random() * PI
    return angle

physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, GRAVITY)
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("body.urdf")

p.loadSDF("./world.sdf")


pyrosim.Prepare_To_Simulate(robot_id)
backLeg_sensor_values = numpy.zeros(TIMESTEPS)
frontLeg_sensor_values = numpy.zeros(TIMESTEPS)

for i in range(TIMESTEPS):
    p.stepSimulation()
    backLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random_angle(),
        maxForce = 500
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot_id,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random_angle(),
        maxForce = 500
    )

    time.sleep(1/120.0)

numpy.save("data/sensor.npy", backLeg_sensor_values)
numpy.save("data/frontLeg.npy", frontLeg_sensor_values)

p.disconnect()
