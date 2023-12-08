import pybullet as p
import pybullet_data



class WORLD:
    def __init__(self):
        self.plane_id = p.loadURDF("plane.urdf")
        p.loadSDF("./world.sdf")
