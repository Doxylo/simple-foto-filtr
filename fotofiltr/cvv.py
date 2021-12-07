import cv2 
from PIL import Image, ImageDraw

FACE_DETECTOR_PATH='faces.xml'
def crop_face(main_img, scaleFactor=1.001, face_detector_path=FACE_DETECTOR_PATH):
    face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,  1.3, 11)
    for (x,y,w,h) in faces:
        roi_color = main_img[y:y+h, x:x+w]
        return roi_color

main_img = cv2.imread('rere.jpg')

face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,  1.3, 11)
for i in range(1, len(faces)+1):
    main_img = cv2.imread('rere.jpg')
    for (x,y,w,h) in faces:
        xx = x 
        yy = y

        pudge = cv2.imread('pudjik2.jpg')
        weigth = pudge.shape[1]
        height = pudge.shape[0] 

        cropped = crop_face(main_img, scaleFactor=1.01)
        weigth_main_img = int(cropped.shape[1])
        height_main_img = int(cropped.shape[0])

        points_pudge = (weigth_main_img , height_main_img)
        resize_pudge = cv2.resize(pudge, points_pudge, interpolation = cv2.INTER_LINEAR)
        weigth_resize = resize_pudge.shape[1]
        height_resize = resize_pudge.shape[0]

        main_img_pil = cv2.imwrite('image-2.jpg', main_img)
        pudge_pil = cv2.imwrite('image-1.jpg', resize_pudge)

        cordix = xx 
        cordiy = yy

        mmain_image = Image.open('image-2.jpg')
        rresize_pudge = Image.open('image-1.jpg')
        mmain_image.paste(rresize_pudge, (int(cordix), int(cordiy)))

        mmain_image.save("rere.jpg")



mmain_image.show()
cv2.waitKey()