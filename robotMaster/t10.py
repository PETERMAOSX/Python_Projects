from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_servo = ep_robot.servo

    # 舵机3 转到0度
    ep_servo.moveto(index=3, angle=90).wait_for_completed()

    ep_robot.close()