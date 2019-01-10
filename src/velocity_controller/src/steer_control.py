#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

count =0

def callback(msg):
	global count
	#publish ervery 10th
	if(count >10):
	    u = 0.1 * msg.data
	    map_func(u)     
	    count =0
	    u=0
	    print msg.data
	count= count +1 

def map_func(angle):
	if (angle == 0):
		error_pub.publish(89) 
	else:
		if angle <= -0.7:
			error_pub.publish(0) 
		elif angle <= -0.4:
			error_pub.publish(30)
		elif angle <= -0.2:
			error_pub.publish(60)
		elif angle >= 0.7:
			error_pub.publish(179)
		elif angle >= 0.4:
			error_pub.publish(150)
		elif angle >= 0.2:
			error_pub.publish(120)
		
	return	
   
rospy.init_node("steer_control")
error_sub = rospy.Subscriber("/error", Float32, callback)
error_pub = rospy.Publisher("/steer", Float32, queue_size=1)
rospy.spin()

