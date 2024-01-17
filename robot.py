import os
import pyrosim.pyrosim as pyrosim
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK

from motor import MOTOR
from sensor import SENSOR
import constants as c



class ROBOT:
    def __init__(self, solutionID):
        self.robot_id = p.loadURDF("./body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot_id)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain" + self.solutionID + ".nndf")
        os.system("rm brain" + self.solutionID + ".nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)


    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robot_id)
    
    def Think(self):
        self.nn.Update()
        #self.nn.Print()


    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot_id, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        #print(xCoordinateOfLinkZero)
        with open("tmp" + self.solutionID + ".txt", "w") as file:
            file.write(str(xCoordinateOfLinkZero))

        os.system("mv tmp" + self.solutionID + ".txt fitness" + self.solutionID + ".txt")
