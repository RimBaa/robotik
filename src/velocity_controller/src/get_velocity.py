#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import math

speed_ms=0
ticks =113
error=0
r = 0.03 #radius in m

rospy.init_node("getVelocity")
speed_pub=rospy.Publisher("velocity", Int16, queue_size=10)
rospy.loginfo ("Service started:")
speed_ms = float(input("m/s: "))
rpm = int(speed_ms * 60 /(2*math.pi*r))
rospy.loginfo("Ticks: %i",ticks )
print (rpm)
speed_pub.publish(rpm)
rospy.spin()
