#!/usr/bin/env python3

import rospy
import sys, select, termios, tty
from std_msgs.msg import Float64

msg = """
Điều khiển tay máy:

    Nhấn 'w' để tăng khau1_link_joint
    Nhấn 's' để giảm khau1_link_joint
    Nhấn 'a' để tăng khau2_link_joint
    Nhấn 'd' để giảm khau2_link_joint
    Nhấn 'q' để thoát

"""

# Mức điều chỉnh góc mỗi lần nhấn phím (radians)
step_size = 0.1

# Giá trị ban đầu của các joint
khau1_angle = 0.0
khau2_angle = 0.0

def get_key():
    """Đọc phím từ terminal"""
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def teleop_control():
    global khau1_angle, khau2_angle

    rospy.init_node('arm_teleop')
    khau1_pub = rospy.Publisher('/khau1_controller/command', Float64, queue_size=10)
    khau2_pub = rospy.Publisher('/khau2_controller/command', Float64, queue_size=10)
    rospy.sleep(1)

    print(msg)

    while not rospy.is_shutdown():
        key = get_key()

        if key == 'w':
            khau1_angle += step_size
        elif key == 's':
            khau1_angle -= step_size
        elif key == 'a':
            khau2_angle += step_size
        elif key == 'd':
            khau2_angle -= step_size
        elif key == 'q':
            print("\nThoát teleop!")
            break

        rospy.loginfo(f"Khớp 1: {khau1_angle}, Khớp 2: {khau2_angle}")
        khau1_pub.publish(khau1_angle)
        khau2_pub.publish(khau2_angle)

    rospy.signal_shutdown("Tắt teleop")

if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)
    try:
        teleop_control()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

