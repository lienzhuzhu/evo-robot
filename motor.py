import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy as np

import constants as c



class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude  = c.AMPLITUDE
        self.frequency  = c.FREQUENCY
        self.offset     = c.PHASE_OFFSET

        if self.jointName == "Torso_BackLeg":
            self.amplitude = c.PI / 2
            self.offset = 0

        x = np.linspace(0, 2*c.PI*c.TIMESTEPS/1000, c.TIMESTEPS)
        self.motor_values   = self.amplitude * np.sin(self.frequency * x + self.offset)

    def Set_Value(self, t, robot_id):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot_id,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motor_values[t],
            maxForce = c.MAX_FORCE
        )

    def Save_Values(self):
        np.save("data/" + self.jointName + ".npy", self.motor_values)


"""
BackLeg_amplitude       = c.PI/2
BackLeg_frequency       = 10
BackLeg_phaseOffset     = 0

FrontLeg_amplitude      = c.PI/3
FrontLeg_frequency      = 10
FrontLeg_phaseOffset    = c.PI/3
"""
