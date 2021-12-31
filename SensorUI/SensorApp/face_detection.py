import numpy as np
import cv2
import imutils
from PIL import Image
import os
import pickle

faceDetector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    og_label = pickle.load(f)
    label = {v:k for k,v in og_label.items()}

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret,image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
        for (x,y,w,h) in faces:
            id_, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf >=45:
                #print(id_)
                #print(label[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = label[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(image, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        eyes = eyeDetector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
        for (x,y,w,h) in eyes:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        ret,jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()