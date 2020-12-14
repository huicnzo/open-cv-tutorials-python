import cv2

cap = cv2.VideoCapture(0) # 0 device index if it doesn't work try -1

# creating a while loop in order to capture a frame continuously

while(True):
	ret , frame = cap.read() #read method will return true if frame is available otherwise it will be false
    
	cv2.imshow('frame',frame) # the yellw color frame here is the name given to the variable frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() #after reading ur video we need to releae
cap.destroyAllWindows



##for gray color##
import cv2

cap = cv2.VideoCapture(0) # 0 device index if it doesn't work try -1

# creating a while loop in order to capture a frame continuously

while(True):
	ret , frame = cap.read() #read method will return true if frame is available otherwise it will be false
    
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #method to convert color
	cv2.imshow('frame',gray) # the yellw color frame here is the name given to the variable frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() #after reading ur video we need to releae
cap.destroyAllWindows



##accesing video from a file ##

import cv2

cap = cv2.VideoCapture(0) # inplace of zero write here the filename & format of the video .

# creating a while loop in order to capture a frame continuously
print(cap.isOpened())
while(cap.isOpened()):
	ret , frame = cap.read() #read method will return true if frame is available otherwise it will be false
    
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #method to convert color
	cv2.imshow('frame',gray) # the yellw color frame here is the name given to the variable frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() #after reading ur video we need to releae
cap.destroyAllWindows


## width & height of the frame & OTHER  PROPERTIES (brightness , saturation ) ##

import cv2

cap = cv2.VideoCapture(0) # 0 device index if it doesn't work try -1

# creating a while loop in order to capture a frame continuously

while(True):
	ret , frame = cap.read() #read method will return true if frame is available otherwise it will be false
    
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #method to convert color
	cv2.imshow('frame',gray) # the yellw color frame here is the name given to the variable frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() #after reading ur video we need to release
cap.destroyAllWindows

## how to save video ##

import cv2

cap = cv2.VideoCapture(0) # 0 device index if it doesn't work try -1
      #we used he class VideoCapture for capturing the video
      #we will use  class VideoWriter to save the video
# creating a while loop in order to capture a frame continuously
out = cv2.videoWriter('output.avi')
while(True):
	ret , frame = cap.read() #read method will return true if frame is available otherwise it will be false
    
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #method to convert color
	cv2.imshow('frame',gray) # the yellw color frame here is the name given to the variable frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() #after reading ur video we need to releae
cap.destroyAllWindows


## saving video using four cc code ##

import cv2

cap = cv2.VideoCapture(0) # 0 device index if it doesn't work try -1
      #we used he class VideoCapture for capturing the video
      #we will use  class VideoWriter to save the video
# creating a while loop in order to capture a frame continuously
out = cv2.videoWriter('output.avi')
while(True):
	if ret , frame = cap.read() #read method will return true if frame is available otherwise it will be false
    	out.write(frame)

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #method to convert color
	cv2.imshow('frame',gray) # the yellw color frame here is the name given to the variable frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() #after reading ur video we need to releae
out.release()
cap.destroyAllWindows

