import pyrosim.pyrosim as pyrosim
import pybullet as p

from motor import MOTOR
from sensor import SENSOR



class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robot_id = p.loadURDF("./body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot_id)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
