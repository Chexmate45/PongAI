import numpy as np
from net import NeuralNetwork
import random
from operator import add, sub, mul
import pygame

training_data = np.array([
	[0, 20],
	[240, 300],
	[300, 200],
	[100, 40],
	[60, 70],
	[400, 100],
	[50, 350],
	[45, 450],
	[450, 300],
	[165, 200],
	[70, 20]])

training_labels = np.array([
	-1,
	-1,
	1,
	1,
	-1,
	1,
	-1,
	-1,
	1,
	-1,
	1])


nn = NeuralNetwork(training_data,training_labels)
print(nn.train(1000))


pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

x = 50
y = 150
ballY = 100
ballX = 250
width = 20
height = 60
ballWidth = 10
ballHeight = 10
vel = 5
ballDir = "left-up"

def movement(y, ballY):
	y -= nn.think(y, ballY)*4
	if y < 0:
		y = 0
	if y+height > 500:
		y = 500-height
	return y
def ballMovement(ballX, ballY, ballDir, returnTo):
	if ballDir == "left-up":
		ballX -= 3
		ballY -= 3
	if ballDir == "left-down":
		ballX -= 3
		ballY += 3
	if ballDir == "right-up":
		ballX += 3
		ballY -= 3
	if ballDir == "right-down":
		ballX += 3
		ballY += 3
	if ballX+30 > 500 and ballDir == "right-up":
		ballDir = "left-down"
	if ballX+30 > 500 and ballDir == "right-down":
		ballDir = "left-up"
	if ballY < 0:
		if ballDir == "left-up":
			ballDir = "left-down"
		if ballDir == "right-up":
			ballDir = "right-down"
	if ballY+10 > 500:
		if ballDir == "left-down":
			ballDir = "left-up"
		if ballDir == "right-down":
			ballDir = "right-up"

	if returnTo == "ballx":
		return ballX
	elif returnTo == "bally":
		return ballY
	else:
		return ballDir

def ballCollision(y, x,height,width, ballX, ballY, ballDir):
	if ballX <= x+width and ballX > x:
		if ballY+height >= y and ballY <= y+height:
			if ballDir == "left-up":
				ballDir = "right-down"
			if ballDir == "left-down":
				ballDir = "right-up"
	return ballDir

def addData(y,ballY,returnTo):
	if (y > ballY):
		if returnTo == "data":
			return ([y, ballY])
		if returnTo == "label":
			return (1)
	if (y < ballY):
		if returnTo == "data":
			return ([y, ballY])
		if returnTo == "label":
			return (0)

run = True

while run:
	pygame.time.delay(100)
	y = movement(y, ballY)
	ballX = ballMovement(ballX, ballY, ballDir, "ballx")
	ballY = ballMovement(ballX, ballY, ballDir, "bally")
	ballDir = ballMovement(ballX, ballY, ballDir, "balldir")
	ballDir = ballCollision(y,x,height,width,ballX,ballY,ballDir)
	np.append(training_data, addData(y,ballY, "data"))
	np.append(training_labels, addData(y,ballY, "label"))
	#y += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	win.fill((0,0,0))
	pygame.draw.rect(win, (255,255,255), (x,y,width,height))
	pygame.draw.rect(win, (255,255,255), (ballX,ballY,ballWidth,ballHeight))
	pygame.display.update()
	nn.train(50)

pygame.quit()
