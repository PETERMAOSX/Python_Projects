import cv2
from robomaster import robot



ep_robot = robot.Robot()
ep_robot.initialize(conn_type="sta")

ep_camera = ep_robot.camera

ptStart_1 = (0, 206)
ptEnd_1 = (1280, 206)

ptStart_2 = (0, 412)
ptEnd_2 = (1280, 412)

ptStart_3 = (0, 620)
ptEnd_3 = (1280, 620)

ptStart_4 = (426, 0)
ptEnd_4 = (426, 720)

ptStart_5 = (853, 0)
ptEnd_5 = (853, 720)

point_color = (0, 255, 0) # BGR
thickness = 2
lineType = 4

#----------------------------
text = 'Move Mode'
org = (120, 670)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontcolor = (0, 255, 0) # BGR
thickness = 1 
lineType = 4
bottomLeftOrigin = 1

text2 = "Catch Mode"
org2 = (973,670)
# cv.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType, bottomLeftOrigin)





# 显示200帧图传
ep_camera.start_video_stream(display=False)
while True:
    img = ep_camera.read_cv2_image()
    # img = cv2.resize(img, (1920,1080), interpolation=cv2.INTER_CUBIC)
    cv2.line(img, ptStart_1, ptEnd_1, point_color, thickness, lineType)
    cv2.line(img, ptStart_2, ptEnd_2, point_color, thickness, lineType)
    cv2.line(img, ptStart_3, ptEnd_3, point_color, thickness, lineType)
    cv2.line(img, ptStart_4, ptEnd_4, point_color, thickness, lineType)
    cv2.line(img, ptStart_5, ptEnd_5, point_color, thickness, lineType)
    cv2.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)
    cv2.putText(img, text2, org2, fontFace, fontScale, fontcolor, thickness, lineType)
    print(img.shape)
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
    cv2.resizeWindow("frame", 1920, 1080)    # 设置长和宽
    cv2.imshow("frame", img)
    c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
    if c == ord('q'):
        break
cv2.destroyAllWindows()
ep_camera.stop_video_stream()

ep_robot.close()