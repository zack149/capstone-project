#Adam Silver and Zack Jordan
#"Settling Down and Setting Up Shop: Using Machine Learning to Help Shape Our Neighborhoods"
#
#Version 0.1: Milestone 2 Demo

import numpy as np

f_in = open("input.txt", "r")
f_data = open("data.txt", "r")



#TODO: command-line input of user input, import sample data set, implement basic algorithm
# No ML yet, just using weights and equations from FCLA paper.

# Computing dX, where X is a feature, n=num points in data set, x' is new data point:
# dX = X - ((X*(n/n+1)) + (x'/n+1))
# This basically just saves us from having to recompute the whole average
