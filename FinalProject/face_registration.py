import cv2
import face_recognition
import pickle
from datetime import datetime

#Create an instance of the VideoCapture class
cap = cv2.VideoCapture(0)

#set the image width and height
width, height = 320, 240

#set the format of the captured image
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#Create a face detector using the haar cascade classifier
face_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')

#Prompt the user to enter the name for the registered face
name = input("Enter your name: ")

#Prompt the user to enter the room access (comma-separated)
access_input =("Enter room access (comma-separated): ")
access_list = access_input.split(',')

#Initialize an empty list to store the face data
face_data = []

#Counter for the number of face captures
capture_count = 0

while True:
	#Capture frame-by-frame
	ret, frame = cap.read()

	#Convert the frame grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#Detect faces in the frame 
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

	#Draw rectangles around the detected faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 225, 0), 2)

		#Encode the face region of interest (ROI),  using face recognition
		rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BRG2RGB)
		face_encodings = face_recognition.face_encodings(rgb_frame, [(y, x+w, y+h, x)])

		
		for face_encoding in face_encodings:
			face_data.append({"name": name, "face": frame[y:y+h, x:x+w], "face_encoding": face_encoding, "access": access_list})

	#Display the frame
	cv2.imshow('Register Face', frame)

	if cv2.waitKey(1) & 0xFF == ord('s'):
		capture_count += 1
		print(f"Capture {capture_count}  complete!")
	if capture_count >= 5:
		break
cap.release()
cv2.destroyAllWindows()

now = datetime.now()
file_name = f"faces/{now/.strftime('%Y-%m-%d-%H-%M-%s')}-{name}.pickle"
with open(file_name, 'wb') as f:
	pickle.dump(face_data, f)
print(f"Face data for '{name}' saved successfully!")




	

		


	


