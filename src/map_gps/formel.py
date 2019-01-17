#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:00:35 2019

@author: rima
"""
import sympy as sy
from PIL import Image
import numpy.linalg as numpy
import numpy as np
import math


radius =118.25
p1 = [185,95.21]
p2=[185,335.29]
p3=[415.5,97]
p4=[415.5,333.5]
m1 = (195.5,215.5)
m2 = (404.5,215.5)


def find_point(point_input):
	if (point_input[0]<=185.5):
		delete =[]
		#line from the input point to the center of the 1.circle
		m = (195.5 - point_input[0])/(215.5 - point_input[1])
		b = 195.5 - m * 215.5
		
		if(point_input[1]==215.5):
			point = (point_input[0]/100,95/100)
			print point
		else:	

		 	# calculate x and y value of the point on the circle 
			x,y = sy.symbols('x, y')
			eq1 = m*x+b-y
			eq2 = (y-m1[0])**2 + (x-m1[1])**2 - 120.5**2
			solution = sy.solve([eq1,eq2],(x,y))
			
			#if there are more points, keep only the one of the given half circle
			for i in range (len(solution)):
		 		if solution[i][1]>185:
		 			delete.append(solution[i])
		 	if len(delete) > 0:
		 		for i in range (len(delete)):
		 			solution.remove(delete[i])	

			point = (solution[0][0]/100,solution[0][1]/100)
			print point
		
	elif (point_input[0]>=415):
		delete =[]
		#line from the input point to the center of the 2.circle	
		
		delete =[]
		#line from the input point to the center of the 1.circle
		m = (404.5 - point_input[0])/(215.5 - point_input[1])
		b = 404.5 - m * 215.5
		
		
		if(point_input[1]==215.5):
			point = (point_input[0]/100,336/100)
			print point
		else:	
		 	# calculate x and y value of the point on the circle 
			
			x,y = sy.symbols('x, y')
			eq1 = m*x+b-y
			eq2 = (y-m2[0])**2 + (x-m2[1])**2 - 120.5**2
			solution = sy.solve([eq1,eq2],(x,y))
			
			#if there are more points, keep only the one of the given half circle
		 	for i in range (len(solution)):
		  		if solution[i][1]<415:
		  			delete.append(solution[i])
		  	if len(delete) > 0:
		  		for i in range (len(delete)):
		  			solution.remove(delete[i])	

			point = (solution[0][0]/100, solution[0][1]/100)
			print point
		
		
	elif (point_input[1]<=215):
		#left line

		point = (point_input[0]/100,95.0/100)
		print point	

			
	elif (point_input[1]>215):
		#right line
		
		point = (point_input[0]/100,336.0/100)	
		print point	
		
point_input = (input("Punkt: "))
point_input = (point_input[0]*100,point_input[1]*100)
find_point(point_input)		