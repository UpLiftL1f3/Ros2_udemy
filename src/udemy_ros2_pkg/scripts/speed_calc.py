#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32, Bool

WHEEL_RADIUS_DEFAULT = 12.5 / 100 # CENTIMETERS TO METERS

class SpeedCalculator(Node):
    def __init__(self):
        super().__init__("speed_calc_node")
        self.declare_parameter("wheel_radius", WHEEL_RADIUS_DEFAULT)
        self.sub = self.create_subscription(Float32, "rpm", self.calculate_speed, 10)
        self.pub = self.create_publisher(Float32, "speed", 10)
        print(self.get_parameter("wheel_radius").get_parameter_value())
        
    def calculate_speed(self, rpm_msg):
        # calc speed
        wheel_radius_param = self.get_parameter("wheel_radius").get_parameter_value().double_value
        speed = rpm_msg.data * wheel_radius_param * 2 * 3.14159 / 60 # speed per second (/60 turns rotations per minute aka rpm into per second)

        # publish calculated speed
        speed_msg = Float32()
        speed_msg.data = float(speed)
        self.pub.publish(speed_msg)

def main(args = None):
    rclpy.init()
    speed_calc_node = SpeedCalculator()
    print("Speed calculator node running...")

    try:
        rclpy.spin(speed_calc_node)
    except KeyboardInterrupt:
        print("Terminating...")
        speed_calc_node.destroy_node()

if __name__ == '__main__':
    main()
