import cv2

import numpy as np

vid = cv2.imread('C:\\Users\\PJZ\\Downloads\\43.png')



grey = cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey,100,0.5,10)

corners=np.int0(corners)

for corner in corners:

    x, y = corner.ravel()
    cv2.circle(vid,(x,y),3,(0,0,255),-1)

cv2.imshow("vid",vid)

cv2.waitKey(0)


cv2.destroyAllWindows()