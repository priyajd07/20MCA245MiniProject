import keras
import cv2
from keras.models import model_from_json
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
from src.dbconnection import *
model = model_from_json(open(r"model/facial_expression_model_structure.json", "r").read())
model.load_weights(r'model/facial_expression_model_weights.h5')  # load weights



face_cascade = cv2.CascadeClassifier(r'model/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

def camclick():
    i=0
    while(True):
        ret, img = cap.read()

        # img = cv2.imread('../11.jpg')
        # cv2.imwrite(str(i)+".jpg",img)
        i=i+1

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #print(faces) #locations of detected faces
        emotion=None

        emotionlist=[]

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image

            detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
            detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48

            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis = 0)

            img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

            predictions = model.predict(img_pixels) #store probabilities of 7 expressions

            #find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
            max_index = np.argmax(predictions[0])

            emotion = emotions[max_index]
            cv2.putText(img,emotion,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

            emotionlist.append(emotion)

            # if cv2.waitKey(1):
        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
            break
        # 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'
        if 'angry' in emotionlist or 'disgust' in emotionlist or 'sad' in emotionlist or 'fear' in emotionlist or 'happy' in emotionlist:
            import datetime
            fn=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
            cv2.imwrite("static/noti/"+fn,img)
            qry="INSERT INTO `camnoti` VALUES(NULL,1,%s,NOW(),'pending')"
            val=(fn)
            iud(qry,val)
        # kill open cv things
    cap.release()
    cv2.destroyAllWindows()
            # 	pass
        # return emotion
            #write emotion text above rectangle

camclick()
