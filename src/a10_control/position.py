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
import formel
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
	point = formel.find_point(position_point,lane, distance)
	#print point
	
	
	orientation_list = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w]
	(roll, pitch, yaw) = euler_from_quaternion(orientation_list)
	print roll, pitch, yaw
#
	#yaw angle 
	yaw= (int(yaw))
	yaw_deg=(yaw*180)/math.pi

	#vector orientation
	vector_x = position_point[0]+(math.cos(yaw_deg))
	vector_y = position_point[1]+(math.sin((yaw_deg)))
	
	look_ahead_vector_x = (point[0])
	look_ahead_vector_y = (point[1])

	f_x = look_ahead_vector_x-vector_x
	f_y = look_ahead_vector_y - vector_y
	
	#correction angle
	angle = math.atan(f_y/f_x)
	angle_deg = angle*180/math.pi
	
	
	steer = 90-angle_deg
	
	angle_pub.publish(steer)	
	rospy.sleep(2)

rospy.init_node("trajectory_control")
location_sub = rospy.Subscriber("localization/odom/6",Odometry, callback, queue_size=1)
angle_pub = rospy.Publisher("/control_steer",UInt8, queue_size=1)

rospy.spin()
	


