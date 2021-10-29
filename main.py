#Adam Silver and Zack Jordan
#"Settling Down and Setting Up Shop: Using Machine Learning to Help Shape Our Neighborhoods"
#
#Version 0.1: Milestone 2 Demo

import numpy as np

f_in = open("input.txt", "r")

for i in range(7):
    temp = f_in.readline()
    if i==2:
        user_income = int(temp)
    elif i==4:
        user_education = int(temp)
    elif i==6:
        user_age = int(temp)


# X = [median household income, % college educated, % under 35]
X_i = np.array( [29762, 0.258, 0.668] ) # Indicators for 2011
X_f = np.array( [39827, 0.369, 0.677] ) # Indicators from 2019
x_u = np.array( [int(user_income>X_f[0]), int(user_education==1), int(user_age>34)] ) # User's input

# Output for demo:
d_income = ((X_f[0]-X_i[0])/X_i[0])*100
d_college = ((X_f[1]-X_i[1])/X_i[1])*100 
d_young = ((X_f[2]-X_i[2])/X_i[2])*100
Y = np.array( [d_income, d_college, d_young] )

total = int(np.sum(Y))
C = np.array( [Y[0]/total, Y[1]/total, Y[2]/total] )

print('Percent change in median household income (2011-2019): ' + str(Y[0]))
print('Percent change in college education (2011-2019): ' + str(Y[1]))
print('Percent change in residents under 35 (2011-2019): ' + str(Y[2]))
print('User\'s gentrification quotient (0=no impact, 100=maximum impact): ' + str(np.sum(np.multiply(x_u, Y))))

# From FCLA (Nesbitt), pg 31:
# percent change = [(X-Y)/Y]*100
# X=data, Y=data from 20 years prior


#TODO: command-line input of user input, import sample data set, implement basic algorithm
# No ML yet, just using weights and equations from FCLA paper.

# Computing dX, where X is a feature, n=num points in data set, x' is new data point:
# dX = X - ((X*(n/n+1)) + (x'/n+1))
# This basically just saves us from having to recompute the whole average

f_in.close()
