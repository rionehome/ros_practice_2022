#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("test")
    a = rospy.Publisher("mobile_base/commands/velocity", Twist, queue_size=1)
    n = Twist()
    n.linear.x = 0.1

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        a.publish(n)
        rate.sleep()