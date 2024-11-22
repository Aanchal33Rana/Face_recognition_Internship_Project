import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

Ruchika_image = face_recognition.load_image_file("Ruchika.jpeg")
Ruchika_encoding = face_recognition.face_encodings(Ruchika_image)[0]


Anish_image = face_recognition.load_image_file("Anish.jpeg")
Anish_encoding = face_recognition.face_encodings(Anish_image)[0]


#aanchal_image = face_recognition.load_image_file("aanchal.png")
#aanchal_encoding = face_recognition.face_encodings(aanchal_image)[0]


Hardik_image = face_recognition.load_image_file("Hardik.jpeg")
Hardik_encoding = face_recognition.face_encodings(Hardik_image)[0]


known_face_encoding = [
Ruchika_encoding,
Anish_encoding,
#aanchal_encoding,
Hardik_encoding,

]

known_face_name = [
    "Ruchika",
    "Anish",
    "Aanchal",
    "Hardik"
    
]

students = known_face_name.copy()

face_locations =[]
face_encodings =[]
face_names =[]
s = True

now =datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+',newline='')
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_name[best_match_index]

            face_names.append(name)
            if name in known_face_name:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time,current_date])
                    f.flush()
                    print(f"Written {name}, {current_time} to file.")
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()