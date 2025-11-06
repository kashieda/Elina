# wheel_control_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class WheelControlNode(Node):
    def __init__(self):
        super().__init__('wheel_control_node')

        # Paramètres série
        self.serial_port = '/dev/back_pico'
        self.baud_rate = 115200
        self.ser = None

        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            self.get_logger().info(f"Serial connection of the backward OK on {self.serial_port}")
        except Exception as e:
            self.get_logger().error(f"Serial opening error : {e}")

        # Abonnement ROS
        self.subscription = self.create_subscription(
            String,
            'wheel_key_input',
            self.key_callback,
            10
        )

    def key_callback(self, msg):
        char = msg.data.rstrip('\n')
        if len(char) == 1 and (char.isprintable() or char == ' '):
            try:
                self.ser.write(char.encode('utf-8'))
                self.get_logger().info(f"Send to Pico : {char}")
            except Exception as e:
                self.get_logger().error(f"Serial send error : {e}")
        else:
            self.get_logger().warn(f"Ignored : '{char}'")

def main(args=None):
    rclpy.init(args=args)
    node = WheelControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
