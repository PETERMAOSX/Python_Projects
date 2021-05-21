import time
import robomaster
from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_gripper = ep_robot.gripper
    
    # 张开机械爪
    ep_gripper.open(power=50)
    time.sleep(1)
    ep_gripper.pause()

    # 闭合机械爪
    ep_gripper.close(power=50)
    time.sleep(1)
    ep_gripper.pause()

    ep_robot.close()