# Description: A simple text-to-speech program using the pyttsx3 library. (For Windows)
# Requirements: Install the pyttsx3 library using pip.
# Created by Bhuvan Patil

import pyttsx3

print(
    "=======:[Welcome to Text to Speech Program]:=======")
print("NOTE: Type ':q' to quit the program.")
while True:
    text = input("Enter what you want to speak: ")
    if text == ':q':
        print("Exiting the program...")
        machine = pyttsx3.init()
        machine.say(
            "Thank you for using the Text to Speech Program. Have a good day!")
        machine.runAndWait()
        break
    machine = pyttsx3.init()
    machine.say(text)
    machine.runAndWait()
