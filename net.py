import numpy as np
import random
from operator import add, sub, mul

class NeuralNetwork():
	def __init__(self,data, labels):
		self.weights = np.array([
			random.uniform(0, 2)-1,
			random.uniform(0, 2)-1,
			random.uniform(0, 2)-1])
		self.data = data
		self.labels = labels
	def sigmoid(self, x):
		return 1 / (1 + np.exp(-x))
	def tanh(self, x):
		return np.tanh(x)

	def think(self, in1, in2):
		return self.tanh(in1 * self.weights[0] + in2 * self.weights[1] + self.weights[2])

	def cost(self, pred, label):
		return (pred - label) ** 2
	def slope(self, pred, label):
		return 2 * (pred - label)
	def randomOperation(self, inp, loss):
		ops = (add, sub)
		op = random.choice(ops)
		return op(inp, loss)


	def train(self, iter):
		if not len(self.data) == len(self.labels):
			print("[X] Make sure there are same labels as data!")
		#print(self.weights)
			
		for t in range(iter):
			for i in range(len(self.data)):
				output = self.think(self.data[i][0], self.data[i][1])
				loss = self.cost(output, self.labels[i])
				slope = self.slope(output, self.labels[i])
				#print("In: ",self.data[i][0],self.data[i][1],"Out: ",output," Expected: ", self.labels[i], " Loss: ",loss," Slope: ",slope)
				#print(" ")
				for w in range(len(self.weights)):
					self.weights[w] = self.randomOperation(self.weights[w], loss)
			#print(self.weights)

