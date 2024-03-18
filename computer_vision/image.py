#image loading
import cv2
import numpy as np

path ='computer_vision/cat.jpg'
img = cv2.imread(path)
print(img.size,img.shape)

#image modification
#rotate


img_r=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#manual resize

img_rz_1=cv2.resize(img,(300,300))
#fraction resize
img_rz_2=cv2.resize(img,(0,0),fx=.5,fy=.5)

cv2.imshow('image',img)
cv2.imshow('image_r',img)
cv2.imshow('image_resized_1',img_rz_1)
cv2.imshow('image_resized_2',img_rz_2)
cv2.waitKey(0)