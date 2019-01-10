#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import UInt8

speed=0
ticks =113
error_sum=0
error=0
error_last=0 
actual_ticks=0
u=0

def callback_error():
	global u
	global actual_ticks
	global error_last
	global error_sum
	u=0
	error = ticks - actual_ticks
	rospy.loginfo("error: %i",error)
	u = 0.1 * error + 0.1*error_last + 0.05 * error_sum
	error_last = error
	error_sum += error 
	actual_ticks =0

def callback_speed(msg):
	global u
	speed = msg.data #rpm
	rospy.loginfo("speed: %i u: %i", speed, u)
	speed -= u
	speed_pub.publish(speed)
	
def callbackTicks(msg):
	global actual_ticks
	now = rospy.get_time()
	while(1):
		now2 = rospy.get_time()
		actual_ticks =actual_ticks+msg.data/(now2-now) #ticks in 1 sec	
		rospy.loginfo("Ticks: %i",actual_ticks)
		if(now2>=now):
			callback_error()
			
rospy.init_node("velocity_control")
speed_pub=rospy.Publisher("velocity", Int16, queue_size=10)
sub_tick = rospy.Subscriber("/ticks", UInt8, callbackTicks, queue_size = 10)
sub_speed = rospy.Subscriber("velocit", Int16, callback_speed, queue_size=10)
rospy.spin()
