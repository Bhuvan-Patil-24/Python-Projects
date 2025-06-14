import cv2
import numpy as np
import face_recognition
import csv
from datetime import datetime
import os

# Make sure the video capture is available
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not open video capture device")
    exit()

# Load a sample picture and learn how to recognize it.
try:
    bhuvan_img = cv2.imread("face_images/debug_image.jpg")
    # bhuvan_img = bhuvan_img.astype(np.uint8)
    # cv2.imwrite("face_images/debug_image.jpg", cv2.cvtColor(bhuvan_img, cv2.COLOR_BGR2RGB))
    if bhuvan_img is None:
        raise Exception("Could not load image......")
    bhuvan_img = cv2.cvtColor(bhuvan_img, cv2.COLOR_BGR2RGB)
    bhuvan_face_encoding = face_recognition.face_encodings(bhuvan_img)[0]
except Exception as e:
    print(f"Error loading reference image: {e}")
    video_capture.release()
    exit()

# Create arrays of known face encodings and their names
known_face_encodings = [bhuvan_face_encoding]
known_face_names = ["Bhuvan"]

students = known_face_names.copy()

# Initialize empty lists to store attendance data
face_locations = []
face_encodings = []
name = "Unknown"  # Initialize name variable

# Get current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create attendance directory if it doesn't exist
attendance_dir = "Attendance_System"
os.makedirs(attendance_dir, exist_ok=True)

# Open CSV file with proper path
csv_path = os.path.join(attendance_dir, f"stud_{current_date}.csv")
f = open(csv_path, "w+", newline="")
writer = csv.writer(f)
writer.writerow(["Name", "Time"])

try:
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not read frame")
            break

        # Resize the frame to 1/4 size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color to RGB color
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Find all the faces and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            
            if len(face_distance) > 0:  # Check if any faces were found
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    # Display the name on the frame
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, 
                              f"{name} Present", 
                              (10, 100), 
                              font, 
                              1.5, 
                              (255, 0, 0), 
                              3, 
                              2)

                    # Mark attendance if not already marked
                    if name in students:
                        students.remove(name)
                        current_time = datetime.now().strftime("%H:%M:%S")
                        writer.writerow([name, current_time])
                        print(f"Attendance marked for {name} at {current_time}")

        # Display the results
        cv2.imshow('Attendance', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release handle to the webcam and cleanup
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()