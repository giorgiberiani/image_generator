import cv2
import os
import random
import dlib
import numpy as np

def get_background_images(fiels_path):
        
    files = os.listdir(fiels_path)
    background_image_paths = []
    for file in files:
        images_path = os.path.join(fiels_path,file)
        
        images = os.listdir(images_path)
        
        images = [x for x in images if x.endswith('.jpg')]
        for image in images:
            image_path = os.path.join(images_path, image)
            background_image_paths.append(image_path)
    return background_image_paths

def get_images(path):
    image_paths = []
    images = os.listdir(path)
    for image in images:
        if image.endswith('.png'):
            image = os.path.join(path,image)
            image_paths.append(image)
    return image_paths
    


def alfa_blending(background_image, foreground_image):
    background_image = cv2.resize(background_image, (foreground_image.shape[1], foreground_image.shape[0]))

    b,g,r,a = cv2.split(foreground_image)

    foreground_image = cv2.merge((b,g,r))

    alpha = cv2.merge((a,a,a))

    foreground_image = cv2.merge((b,g,r))

    alpha = cv2.merge((a,a,a))

    foreground_image = foreground_image.astype(float)
    background_image = background_image.astype(float)
    alpha = alpha.astype(float)/255

    foreground_image = cv2.multiply(alpha, foreground_image)
    background_image = cv2.multiply(1.0 - alpha, background_image)
    out_image = cv2.add(foreground_image, background_image)

    return cv2.add(foreground_image, background_image)

def get_face_rect(image):
    face_detector = dlib.get_frontal_face_detector()
    face_rect = face_detector(image, 0)
    return face_rect


def generate_image(face, hand, background):

    background_image = cv2.imread(background)

    face_img = cv2.imread(face, -1)
    hand_img= cv2.imread(hand, -1)
    grayscale_face = cv2.imread(face, 0)

    out_img = alfa_blending(background_image, face_img)
    face_rect = get_face_rect(grayscale_face)[0]

    face_haight = face_rect.right() - face_rect.left()
    top = face_rect.top()
    bottom = face_rect.bottom()
    right = face_rect.right()
    left = face_rect.left()

    hand_img = cv2.resize(hand_img,(face_haight, face_haight),) 
    print(face_rect)
    print('top :{}  bottom :{} rig :{} lef :{}'.format(top, bottom, right, left))
    x_offset = random.randint(top, bottom)
    y_offset = random.randint(left, right)

    y1, y2 = y_offset, y_offset + hand_img.shape[0]
    x1, x2 = x_offset, x_offset + hand_img.shape[1]

    alpha_hand = hand_img[:, :, 3] / 255.0
    alpha_face = 1.0 - alpha_hand

    for c in range(0, 3):
        out_img[y1:y2, x1:x2, c] = (alpha_hand * hand_img[:, :, c] + alpha_face * out_img[y1:y2, x1:x2, c])
                
    cv2.imwrite('/home/beriani/Desktop/pictures/non_nude/face{}.png'.format(i), out_img)
    print(i)

if __name__ == '__main__': erti saati asi lari naxevari saati ormocdaaati lari

    background_images_path = '/home/beriani/Desktop/dtd-r1.0.1/dtd/images'
    face_images_path = '/home/beriani/Desktop/pictures/faces'
    hands_images_path = '/home/beriani/Desktop/pictures/hands'
    hands = get_images(hands_images_path)
    faces = get_images(face_images_path)
    backgrounds = get_background_images(background_images_path)

    for i in range(10):
        face_index = random.randint(0, len(faces) - 1)
        hand_index = random.randint(0, len(hands) - 1)
        background_index = random.randint(0, len(backgrounds) - 1)

        face = faces[face_index]
        hand = hands[hand_index]
        background = backgrounds[background_index]

        generate_image(face, hand, background)
