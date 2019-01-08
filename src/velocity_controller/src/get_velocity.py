#!/usr/bin/env python
import rospy
from velocity_controller.srv import *
from std_msgs.msg import UInt8
from std_msgs.msg import Float32
import math

speed_ms=0
ticks =0
error=0
angular_speed =0
t=1 #time in s

def callbackVelocity(request):
	rospy.loginfo("Geschwindigkeit in m/s " + request.speed + " Ticks: %i", ticks)
	speed_ms=request.speed	
	
	return

def callbackTicks(msg):
	ticks = msg.data
	angular_speed=2* math.pi*ticks/(6*t) #calculate actual velocity from #ticks
	error =speed_ms-angular_speed
	#rospy.loginfo("Ticks: %i",ticks )
	speed_pub.publish(error)
	#drive_pub.publish(angular_speed)
	return


rospy.init_node("getVelocity")
s = rospy.Service('velocity', velocity_controller, callbackVelocity)
rospy.loginfo ("Service started:")
ticks_sub=rospy.Subscriber("/ticks",UInt8, callbackTicks, queue_size=10)
speed_pub=rospy.Publisher("speedError", Float32, queue_size=10)
#drive_pub=rospy.Publisher("speed", Float32, queue_size=10)
rospy.spin()
