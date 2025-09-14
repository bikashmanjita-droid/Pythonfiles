import cv2

camera = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")




while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),3)
        
    cropped_face = gray[y:y+h , x:x+w]
    roi_color =gray [y : y+h , x:x+w]
    eyes = eye_cascade.detectMultiScale(cropped_face, 1.1, 10)
    smile= face_cascade.detectMultiScale(cropped_face,1.1, 350)

   

    if len(eyes) > 0:
        cv2.putText(frame, "Eyes Detected",(x,y-35),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0), 2)
        with open ("eye.txt","w") as f:
            f.write(str(len(eyes)))
    if len(faces) >0 : 
        cv2.putText(frame, "Smile deteced",(x,y-10), cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)

    cv2.imshow("Detecting face...",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("commaded for exit ")
        break



    