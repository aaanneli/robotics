#!/usr/bin/env python
import rospy

# Data structure here: http://docs.ros.org/api/sensor_msgs/html/msg/Laser
Scan.html
from sensor_msgs.msg import LaserScan

# This function is called each time a new message arrives on the scan top
#ic. This callback function then prints the range measured to the object d
#irectly in front of the robot by picking the middle element of the ranges
#field of the LaserScan message
def scan_callback(msg):
    range_ahead = msg.ranges[len(msg.ranges)/2]
    print "range ahead: %0.1f" % range_ahead
    
rospy.init_node('reading_ranges')

# you now subscribe to the topic, this is similar to 'rostopic echo /sca
#n' but now the messages are channelled to 'scan_callback' rather than the
#screen
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)

# spin() keeps your node from exiting until the node is shut down. This i
#s thread independent and does not affect the execution of the callbacks
rospy.spin()