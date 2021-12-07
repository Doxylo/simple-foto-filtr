import cv2 
from PIL import Image, ImageDraw

# img = cv2.imread('test.jpg')
# main_img = Image.open('test.jpg')
# gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)

# faces = cv2.CascadeClassifier('faces.xml')

# results = faces.detectMultiScale(gray, 1.1, 11)


pudge = cv2.imread('pudjik2.jpg', 0)

weigth = int(pudge.shape[1])
height = int(pudge.shape[0])
dim = (weigth, height)

# # cv2.imshow("Result", main_img)
# # cv2.waitKey(0)

print(weigth, height)

img = cv2.imread('Kass.jpg')

FACE_DETECTOR_PATH='faces.xml'

def crop_face(img, scaleFactor=1.001, face_detector_path=FACE_DETECTOR_PATH):
    face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,  1.1, 11)
    for (x,y,w,h) in faces:
        #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        return roi_color

cropped = crop_face(img, scaleFactor=1.01)
weight = int(cropped.shape[1])
heigth = int(cropped.shape[0])
# cv2.imshow('1', cropped)
# cv2.waitKey()
 


