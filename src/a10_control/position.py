#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:56:30 2019

@author: rima
"""

import rospy
import math
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import find_look_ahead_point
from std_msgs.msg import UInt8

distance =0.5
lane =1
old_steering=0

def callback(msg):
	global distance
	global lane
	global old_steering
	
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	position_point =(x,y)
	print position_point
	#look ahead point
	point = find_look_ahead_point.find_point(position_point,lane, distance)
	point = (point[1],point[0])
	#print point
	
	
	orientation_list = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
	(roll, pitch, yaw) = euler_from_quaternion(orientation_list)
	print roll, pitch, yaw
#
	#yaw angle 
	yaw_deg=(yaw*180)/math.pi

	#vector orientation
	vector_x = position_point[0]+(math.cos(yaw))
	vector_y = position_point[1]+(math.sin((yaw)))
	
	look_ahead_vector_x = (point[0])
	look_ahead_vector_y = (point[1])

	f_x = vector_x-look_ahead_vector_x
	f_y = vector_y-look_ahead_vector_y 
	
	#correction angle
	angle = math.atan2(f_y,f_x)
	angle_deg = angle*180/math.pi
	
#==============================================================================
# 	
# 	if (yaw>-170 and yaw<-30 ):
# 		steer = angle_deg	
# 	elif (yaw<170 and yaw>30):
# 		steer = 90-angle_deg
# 		
#==============================================================================
		
	print  "angle", angle_deg,"look ahead punkt", point, "yaw", yaw_deg, "yaw_punkt", (vector_x, vector_y), "position", position_point
	#angle_pub.publish(steer)	
	rospy.sleep(2)

rospy.init_node("trajectory_control")
location_sub = rospy.Subscriber("localization/odom/8",Odometry, callback, queue_size=1)
angle_pub = rospy.Publisher("/control_steer",UInt8, queue_size=1)

rospy.spin()
	


