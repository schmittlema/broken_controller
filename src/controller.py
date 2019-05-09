#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def publisher():
    pub = rospy.Publisher('vesc/high_level/ackermann_cmd_mex/input/nav_0', AckermannDriveStamped, queue_size=10)
    rospy.init_node('controller_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = AckermannDriveStamped()
        msg.drive.steering_angle = 0
        msg.drive.speed = 2

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
