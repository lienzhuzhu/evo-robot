import pyrosim.pyrosim as pyrosim
import numpy as np

import constants as c



class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()


    def Prepare_To_Sense(self):
        self.values = np.zeros(c.TIMESTEPS)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
