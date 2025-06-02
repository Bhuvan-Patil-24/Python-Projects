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