import cv2 as cv
import numpy as np


cap = cv.VideoCapture('images/vtest.avi')
# cap = cv.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # only get the motion of objects
    diff = cv.absdiff(frame1, frame2)

    # convert to gray scale
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    # remove noise
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    # create binary threashold
    _, th = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    # dilate to fill small holes
    dilate = cv.dilate(th, None, iterations=3)

    # find contours from the image
    cont, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw raw contours
    # cv.drawContours(frame1, cont, -1, (0, 0, 255), 2)


    for c in cont:
        # get dimension for the contoure
        (x, y, w, h) = cv.boundingRect(c)

        # draw rectangle if area is above threashold
        if cv.contourArea(c) < 1000:
            continue

        # draw rectangle
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # put text if there is movement
        cv.putText(frame1, "Status: ()".format('Movement'), (10, 20),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv.imshow("video", frame1)

    # re-read frame
    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
cap.release()
