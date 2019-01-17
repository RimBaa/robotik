#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:14:52 2019

@author: rima
"""
import sympy as sy
import math
import csv
import matplotlib.pyplot as plt

point_oval=[]
point_list=[]
distance1 =[]
distance2 =[]
x=[]
y=[]
average_dist=0
squar_dist=0
dist_count=0
average_dist1=0
squar_dist1=0

def find_point(point_input):
	global point_oval
	#in cm
	point_input = (float(point_input[0])*100,float(point_input[1])*100)
	
	m1 = (195.5,215.5)
	m2 = (404.5,215.5)

	if (point_input[0]<=185.5):
		delete =[]
		#line from the input point to the center of the 1.circle
		m = (195.5 - point_input[0])/(215.5 - point_input[1])
		b = 195.5 - m * 215.5
		
		if(point_input[1]==215):
			point = (point_input[0]/100,95.0/100)
			
		else:	
		 	# calculate x and y values
			x,y = sy.symbols('x, y')
			eq1 = m*x+b-y
			eq2 = (y-m1[0])**2 + (x-m1[1])**2 - 120.5**2
			solution = sy.solve([eq1,eq2],(x,y))
			
			#if there are more points, keep only the one on the given half circle
			for i in range (len(solution)):
		 		if solution[i][1]>185:
		 			delete.append(solution[i])
		 	if len(delete) > 0:
		 		for i in range (len(delete)):
		 			solution.remove(delete[i])	

			point = (solution[0][1]/100,solution[0][0]/100)

		point_oval.append(point)
		
	elif (point_input[0]>=415):
		delete =[]
		#line from the input point to the center of the 2.circle	
		
		m = (404.5 - point_input[0])/(215.5 - point_input[1])
		b = 404.5 - m * 215.5
		
		
		if(point_input[1]==215):
			point = (point_input[0]/100,336.0/100)
			
		else:	
		 	# calculate x and y value on the circle 
			
			x,y = sy.symbols('x, y')
			eq1 = m*x+b-y
			eq2 = (y-m2[0])**2 + (x-m2[1])**2 - 120.5**2
			solution = sy.solve([eq1,eq2],(x,y))
			
			#keep only the point of the given half circle
		 	for i in range (len(solution)):
		  		if solution[i][1]<415:
		  			delete.append(solution[i])
		  	if len(delete) > 0:
		  		for i in range (len(delete)):
		  			solution.remove(delete[i])	
		
			point = (solution[0][1]/100,solution[0][0]/100)

		point_oval.append(point)
		
		
	elif (point_input[1]<=215.5):
		#left line
		

		point = (point_input[0]/100,95.0/100)
		point_oval.append(point)
			
	elif (point_input[1]>215.5):
		#right line

		point = (point_input[0]/100,336.0/100)
		point_oval.append(point)				
	
#open file with the data and take only the x and y values 
with open("data.txt", mode = 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	for row in csv_reader:
		  content = (row[i] for i in [5,6])
		  content = [float(i) for i in content]
		  point_list.append(content)

#find point on oval
for i in range (0,len(point_list)):
 	find_point(point_list[i])

#calculate distance
for i in range (0,len(point_list)):
	d = math.sqrt((point_list[i][0]-point_oval[i][0])**2+(point_list[i][1]-point_oval[i][1])**2)
	d2 = ((point_list[i][0]-point_oval[i][0])**2+(point_list[i][1]-point_oval[i][1])**2)
	dist_count+=1
	average_dist+=d
	squar_dist+=d2

#average absolute distance
print average_dist/dist_count

#average squared distance	
print squar_dist/dist_count

#plotting
for i in range (len(point_list)):
	x.append(point_list[i][0])
	y.append(point_list[i][1])
	
plt.plot(y,x)
plt.ylabel('x in m')
plt.xlabel('y in m')
plt.show()