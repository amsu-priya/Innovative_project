import cv2
import winsound

img=cv2.imread('ip1.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img_gray)

inv_img=cv2.bitwise_not(img_gray)   #invert b&w colors
cv2.imwrite('ip3.jpg',inv_img)
cv2.imshow("inverted",inv_img)

res,thresh_img=cv2.threshold(inv_img,202,255,cv2.THRESH_BINARY_INV) #202 manual t value 255 is when value is less than thresh
cv2.imwrite('ip2.jpg',thresh_img)
cv2.imshow("threshold",thresh_img)

thresh_img=255- thresh_img

contours,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im2=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

sum1=0
for c in contours:
    area=cv2.contourArea(c)
    if area>4:
        #print (area)
        sum1+=1
print("no of threads",sum1)


if(sum1==30):
    print("No fault is detected")
else:
    print("Fault detected")
    winsound.Beep(440, 500)    
    winsound.Beep(440, 500)
    winsound.Beep(440, 500)
