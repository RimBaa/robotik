#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:55:35 2019

@author: rima
"""

import rospy
from nav_msgs.msg import Odometry


def callback_position(msg):
	rospy.loginfo(msg)

rospy.init_node("map_Position")
map_sub=rospy.Subscriber("/localization/odom/9", Odometry, callback_position, queue_size=10)
rospy.loginfo ("Service started:")
rospy.spin()