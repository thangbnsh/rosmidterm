#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
import time  # Thêm thư viện để theo dõi thời gian

last_log_time = 0  # Lưu thời gian log lần trước
log_interval = 1.0  # Giảm log xuống 1 lần mỗi giây

def imu_callback(data):
    global last_log_time
    current_time = time.time()
    
    # Chỉ log nếu đã qua ít nhất `log_interval` giây
    if current_time - last_log_time >= log_interval:
        rospy.loginfo(f"Orientation: x={data.orientation.x}, y={data.orientation.y}, z={data.orientation.z}, w={data.orientation.w}")
        rospy.loginfo(f"Angular Velocity: x={data.angular_velocity.x}, y={data.angular_velocity.y}, z={data.angular_velocity.z}")
        rospy.loginfo(f"Linear Acceleration: x={data.linear_acceleration.x}, y={data.linear_acceleration.y}, z={data.linear_acceleration.z}")
        rospy.loginfo("----")
        last_log_time = current_time  # Cập nhật thời gian log gần nhất

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)
    rospy.Subscriber("/imu/data", Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    imu_listener()

