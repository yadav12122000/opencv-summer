#test the model

import smtplib
import pywhatkit

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from datetime import date
from datetime import datetime
now = datetime.now()
today = date.today()
import pywhatkit

def send_whatsapp_msg():
    current_time = now.strftime("%H:%M:%S")
    hr,mnt,sec = current_time.split(":")

    wh = pywhatkit.pywhatkit
    wh.sendwhatmsg('+91 1234567890' , "🤩🤩👍 Hey, I am Lalit", int(hr) , int(mnt)+2 )



email_user='your_email@gmail.com'
email_send='other_person@gmail.com'
email_user_pass='your_email_password'

def securityMail():
    
    subject= '⚠ Security Alert!! ⚠'
    
    msg=MIMEMultipart()
    msg['From']=email_user
    msg['To']=email_send
    msg['Subject']=subject

    dtime= now.strftime("%H:%M:%S")
    ddate=today.strftime("%B %d, %Y")

    body = '''
⚠ Login Alert ⚠
I have logged in...
During:-
Date: '''+ddate+'''
Time: '''+dtime+'''
Front face in jpg format:
'''

    msg.attach(MIMEText(body,'plain'))

    filename="Lalit.jpg"
    attachment =open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename="+filename)

    msg.attach(part)
    text= msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user, email_user_pass)

    server.sendmail(email_user,email_send,text)
    server.quit()
    return("mail is sended")
# load the model and predict

import cv2
import numpy as np
import os , time
import subprocess as sp


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


# Open Webcam
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("http://192.168.43.1:8080/video")
name={0:"Lalit" , 1:"Pawan"}
while True:

    ret, frame = cap.read()

    
    image, face = face_detector(frame)
    image = cv2.resize(image, (1200,900))
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        face_recognizer=cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('C:/Users/Asus/Documents/summer_training/cv/task_6_face/trained_model.xml')
        results = face_recognizer.predict(face)
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
            cv2.putText(image, display_string, (220,200), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
            cv2.imshow('Face Recognition' , image)
        if confidence > 88:
            predicted_name=name[results[0]]
            cv2.putText(image, predicted_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            if (results[0]==0):
                print(f"hii {predicted_name}")
                cv2.imwrite(f"{predicted_name}.jpg" , image)
                cv2.destroyAllWindows()
                securityMail()
                send_whatsapp_msg()
                break
            if results[0]==1:
                print(f"hii {predicted_name}")
                cv2.destroyAllWindows()
                ins = sp.getoutput('aws ec2 run-instances --image-id ami-06a0b4e3b7eb7a300 --instance-type t2.micro --key-name firstkey --subnet-id subnet-e8c2cb80  --security-group-ids  sg-043a35ed45e0208d6  --count 1 --query Instances[0].InstanceId')
                vol = sp.getoutput('aws ec2 create-volume   --volume-type gp2   --size 5   --availability-zone ap-south-1a --query VolumeId ' )
                time.sleep(20)
                print(sp.getoutput(f'aws ec2 attach-volume --volume-id {vol} --instance-id {ins} --device /dev/xvdf'))
                break
         
        else:
            cv2.putText(image, "I dont know, who r u", (250,650), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
    
    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()