#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
import numpy as np

class teleop_move:
	def __init__(self):
		rospy.init_node('circle',anonymous=True)
		self.pub=rospy.Publisher('teleopPose',PoseStamped,queue_size=10)
		self.rate=rospy.Rate(5)
		self.cmd=Twist()
		self.teleopPose=PoseStamped()
		self.teleopPose.pose.orientation.w=1

		rospy.Subscriber("cmd",Twist,self.sub_callBack)

	def sub_callBack(self, data):
		new_x=self.teleopPose.pose.position.x+data.linear.x
		new_y=self.teleopPose.pose.position.y+data.linear.y

		if -5<=new_x<=5:
			self.teleopPose.pose.position.x=new_x
		if -5<=new_y<=5:
			self.teleopPose.pose.position.y=new_y
		
	def run(self):   
		while not rospy.is_shutdown():
			self.teleopPose.header.stamp=rospy.Time.now()
			self.teleopPose.header.frame_id='map'
			self.pub.publish(self.teleopPose)
			self.rate.sleep()

if __name__ == '__main__':
	try:
		node=teleop_move()
		node.run()
	except rospy.ROSInterruptException:
		pass