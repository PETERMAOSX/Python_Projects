def windows_split(x,y):
    if (x > 0 and y >0) and (x < 640 and y < 310):
        print("1")
    elif (x > 640 and y > 0) and (x < 1280 and y < 310):
        print("2")
    elif (x > 1280 and y > 0) and (x < 1920 and y < 310):
        print("3")
    elif (x > 0 and y > 310) and (x < 640 and y < 620):
        print("4")
    elif (x > 640 and y > 310) and (x < 1280 and y < 620):
        print("5")
    elif (x > 1280 and y > 310) and (x < 1920 and y < 620):
        print("6")
    elif (x > 0 and y > 620) and (x < 640 and y < 930):
        print("7")
    elif (x > 640 and y > 620) and (x < 1280 and y < 930):
        print("8")
    elif (x > 1280 and y > 620) and (x < 1920 and y < 930):
        print("9")
    elif (x > 0 and y > 930) and (x <640 and y < 1080):
        print("10")
    elif (x > 640 and y > 930) and (x < 1280 and y < 1080):
        print("11")
    elif (x > 1280 and y > 930) and (x < 1920 and y < 1080):
        print("12")