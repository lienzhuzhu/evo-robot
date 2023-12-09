from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()


"""

import pyrosim.pyrosim as pyrosim
import numpy as np
import pybullet as p
import pybullet_data
import time
import math
import random
import constants as c


BackLeg_amplitude       = c.PI/2
BackLeg_frequency       = 10
BackLeg_phaseOffset     = 0

FrontLeg_amplitude      = c.PI/3
FrontLeg_frequency      = 10
FrontLeg_phaseOffset    = c.PI/3

x = np.linspace(0, 2*c.PI*c.TIMESTEPS/1000, c.TIMESTEPS)
BackLeg_targetAngles    = BackLeg_amplitude  * np.sin(BackLeg_frequency  * x + BackLeg_phaseOffset)
FrontLeg_targetAngles   = FrontLeg_amplitude * np.sin(FrontLeg_frequency * x + FrontLeg_phaseOffset)

"""
