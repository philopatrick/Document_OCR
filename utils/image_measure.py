import cv2


## change the image path here
image = cv2.imread('./asset/Inkedres_front.jpg')


def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),10,(255,0,0),-1)
        cv2.putText(image, f"x:{x} y:{y}", (x,y), cv2.FONT_HERSHEY_DUPLEX, fontScale = 1, color = (125, 246, 55), thickness = 3)
        mouseX,mouseY = x,y
        print(f"x:{x} y:{y}")



cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('original',draw_circle)


while(1):
    cv2.imshow('original',image)
    k = cv2.waitKey(20) & 0xFF
    if k == 27: #press ESC to quit
        break
    
