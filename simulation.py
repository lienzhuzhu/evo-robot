import pybullet as p
import pybullet_data

from world import WORLD
from robot import ROBOT
import constants as c



GRAVITY     = c.GRAVITY


class SIMULATION:
    def __init__(self):
        self.physics_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0, 0, GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()
