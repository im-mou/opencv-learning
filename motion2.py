import cv2 as cv


def cb(e):
    pass

cv.namedWindow('track')
cv.createTrackbar('t1', 'track', 90, 255, cb)
cv.createTrackbar('t2', 'track', 255, 255, cb)
cv.createTrackbar('area', 'track', 500, 1500, cb)


cap = cv.VideoCapture('images/vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    gauss = cv.GaussianBlur(gray, (5, 5), 0)

    th1 = cv.getTrackbarPos('t1', 'track')
    th2 = cv.getTrackbarPos('t2', 'track')


    _, thr = cv.threshold(gauss, th1, th2, cv.THRESH_BINARY)
    dilate = cv.morphologyEx(thr, cv.MORPH_OPEN, (5, 5))

    cont, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # cv.drawContours(frame1, cont, -1, (0, 0, 255), 2)

    area = cv.getTrackbarPos('area', 'track')

    for c in cont:
        (x, y, w, h) = cv.boundingRect(c)
        if cv.contourArea(c) < area:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('image', diff)

    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
