from robomaster import robot


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta")

    ep_sensor_adaptor = ep_robot.sensor_adaptor

    # 获取传感器转接板adc值
    adc = ep_sensor_adaptor.get_adc(id=1, port=1)
    print("sensor adapter id1-port1 adc is {0}".format(adc))

    # 获取传感器转接板io电平
    io = ep_sensor_adaptor.get_io(id=1, port=1)
    print("sensor adapter id1-port1 io is {0}".format(io))

    # 获取传感器转接板io电平持续时间
    duration = ep_sensor_adaptor.get_pulse_period(id=1, port=1)
    print("sensor adapter id1-port1 duration is {0}ms".format(duration))

    ep_robot.close()