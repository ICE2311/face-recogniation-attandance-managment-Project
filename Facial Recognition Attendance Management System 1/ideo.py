import cv2 as cv

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while cap.isOpened():

    _, img = cap.read()

    gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()