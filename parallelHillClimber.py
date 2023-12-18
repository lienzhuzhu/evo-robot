import os
import copy

from solution import SOLUTION
import constants as c




class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0

        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1



    def Evolve(self):
        self.Evaluate(self.parents)
        for _ in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i, parent in enumerate(self.parents.values()):
            self.children[i] = copy.deepcopy(parent)
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Print(self):
        print()
        for parent, child in zip(self.parents.values(), self.children.values()):
            print(parent.fitness, child.fitness)
        print()

    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Show_Best(self):
        min(self.parents.values(), key=lambda x: x.fitness).Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")

        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()
