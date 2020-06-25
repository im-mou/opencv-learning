import cv2 as cv
import datetime

cap = cv.VideoCapture(0)

print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 512)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 512)
height = str(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = str(cap.get(cv.CAP_PROP_FRAME_WIDTH))
font = cv.FONT_HERSHEY_SIMPLEX

text = height + 'x' + width


while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        date = str(datetime.datetime.now())
        frame = cv.putText(frame, text + ' ' + date, (10, 40), font, 0.5, (0 ,255, 255), 1, cv.LINE_AA)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv.destroyAllWindows()
