#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
import random
def talker():
    #Initialising random values for the linear and angular accelaration vectors
    Lx=random.randrange(0,5)
    Ly=random.randrange(0,5)
    Lz=random.randrange(0,5)
    Ax=random.randrange(0,5)
    Ay=random.randrange(0,5)
    Az=random.randrange(0,5)
    g=9.8
    rospy.init_node('imu_p_node', anonymous=True)
    pub = rospy.Publisher('imu', Float64MultiArray, queue_size=100) 
    #Initialising an empty message of type Float64MultiArray
    rAz = 0.1
    rLx = 0.025
    #Rates of change of Angular z accelaration and Linear x Accelaration as per given instructions (Time difference between 2 messages is 100 ms)
    for i in range(100):
        my_msg = Float64MultiArray() 
        rate = rospy.Rate(10) # 10hz
        d = [[Ax,Ay,Az+rAz],[Lx+rLx,Ly,Lz],g]
        d= [[float(d[i][j]) for j in range(len(d))]for i in range (len(d[0]))]
        #Forcibly converting the values to float
        my_msg.data=d
        pub.publish(my_msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
