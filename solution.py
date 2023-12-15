import os
import time
import numpy
import random
import pyrosim.pyrosim as pyrosim

import constants as c



class SOLUTION:

    def __init__(self, myID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = myID


    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &>/dev/null &")


    def Wait_For_Simulation_To_End(self):

        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        with open("fitness" + str(self.myID) + ".txt", "r") as file:
            self.fitness = float(file.read())
        print(self.fitness)
        os.system("rm fitness" + str(self.myID) + ".txt")


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[c.X-2, c.Y+2, c.Z] , size=[c.LENGTH, c.WIDTH, c.HEIGHT])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[c.X+1.5, c.Y, c.Z+1.0] , size=[c.LENGTH, c.WIDTH, c.HEIGHT])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [c.X+1.0, c.Y, c.Z+0.5])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5] , size=[c.LENGTH, c.WIDTH, c.HEIGHT])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [c.X+2.0, c.Y, c.Z+0.5])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[c.LENGTH, c.WIDTH, c.HEIGHT])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()


    def Mutate(self):
        random_sensor = random.randint(0, c.numSensorNeurons-1)
        random_motor = random.randint(0, c.numMotorNeurons-1)
        self.weights[random_sensor][random_motor] = random.random() * 2 - 1

    def Set_ID(self, myID):
        self.myID = myID
