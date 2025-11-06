import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class PicoReaderNode(Node):
    def __init__(self):
        super().__init__('pico_reader_node')
        self.publisher_ = self.create_publisher(String, 'pico/status', 10)

        try:
            self.ser = serial.Serial('/dev/back_pico', 115200, timeout=1)
            self.get_logger().info("Serial connection established with /dev/back_pico")
        except Exception as e:
            self.get_logger().error(f"Failed to open port: {e}")
            exit(1)

        self.timer = self.create_timer(0.1, self.read_serial)

    def read_serial(self):
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line:
                    msg = String()
                    msg.data = line
                    self.publisher_.publish(msg)
            except Exception as e:
                self.get_logger().warn(f"Error reading serial data: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = PicoReaderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
