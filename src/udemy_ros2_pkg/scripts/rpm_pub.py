#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32, Bool

RPM = 10

class RpmPublisher(Node): 
	def __init__(self):
		super().__init__("rpm_pub_node")
		self.pub = self.create_publisher(Float32, "rpm", 10)
		self.timer = self.create_timer(0.5, self.publish_rpm)

	def publish_rpm(self):
		msg = Float32()
		msg.data = float(RPM)
		self.pub.publish(msg)

def main(args=None):
	rclpy.init()
	my_pub = RpmPublisher()
	print("RPM Publisher Node Running...")

	try:
		rclpy.spin(my_pub)
	except KeyboardInterrupt:
		print("Terminating Node...")
		my_pub.destroy_node()

if __name__ == '__main__': 
	main()
	

