import cv2
import numpy as np
f = open('D:/MEMOIRE MASTER/database/HAMMOUTI_DATASET/char.txt', "r", encoding='utf8')
# read image
for line in f:
    lineSplit = line.strip().split(' ')
    img = cv2.imread('D:/MEMOIRE MASTER/database/HAMMOUTI_DATASET/chars/' + lineSplit[0] + '.bmp')
    #print(lineSplit[0])
    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray,(5,5),0)
    # threshold
    ret, thresh1 = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 8) 
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                cv2.CHAIN_APPROX_NONE)
    # get contours
    result = img.copy()
    
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print(lineSplit[0],'ok 154','0','0',w,h,',')

    
        
  # show thresh and result    
cv2.imshow("bounding_box", result)
cv2.waitKey(0)
cv2.destroyAllWindows()



