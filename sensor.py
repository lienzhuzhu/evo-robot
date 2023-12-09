import numpy as np

import constants as c



class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

        self.values = np.zeros(c.TIMESTEPS)
        print(self.values)
