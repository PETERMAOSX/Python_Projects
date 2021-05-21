import robomaster
from robomaster import robot
robomaster.config.LOCAL_IP_STR = "192.168.1.122"
er_robot = robot.Robot()
er_robot.initialize(conn_type="sta")
robomaster.config.DEFAULT_CONN_TYPE = "sta"
robomaster.config.DEFAULT_PROTO_TYPE = "tcp"
