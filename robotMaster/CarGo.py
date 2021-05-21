import time
import cv2
from robomaster import robot
import socket
import json
from multiprocessing import Process


class Car:
    def __init__(self,x_val,y_val,z_angel_val) -> None:
        self.x_val = x_val
        self.y_val = y_val
        self.z_angel_val = z_angel_val
        self.car = robot.Robot()
        self.car.initialize(conn_type='sta')
        self.car_transform = self.car.chassis
        self.car_camera = self.car.camera
        self.car_gripper = self.car.gripper
        self.car_servo = self.car.servo
        self.eye_x = 0
        self.eye_y = 0
        #self.show_camera()
    
    def show_camera(self):
        self.car_camera.start_video_stream(display=False)
        while True:
            img = self.car_camera.read_cv2_image()
            cv2.imshow("Robot", img)
            c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
            if c == ord('q'):
                break
        cv2.destroyAllWindows()
        self.car_camera.stop_video_stream()

    def run_forward(self):
        self.car_transform.drive_speed(x=self.x_val, y=0, z=0, timeout=5)
        
    
   

    def run_back(self):
        self.car_transform.drive_speed(x=-self.x_val,y=0,z=0,timeout=5)
        

    def run_left(self):
        self.car_transform.drive_speed(x=0,y=-self.y_val,timeout=5)
        

    def run_right(self):
        self.car_transform.drive_speed(x=0,y=self.y_val,timeout=5)
        

    def run_left_rotate(self):
        self.car_transform.drive_speed(x=0,y=0,z=-self.z_angel_val,timeout=0)
        
    
    def run_right_rotate(self):
        self.car_transform.drive_speed(x=0,y=0,z=self.z_angel_val,timeout=0)
    
    def run_left_rotate_back(self):
        self.car_transform.drive_speed(x=0,y=0,z=self.z_angel_val,timeout=0)
        
    
    def run_right_rotate_back(self):
        self.car_transform.drive_speed(x=0,y=0,z=-self.z_angel_val,timeout=0)
        
    def run_stop(self):
        self.car_transform.drive_speed(x=0, y=0, z=0, timeout=5)
    
    def open_gripper(self):
        self.car_gripper.open(power=50)
        
        self.car_gripper.pause()
    
    def close_gripper(self):
        self.car_gripper.close(power=50)
        
        self.car_gripper.pause()
    
    def windows_split(self,x,y):
        if (x > 0 and y >0) and (x < 640 and y < 310):
            return 1
        elif (x > 640 and y > 0) and (x < 1280 and y < 310):
            return 2
        elif (x > 1280 and y > 0) and (x < 1920 and y < 310):
            return 3
        elif (x > 0 and y > 310) and (x < 640 and y < 620):
            return 4
        elif (x > 640 and y > 310) and (x < 1280 and y < 620):
            return 5
        elif (x > 1280 and y > 310) and (x < 1920 and y < 620):
            return 6
        elif (x > 0 and y > 620) and (x < 640 and y < 930):
            return 7
        elif (x > 640 and y > 620) and (x < 1280 and y < 930):
            return 8
        elif (x > 1280 and y > 620) and (x < 1920 and y < 930):
            return 9
        elif (x > 0 and y > 930) and (x <640 and y < 1080):
            return 10
        elif (x > 640 and y > 930) and (x < 1280 and y < 1080):
            return 11
        elif (x > 1280 and y > 930) and (x < 1920 and y < 1080):
            return 12

    def get_eye_data(self):
        ip_port = ('127.0.0.1', 6555)
        s = socket.socket()     # 创建套接字
        s.connect(ip_port)      # 连接服务器
        count = 0
        while True:    
            s.sendall('values'.encode())
            server_reply = s.recv(8192).decode()
            server_reply = json.loads(server_reply)
            if server_reply["values"]["frame"]["avg"]["x"] == 0 or server_reply["values"]["frame"]["avg"]["y"] == 0:
                continue
            self.eye_x = server_reply["values"]["frame"]["avg"]["x"]
            self.eye_y = server_reply["values"]["frame"]["avg"]["y"]
            #print(self.eye_x)
            count += 1
            if count % 10 == 0:
                # if(self.eye_x < 1900 and self.eye_x > 1500):
                #     self.run_right_rotate()
                #     print("R")
                # elif(self.eye_x > 10 and self.eye_x < 500):
                #     self.run_left_rotate()
                #     print("L")
                # else:
                #     print('M')
                #     self.run_stop()
                if(self.windows_split(self.eye_x,self.eye_y) == 1):
                    self.run_left_rotate()
                elif(self.windows_split(self.eye_x,self.eye_y) == 2):
                    self.run_forward()
                elif(self.windows_split(self.eye_x,self.eye_y) == 3):
                    self.run_right_rotate()
                elif(self.windows_split(self.eye_x,self.eye_y) == 4):
                    self.run_left()
                elif(self.windows_split(self.eye_x,self.eye_y) == 5):
                    self.run_stop()
                elif(self.windows_split(self.eye_x,self.eye_y) == 6):
                    self.run_right()
                elif(self.windows_split(self.eye_x,self.eye_y) == 7):
                    self.run_left_rotate_back()
                elif(self.windows_split(self.eye_x,self.eye_y) == 8):
                    self.run_back()
                elif(self.windows_split(self.eye_x,self.eye_y) == 9):
                    self.run_right_rotate_back()
                elif(self.windows_split(self.eye_x,self.eye_y) == 10):
                    pass
                elif(self.windows_split(self.eye_x,self.eye_y) == 11):
                    pass
                elif(self.windows_split(self.eye_x,self.eye_y) == 12):
                    pass
                pass
                    
            elif count > 200:
                count = 0
            else:
                pass
            

if __name__ == "__main__":
    car_demo = Car(0.3,0.3,30)
    car_demo.get_eye_data()
 
    car_demo.car.close()

# ep_robot = robot.Robot()
# ep_robot.initialize(conn_type="sta")

# ep_chassis = ep_robot.chassis

# x_val = 1
# y_val = 0.2
# z_val = 180

# # 前进 3秒
# ep_chassis.drive_speed(x=x_val, y=0, z=0, timeout=5)
# time.sleep(2)

# # 后退 3秒
# ep_chassis.drive_speed(x=-x_val, y=0, z=0, timeout=5)
# time.sleep(2)

# # 左移 3秒
# ep_chassis.drive_speed(x=0, y=-y_val, z=0, timeout=5)
# time.sleep(2)

# # 右移 3秒
# ep_chassis.drive_speed(x=0, y=y_val, z=0, timeout=5)
# time.sleep(2)

# # 左转 3秒
# ep_chassis.drive_speed(x=0, y=0, z=-z_val, timeout=5)
# time.sleep(2)

# # 右转 3秒
# ep_chassis.drive_speed(x=0, y=0, z=z_val, timeout=5)
# time.sleep(2)

# # 停止麦轮运动
# ep_chassis.drive_speed(x=0, y=0, z=0, timeout=5)

# ep_robot.close()
