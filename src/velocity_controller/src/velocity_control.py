# #!/usr/bin/env python
import rospy
import math
from std.msg import Float32

speed_rpm =0
speed_error=0
kp=0.1
r = 3 #radius in cm

#p controller for velocity control
def controller(msg):
	speed_error=msg.data #in m/s
	u= kp*speed_error
	rospy.loginfo("error:"+speed_error)
	speed_rpm = 60 * u / math.pi * r #calculate spedd in rpm
	speed_pub.publish(speed_rpm) #publish speed
	
	
speed_sub = rospy.Subscriber("speedError",controller, Float32,queue_size=10)
speed_pub = rospy.Publisher("drive", Float32,queue_size=10)
rospy.init_node("velocity_control")
rospy.spin()
