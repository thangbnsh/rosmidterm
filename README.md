# ROS MID TERM
## Hướng dẫn mô phỏng và điều khiển Robot
### 1. Sau khi gitclone về máy tính ta sẽ biên dịch lại package và source lại không gian làm việc

```bash
cd ~/catkin_ws/src
```

```bash
catkin_make
```
```bash
source devel/setup.bash
```
### 2. Chạy file launch để chạy Gazebo và Rviz

```bash
roslaunch tn13 rosmidterm.launch
```


### GAZEBO
![gazebo](https://raw.githubusercontent.com/thangbnsh/rosmidterm/9e3c17dba61e0b1e119516485661065a6e830d86/launch/gazebo.png)

### RVIZ
![Rviz](https://raw.githubusercontent.com/thangbnsh/rosmidterm/9e3c17dba61e0b1e119516485661065a6e830d86/launch/rviz.png)

### 3. Thêm vật cản trong gazebo
![Screenshot from 2025-03-31 12-37-38](https://raw.githubusercontent.com/thangbnsh/rosmidterm/9e3c17dba61e0b1e119516485661065a6e830d86/launch/themvatcan.png)


### 4. Điều khiển robot và tay máy


Điều khiển xe di chuyển bằng bàn phím
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```


Điều khiển tay máy bằng bàn phím
```bash
roslaunch tn13 tn13_control.launch.launch
```
```bash
rosrun tn13 control_arm.py
```
![Screenshot from 2025-03-31 12-40-21](https://raw.githubusercontent.com/thangbnsh/rosmidterm/9e3c17dba61e0b1e119516485661065a6e830d86/launch/taymay.png)

Đọc dữ liệu từ imu_reader
```bash
rosrun tn13 imu_reader.py
```
### KẾT QUẢ 
### Hiển thị robot trên Gazebo Rviz, điều khiển tay máy và robot di chuyển thành công. Lấy dữ liệu từ 3 cảm biến
![Screenshot from 2025-03-31 17-51-00](https://raw.githubusercontent.com/thangbnsh/rosmidterm/9e3c17dba61e0b1e119516485661065a6e830d86/launch/ketqua1.png)

![Screenshot from 2025-03-31 17-50-38](https://raw.githubusercontent.com/thangbnsh/rosmidterm/9e3c17dba61e0b1e119516485661065a6e830d86/launch/ketqua2.png)



