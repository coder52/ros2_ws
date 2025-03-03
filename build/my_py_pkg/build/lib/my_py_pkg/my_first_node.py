#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        self.counter_ = 0
        # init the node and give it to name
        super().__init__("py_test")
        # print somethink 
        self.get_logger().info("Hello world!")

    # if you print every second an info
        # make a timer (it runs callback function on spin command)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    # initialize ros2  cominication
    rclpy.init(args=args)  

    # Make the node
    # node = Node("py_test")
    # node.get_logger().info("Hello world!")
    # if you don't want to oop, comment next line and uncommnet 
    # before two lines
    node = MyNode()

    # spin stops the execution but node alive 
    # and allow to execution to callback
    # that means every second writes "Hello" on the screen
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()