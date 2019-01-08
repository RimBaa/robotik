#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:23:23 2019

@author: rima
"""
import rospy
from math import sqrt
from std_msgs.msg import UInt8
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry
from std_msgs.msg import String

ticks =0

def callbackTicks(msg):
	global ticks
	ticks =ticks+msg.data
	rospy.loginfo("ticks %d", ticks)

 
def callbackOdom(msg):
    global last_odom
    last_odom = msg
 
 sub_tick = rospy.Subscriber("/ticks", UInt8, callbackTicks, queue_size = 1)
 
 rospy.spin()