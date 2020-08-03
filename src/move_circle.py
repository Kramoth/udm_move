#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np

class circle:
	def __init__(self):
		rospy.init_node('circle',anonymous=True)
		self.pub=rospy.Publisher('circlePose',PoseStamped,queue_size=10)
		self.rate=rospy.Rate(5)
		self.radius=float(rospy.get_param("~radius", "0"))
		self.speed=float(rospy.get_param("~speed","1"))
		print("radius : %f"%(self.radius))
		print("speed : %f"%(self.speed))

	def run(self):
		circlePose=PoseStamped() 
		theta=0      
		while not rospy.is_shutdown():
			theta=theta+self.speed
			circlePose.header.stamp=rospy.Time.now()
			circlePose.header.frame_id='map'
			circlePose.pose.position.x=self.radius*np.cos(theta)
			circlePose.pose.position.y=self.radius*np.sin(theta)
			circlePose.pose.orientation.w=1
			self.pub.publish(circlePose)
			self.rate.sleep()

if __name__ == '__main__':
	try:
		node=circle()
		node.run()
	except rospy.ROSInterruptException:
		pass