import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from scipy.misc import face

cap = cv2.VideoCapture(0)

# define our face detector
detector = FaceMeshDetector(maxFaces=1)

while True:
   success, img = cap.read()
   img, faces = detector.findFaceMesh(img)
   
   if faces:
      face = faces[0]
      # find distance between right-left eyes
      pointLeft = face[145]
      pointRight = face[374]
      
      #cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
      #cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
      #cv2.line(img, pointLeft, pointRight, (255, 0, 0), 3)
      
      w,_ = detector.findDistance(pointLeft, pointRight)
      W = 6.3
      
      # finding distance
      f = 840
      d = (W*f)/w - 15
      print(d)
      
      cv2.putText(img, "Distance:  " + str(int(d)) + " cm", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)
      
   cv2.imshow("Video", img)
   cv2.waitKey(1)
