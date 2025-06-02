import cv2
import numpy as np
import face_recognition
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
bhuvan_img = face_recognition.load_image_file("face_images/bhuvan.jpg")
bhuvan_face_encoding = face_recognition.face_encodings(bhuvan_img)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [bhuvan_face_encoding]
known_face_names = ["Bhuvan"]

students = known_face_names.copy()

# Initialize empty lists to store attendance data
face_locations = []
face_encodings = []

#Get current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"Attendance_System/stud_{current_date}.csv", "w+", newline="")
writer = csv.writer(f)
writer.writerow(["Name", "Time"])

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize the frame to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (OpenCV uses BGR) to RGB color
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # If the name is not already in the list, add it to the attendance
        if name in students:
            students.remove(name)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            writer.writerow([name, current_time])
            print(f"Attendance marked for {name} at {current_time}")

    # Display the results
    cv2.imshow('Attendance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break