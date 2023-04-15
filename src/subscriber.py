#!/usr/bin/env python
import complementary_filter.py as cf
import rospy
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Imu
def calback(data):
    quarter = cf.estimate_orientation(a=numpy.array(data[1]),w=numpy.array(data[0]),t=numpy.array(data[3]))
def listener():
    rospy.init_node('imu_s_node', anonymous=True)

    rospy.Subscriber("imu", Float64MultiArray, callback)

