import cv2
import sys

drawing = False
complete_region = False
ix,iy,width,height = -1,-1,0,0
 
def my_mouse_callback(event,x,y,flags,param):
    global ix,iy,width,height,drawing,complete_region
 
    if event == cv2.EVENT_MOUSEMOVE:      # mouse move
        if(drawing == True):
            width = x - ix
            height = y - iy
 
    elif event == cv2.EVENT_LBUTTONDOWN:  # left_button push
        drawing = True
 
        ix = x
        iy = y
        width = 0
        height = 0
 
    elif event == cv2.EVENT_LBUTTONUP:    # left_button release
        drawing = False
        complete_region = True
 
        if(width < 0):
            ix += width
            width *= -1
        if(height < 0):
           iy += height
           height *= -1

cap = cv2.VideoCapture(sys.argv[1])
ret, img = cap.read()       # get first frame
temp = img.copy()           

source_window = "draw_rectangle"
cv2.namedWindow(source_window)
cv2.setMouseCallback(source_window, my_mouse_callback)

while(1):
    cv2.imshow(source_window,temp)

    if(drawing):            
        temp = img.copy()   
        cv2.rectangle(temp,(ix,iy),(ix + width, iy+ height),(0,255,0),2)  

    if(complete_region):    
        complete_region = False

        print('xmin:%d'%ix)
        print('ymin:%d'%iy)
        print('width:%d'%width)
        print('height:%d'%height)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:             
        break

cap.release()
cv2.destroyAllWindows()