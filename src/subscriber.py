#!/usr/bin/env python
import complementary_filter.py as cf
import rospy
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Imu
p = rospy.Publisher('imu1', Imu, queue_size=100)
def calback(data):
    quarter = cf.estimate_orientation(a=numpy.array(data[1]),w=numpy.array(data[0])*data[3],t=data[3])
    #This is the required data in imu format (quarternion)
    p.publish(quarter)
def listener():
    rospy.init_node('imu_s_node', anonymous=True)
    rospy.Subscriber("imu", Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
