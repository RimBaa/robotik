#! /usr/bin/env python 
import rospy
from sensor_msgs.msg import LaserScan
import math
import ransac

array = []	 
array2 = []
dist = []
def distance(msg):

	for i in range (350,359):
		array.append(msg.ranges[i])	
	for i in range (0,9):
		array.append(msg.ranges[i])
	dist1 = min(array)
	print dist1
	for i in range (280,300):
		array2.append(msg.ranges[i])
		#print msg.ranges[i]
		#   print msg.ranges[359]	
	dist2 = min(array2)
	dist.append((dist1,dist2))
	print dist2
	return

def callback(msg):
	
	distance(msg)
	print dist
	rospy.sleep(15)
	
	return
	


#270 ->rechts
#90 -> links
#180 -> hinten
#359 -> vorne
 

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback, queue_size=1)
rospy.sleep(15)
sub.unregister()
rospy.spin()
