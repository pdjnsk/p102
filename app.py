import pyttsx3

speaker = pyttsx3.init()

f = input("enter the path of the file ")

with open(f, 'r') as a:
    data = a.read()

print(data)
speaker.say(data)
speaker.runAndWait()