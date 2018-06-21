import cv2
import numpy as np 
import dlib

image = cv2.imread('/home/beriani/Desktop/pictures/be.jpg')
height, width, channels = image.shape

face_detector = dlib.get_frontal_face_detector()
face_rects = face_detector(image, 0)


white = [255,255,255]

left = int(face_rects[0].left())
right = int(face_rects[0].right())
top = int(face_rects[0].top())
bottom = int(face_rects[0].bottom())

# top =  top - int((bottom-top)/1.5)
# bottom =  bottom + int((bottom-top)/3)
# right = right+int((right-left)/4)
# left = left-int((right-left)/4)

background = cv2.imread('/home/beriani/Desktop/pictures/background.jpeg')
background = cv2.resize(background, (width, height))


for x in range(0, height):

    for y in range(0, width):
        if y > right or y < left or x < top or x > bottom :
            image[x,y] = background[x,y]

cv2.imshow("transparent", image)
cv2.waitKey(0)
cv2.destroyAllWindows()