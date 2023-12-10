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
            self.amplitude = np.pi / 2
            self.offset = 0

        x = np.linspace(0, 2*np.pi*c.TIMESTEPS/1000, c.TIMESTEPS)
        self.motor_values   = self.amplitude * np.sin(self.frequency * x + self.offset)

    def Set_Value(self, desiredAngle, robot_id):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot_id,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.MAX_FORCE
        )

    def Save_Values(self):
        np.save("data/" + self.jointName + ".npy", self.motor_values)


"""
BackLeg_amplitude       = np.pi/2
BackLeg_frequency       = 10
BackLeg_phaseOffset     = 0

FrontLeg_amplitude      = np.pi/3
FrontLeg_frequency      = 10
FrontLeg_phaseOffset    = np.pi/3
"""
