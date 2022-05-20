#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    # initialize the node with name test
    rospy.init_node("test")

    # send this
    pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 1)

    # set rate
    rate = rospy.Rate(10)

    # define data type
    t = Twist()
    
    # set value type
    t.linear.x = 0.1

    while not rospy.is_shutdown():
        pub.publish(t)
        rate.sleep()