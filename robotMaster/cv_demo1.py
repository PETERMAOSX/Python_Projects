import cv2
import numpy as np
from robomaster import robot
 
def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """
 
    b_channel, g_channel, r_channel = cv2.split(img) # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 # 创建Alpha通道
 
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel)) # 融合通道
    return img_new
 
def merge_img(jpg_img, png_img, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加 
        y1,y2,x1,x2为叠加位置坐标值
    """
    
    # 判断jpg图像是否已经为4通道
    if jpg_img.shape[2] == 3:
        jpg_img = add_alpha_channel(jpg_img)
    
    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = png_img.shape[0]
    xx1 = 0
    xx2 = png_img.shape[1]
 
    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > jpg_img.shape[1]:
        xx2 = png_img.shape[1] - (x2 - jpg_img.shape[1])
        x2 = jpg_img.shape[1]
    if y2 > jpg_img.shape[0]:
        yy2 = png_img.shape[0] - (y2 - jpg_img.shape[0])
        y2 = jpg_img.shape[0]
 
    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_img[yy1:yy2,xx1:xx2,3] / 255.0
    alpha_jpg = 1 - alpha_png
    
    # 开始叠加
    for c in range(0,3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg*jpg_img[y1:y2,x1:x2,c]) + (alpha_png*png_img[yy1:yy2,xx1:xx2,c]))
 
    return jpg_img

ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_camera = ep_robot.camera
ep_camera.start_video_stream(display=False)

while True:
    img_jpg = ep_camera.read_cv2_image()
    img_jpg = cv2.resize(img_jpg, (1920,1080), interpolation=cv2.INTER_CUBIC)
    img_png = cv2.imread('./yidong111.png', cv2.IMREAD_UNCHANGED)
    
    res = cv2.addWeighted(img_jpg,0.5,img_png,0.5,0)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
    # cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
    cv2.imshow("frame", res)
    c = cv2.waitKey(1)
    if c == ord('q'):
        break
cv2.destroyAllWindows()

'''
    # 定义图像路径
    img_jpg_path = './jpg11.jpg' # 读者可自行修改文件路径
    img_png_path = './yidong111.png' # 读者可自行修改文件路径
 
    # 读取图像
    img_jpg = cv2.imread(img_jpg_path, cv2.IMREAD_UNCHANGED)
    img_png = cv2.imread(img_png_path, cv2.IMREAD_UNCHANGED)
 
    # 设置叠加位置坐标
    x1 = 0
    y1 = 0
    x2 = x1 + img_png.shape[1]
    y2 = y1 + img_png.shape[0]
 
    # 开始叠加
    res_img = merge_img(img_jpg, img_png, y1, y2, x1, x2)
    cv2.namedWindow('result', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('result', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # 显示结果图像
    cv2.imshow('result', res_img)
 
    # 保存结果图像，读者可自行修改文件路径
    cv2.imwrite('./res.jpg', res_img)
 
    # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

'''

'''

import cv2
from robomaster import robot



ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_camera = ep_robot.camera

# 显示200帧图传
ep_camera.start_video_stream(display=False)
while True:
    img = ep_camera.read_cv2_image()
    cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
    cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
    cv2.imshow("frame", img)
    c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
    if c == ord('q'):
        break
cv2.destroyAllWindows()
ep_camera.stop_video_stream()

ep_robot.close()


'''