#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from numpy import sign
import time

#A sample to move the turtlebot2
class Super_Sample():
    def __init__(self):
        self.pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
        self.go_back = 0.5      #moveOn_distance
        self.move_on = 0.0      #linear_x's value

    def move(self):
        target_time = 0.05
        
        #acceleration processing
        if self.go_back == 0:
            self.move_on = self.move_on - sign(self.move_on) * 0.01
        elif self.move_on <= 0 and self.move_on >= self.go_back:
            self.move_on = self.move_on - 0.01
        elif self.move_on >= 0 and self.move_on <= self.go_back:
            self.move_on = self.move_on + 0.01
        else:
            self.move_on = self.go_back
        
        t = Twist()
        t.linear.x = self.move_on * 1.0
        t.angular.z = 0

        start_time = time.time()
        end_time = time.time()

        rate = rospy.Rate(50)
        
        while end_time - start_time <= target_time:
            self.pub.publish(t)
            end_time = time.time()
            rate.sleep()
    
    def stop(self):
        self.go_back = 0.0
        while True:
            self.move()
            if self.move_on <= 0:
                break

if __name__ == '__main__':
    rospy.init_node('movement_publisher')

    sample = Super_Sample()

    #The following is the operation related to movement
    r = 1 / 0.05
    rate = rospy.Rate(r)
    n = 0
    while True:
        sample.move()
        if n >= 3 * r:
            break
        n += 1
        rate.sleep()
    sample.stop()
