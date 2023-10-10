import pyrosim.pyrosim as pyrosim
import numpy as numpy
import pybullet as p
import pybullet_data
import time

GRAVITY = -9.8

physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, GRAVITY)
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("body.urdf")

p.loadSDF("./world.sdf")


pyrosim.Prepare_To_Simulate(robot_id)
backLeg_sensor_values = numpy.zeros(1000)

for i in range(1000):
    p.stepSimulation()
    backLeg_sensor_values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/120.0)

p.disconnect()
print(backLeg_sensor_values)
