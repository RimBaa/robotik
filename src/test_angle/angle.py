#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:40:55 2018

@author: rima
"""

kp=0.1


def controller(error):
	tmp_ang =0 #drive straight forward
	if error <0:
		#left
		#-0.2 -> 60, -04 30, -0.7 0
		#error : -10 bis 15  straight: <-15 left: >15 right
		tmp_ang=kp*error
	elif error > 0:
		#right
		tmp_ang=kp*error
	print tmp_ang
	map_func(tmp_ang)
	return



def map_func(angle):
	if (angle == 0):
		print "90"
	else:
		if angle <= -0.7:
			print "0"
		elif angle <= -0.4:
			print "30"
		elif angle <= -0.2:
			print "60"
		elif angle >= 0.7:
			print "179"
		elif angle >= 0.4:
			print "150"
		elif angle >= 0.2:
			print "120"
		
	return


controller(-15)
controller(0)
controller(2)
controller(-30)
controller(45)