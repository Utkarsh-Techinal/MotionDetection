from firebase import firebase
from google.cloud import storage
import os
from picamera import PiCamera
from time import sleep



camera = PiCamera()
camera.start_preview()
sleep(2)

#where you want to save the image
camera.capture('/home/pi/firebaseTesting/Test.jpg')
camera.stop_preview()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/firebaseTesting/Motion Dection-c6785d268c68.json"
#Real time Database Link
firebase = firebase.FirebaseApplication('https://motion-dection-3e190.firebaseio.com/')
client = storage.Client()
#Storage Database Link
bucket = client.get_bucket('motion-dection-3e190.appspot.com') 
# posting to firebase storage
imageBlob = bucket.blob("/")
# imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
imagePath = "/home/pi/firebaseTesting/Test.jpg"
#where your image is saved
imageBlob = bucket.blob("Test.jpg")
#the name you want to save your image as on firebase
imageBlob.upload_from_filename(imagePath)

