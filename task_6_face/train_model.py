import cv2
import os
import numpy as np
from os import listdir
from os.path import isfile, join

# train the model
# path of the images 
data_path = 'C:/Users/Asus/Documents/summer_training/cv/CNN/users/train_img/'

faces=[]
faceID=[]
    
for path,subdirnames,filenames in os.walk(data_path):
    for filename in filenames:
        if filename.startswith("."):
            print("this file is not used by the model")
            continue
        id=os.path.basename(path)
        img_path=os.path.join(path,filename)
        print ("img_path",img_path)
        print("id: ",id)
        test_img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
        if test_img is None:
            print ("Not used ")
            continue
                
        faces.append(test_img)
        faceID.append(int(id)) 
# create the model using LBPH and train the model.       
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces,np.array(faceID))
print("Model is trained successfully.. ")
face_recognizer.save('C:/Users/Asus/Documents/summer_training/cv/task_6_face/trained_model.xml')
