import cv2
import numpy as np
import winsound

"""import os
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from twilio.rest import Client
client = Client(account_sid, auth_token)"""


cap = cv2.VideoCapture('input.mp4')  #including input

while True:
  success, image = cap.read() #reading nd storing in image
  if success:
    imgContour = image.copy()  #loading image in newname
    imgcrop=image[0:100,250:560]  #fixing into size
    cropCopy=imgcrop.copy() #loading in new name
    
    imgGray=cv2.cvtColor(imgcrop,cv2.COLOR_BGR2GRAY)  #greyconversion
    imgBlur=cv2.GaussianBlur(imgGray,(7,7),1) #applying gb(low pass filter removes high freq ie.noise)
    imgCanny=cv2.Canny(imgBlur,50,100)  #applying canny(detects edges and shoes sharp intensity )
    contours, _ =cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #retrieval,approximate none because we need all points simple used to have specific points

    for cnt in contours:
        area=cv2.contourArea(cnt) #area
        print("area",area)
        if area>2000:
            peri=cv2.arcLength(cnt,True)  #perimeter
            print("perimeter",peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True) #approximation Douglas-Peucker algorithm
            points=len(approx)  #points
            print("points",points)
            x,y,w,h=cv2.boundingRect(approx)  #to have boundaries in op
            if points>4:
                name="circle"
                cv2.rectangle(cropCopy,(x,y),(x+w,y+h),(0,255,0),1) 
                cv2.putText(cropCopy,"circle",(x,y+60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
                cv2.rectangle(image,(0,220),(856,300),(0,0,255),cv2.FILLED)
                cv2.putText(image,"FAULTY ITEM DETECTED",(90,280),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)
                #print('\a')
                winsound.Beep(440, 500)
                #winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
                """message = client.messages \
                  .create(
                   body='Hello there from Twilio SMS API',
                   from_ =  FROM_N,
                   to = TO_NUMBER
                   )    
                print(message.sid)"""
                
            else:   #less than or equals 4
                cv2.rectangle(cropCopy,(x,y),(x+w,y+h),(0,255,0),1)
                cv2.putText(cropCopy,"Rectangle",(x,y+40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
                
    #cv2.imshow("gray",imgGray)
    cv2.imshow("threshold",imgCanny)
    cv2.imshow("result",image)
    cv2.imshow("crop",cropCopy)
    
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
  else:
      break
