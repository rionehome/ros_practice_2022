#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist

#A sample to move the turtlebot2
class Sample():
    def __init__(self):
        self.pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)

    def pub_linear_x(self):     #linear movement
        dist = 1.0      #distance
        speed = 0.2     #speed
        target_time = dist / speed      #calculation of the time required for movement

        t = Twist()
        t.linear.x = speed
        t.angular.z = 0
            
        start_time = time.time()    #get the current time
        end_time = time.time()      #get the current time

        rate = rospy.Rate(30)
        while end_time - start_time <= target_time:  #repeat for as long as needed
            self.pub.publish(t)
            end_time = time.time()  #get the current time
            rate.sleep()

    def pub_angular_z(self):     #rotational movement
        theta = 180.0   #angle
        speed = 40.0    #speed
        target_time = theta / speed     #calculation of the time required for movement

        t = Twist()
        t.linear.x = 0
        t.angular.z = speed * 3.1415 / 180.0    #conversion from degree to radians
            
        start_time = time.time()    #get the current time
        end_time = time.time()      #get the current time

        rate = rospy.Rate(30)
        while end_time - start_time <= target_time:  #repeat for as long as needed
            self.pub.publish(t)
            end_time = time.time()  #get the current time
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('movement_publisher')

    sample = Sample()

    #The following is the operation related to movement
    sample.pub_linear_x()
    sample.pub_angular_z()