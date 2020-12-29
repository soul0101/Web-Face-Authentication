import face_recognition
import imutils
import pickle
import time
import cv2
import os

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt2.xml')
data = pickle.loads(open("face_enc","rb").read())

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
hiegh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(gray,1.1,5,minSize=(60, 60),flags=cv2.CASCADE_SCALE_IMAGE)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],encoding)     

        name = "Unknown"
        if True in matches:
            matchIndx = [i for (i , b) in enumerate(matches) if b]
            counts = {}
            for i in matchIndx:
                name = data["name"][i]
                counts[name] = counts.get(name,0)+1
            name = max(counts , key = counts.get)    
        
        names.append(name)      

    for((x , y , w , h) , name) in zip(face , names):
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
        frame = cv2.rectangle(frame,(x,y+h),(x+w,y+h+35),(0,255,0),cv2.FILLED)
        frame = cv2.putText(frame, name.upper(), (x+6, y+h+28), cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 255, 255), 2) 
       
    cv2.imshow("live capture",frame)

    key=cv2.waitKey(1)

    if(key==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
