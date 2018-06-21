import cv2
import os
import dlib
import numpy as np
from multiprocessing import Pool

def get_face_rect(image):
    face_detector = dlib.get_frontal_face_detector()
    face_Rects = face_detector(image, 0)
    return face_Rects

def crop_face_from_image(image):
    faces_folder_path = '/home/beriani/Desktop/pictures/faces'

    image_name = image.split('.')[0]
    image_type = image.split('.')[1]
    
    image_path = os.path.join(images_folder_path, image)
    image = cv2.imread(image_path)
    face_rects = get_face_rect(image)

    for i in range(0,len(face_rects)):
        
        left = int(face_rects[i].left())
        right = int(face_rects[i].right())
        top = int(face_rects[i].top())
        bottom = int(face_rects[i].bottom())
        face = image[ top - int((bottom-top)/1.5) : bottom + int((bottom-top)/3) , left-int((right-left)/4) :right+int((right-left)/4) ]
        path = os.path.join(faces_folder_path,  "{}face{}.{}".format(image_name, i, image_type) )
        cv2.imwrite(path, face)
        print(path)

if __name__ == '__main__':
    images_folder_path = '/home/beriani/Desktop/facial_landmark_data/datasets/helen/testset'
    images = os.listdir(images_folder_path)
    images = [x for x in images if x.endswith('.jpg') and not 'mirror' in x]
    pool = Pool()
    pool.map(crop_face_from_image, images)