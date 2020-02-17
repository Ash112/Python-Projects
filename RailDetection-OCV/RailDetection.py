import cv2
import numpy


def roi(img, vertices):
    #blank mask:
    mask = numpy.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


vertices = numpy.array([[460,720],[900,720],[800,350],[500,350]], numpy.int32)

vid = cv2.VideoCapture('C:\\Users\\PJZ\\Downloads\\Railcap.mp4')

while True:

    ret,frame = vid.read()
    roi_frame = roi(frame, [vertices])


    hsv = cv2.cvtColor(roi_frame,cv2.COLOR_RGB2HSV)




    lower_green = numpy.array([0, 52, 25])
    upper_green = numpy.array([100, 255, 85])


    mask = cv2.inRange(hsv, lower_green, upper_green)

    blurredmask = cv2.GaussianBlur(mask,(1,1),0)

    edges = cv2.Canny(blurredmask,10,25)



    #lines = cv2.HoughLinesP(edges, 1 , numpy.pi/180, 50, maxLineGap=15)

    fet,contour,fet = cv2.findContours(blurredmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for conts in contour:

        area = cv2.contourArea(conts)

        if area >=4000:

            drawcont = cv2.drawContours(frame, contour, -1, (0, 0, 255), 1)


    #drawcont = cv2.drawContours(frame,contour,-1,(0,0,255),1)

    #if lines is not None:
        #for line in lines:

            #x1,y1,x2,y2 = line[0]
            #cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),1)

    cv2.imshow("frame", frame)

    key =cv2.waitKey(50)

    if key ==27:

        break

vid.release()

# Closes all the frames
cv2.destroyAllWindows()