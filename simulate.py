import pybullet as p
import pybullet_data
import time

GRAVITY = -9.8

physics_client = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setGravity(0, 0, GRAVITY)
plane_id = p.loadURDF("plane.urdf")



p.loadSDF("./boxes.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/120.0)
    print(i)

p.disconnect()
