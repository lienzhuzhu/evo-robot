import os
import copy

from solution import SOLUTION
import constants as c




class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0

        #self.parent = SOLUTION()
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1



    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        #self.Print()
        #self.Select()

    def Spawn(self):
        self.children = {}
        for i, parent in enumerate(self.parents.values()):
            self.children[i] = copy.deepcopy(parent)
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass

    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")

        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()
