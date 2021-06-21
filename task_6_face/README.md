### Face Recognition Model
1. Create the database using your face.
2. Train the model
3. Predict using the trained model.
4. Classify the users and then ,if User Acome in front of camera, send the gmail with face picture and if User B will come, it launch the EC2 instance and create a EBS volume and attach to it. 

## This is a face detection program using Haarcascade model.

Using this, we can create multiple faces model and then classify the faces.(This will tell you this is User A and this is user B) 

## Requirements
Install the libraries that are required:
i.) opencv-contrib-python

## Steps to Use
1. Create the database with the User's face.
----------------------------------------------
Run the create_db.py and look in front of your camera.
To save the file in a folder, first create the folder and inside the folder Create folders like 0,1,2,.. to store the user wise data. For e.g. ('C:/Users/Asus/Documents/summer_training/cv/CNN/users/train_img/0/') for User A and for more users , change the folder name 0 to 1 , and so on.

2. Train the model
-------------------
To train the model, first give the data_path in train_model.py file.
Here, you have to provide the path of folder till train_img only. It will automatically go through all the folders in train_img and train the model.
After trained, give the path to save the model. For e.g. 'C:/Users/Asus/Documents/summer_training/cv/task_6_face/trained_model.xml'.

3. Load the model and Predict the image 
-----------------------------------------
In my case, it will predict the face and perform some extra activites also. If you don't need these, you can comment these lines of code.

NOTE:--

In final_face_recog.py file:
For One user, name={0:"Lalit"} use only this, and for two users,  name={0:"Lalit" , 1:"Pawan"}, and so on.

Give the path of your saved model, by which it can load the model and predict.
After predicting the face, you can apply conditions and perform other actions also.
Here I am sending whatsapp message to my friend , Using SMTP protocol, it will send the mail and also mail the image of mine.

In my system, there is already configure the aws cli. So it will create the instance and EBS volume and then attach also.
To configure the aws, use "aws configure" command .



