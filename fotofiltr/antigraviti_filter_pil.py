import tkinter
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from PIL import Image, ImageDraw, ImageTk
import tkinter.filedialog as fd
import random
import cv2

FACE_DETECTOR_PATH='faces.xml'
def crop_face(main_img, scaleFactor=1.001, face_detector_path=FACE_DETECTOR_PATH):
    face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,  1.1, 11)
    for (x,y,w,h) in faces:
        roi_color = main_img[y:y+h, x:x+w]
        return roi_color

def choose_file():
    filetypes = (("Изображение", "*.jpg *.gif *.png"), 
                ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        file = filename
    return file

def obr_ser_stile():
    image = Image.open(choose_file())
    draw = ImageDraw.Draw(image)
    wigth = image.size[0]
    heigth = image.size[1]
    pix = image.load()
    for x in range(wigth):
        for y in range(heigth):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            s = (r + g + b) // 3
            draw.point((x, y), (s, s, s))
    image.save("new_style.jpg", "JPEG")
    return image.show()

def obr_negative():
    image = Image.open(choose_file())
    draw = ImageDraw.Draw(image)
    wigth = image.size[0]
    heigth = image.size[1]
    pix = image.load()
    for x in range(wigth):
        for y in range(heigth):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (255-r, 255-g, 255-b))
    image.save("new_style.jpg", "JPEG")
    return image.show()

def obr_bw():
    image = Image.open(choose_file())
    draw = ImageDraw.Draw(image)
    wigth = image.size[0]
    heigth = image.size[1]
    pix = image.load()
    for x in range(wigth):
        for y in range(heigth):
            r = pix[x, y][0]
            g = pix[x, y][1] 
            b = pix[x, y][2] 
            n = r + g + b 
            if n > (255 // 2 * 3):
                r = 255
                g = 255 
                b = 255
            else:
                r = 0
                g = 0
                b = 0

            draw.point((x, y), (r, g, b))
    image.save("new_style.jpg", "JPEG")
    return image.show()

def obr_noise():
    image = Image.open(choose_file())
    draw = ImageDraw.Draw(image)
    wigth = image.size[0]
    heigth = image.size[1]
    pix = image.load()
    choise = spinbox_noise.get()
    for x in range(wigth):
        for y in range(heigth):
            randomi = random.randint(-int(choise), int(choise))
            r = pix[x, y][0] + randomi 
            g = pix[x, y][1] + randomi 
            b = pix[x, y][2] + randomi 
            if r < 0:
                r = 0 
            if g < 0:
                g = 0
            if b < 0:
                b = 0 
            if r > 255:
                r = 255 
            if g > 255:
                g = 255  
            if b > 255:
                b = 255
            draw.point((x, y), (r, g, b))
    image.save("new_style.jpg", "JPEG")
    return image.show()

def obr_sepia():
    image = Image.open(choose_file())
    draw = ImageDraw.Draw(image)
    wigth = image.size[0]
    heigth = image.size[1]
    pix = image.load()
    user = spinbox_sepia.get()
    for x in range(wigth):
        for y in range(heigth):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            R = ((r + g + b) // 3) + int(user) * 2
            G = ((r + g + b) // 3) + int(user) 
            B = (r + g + b) // 3
            draw.point((x, y), (R, G, B))
    image.save("new_style.jpg", "JPEG")
    return image.show()

def obr_brightness():
    image = Image.open(choose_file())
    draw = ImageDraw.Draw(image)
    wigth = image.size[0]
    heigth = image.size[1]
    pix = image.load()
    choise = spinbox_brightness.get()
    for x in range(wigth):
        for y in range(heigth):
            r = pix[x, y][0] + int(choise)
            g = pix[x, y][1] + int(choise) 
            b = pix[x, y][2] + int(choise)
            if r < 0:
                r = 0 
            if g < 0:
                g = 0
            if b < 0:
                b = 0 
            if r > 255:
                r = 255 
            if g > 255:
                g = 255  
            if b > 255:
                b = 255
            draw.point((x, y), (r, g, b))
    image.save("new_style.jpg", "JPEG")
    return image.show()

def upgrade_photo():
    main_img = cv2.imread(choose_file())
    face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,  1.1, 11)

    for (x,y,w,h) in faces:
        xx = x 
        yy = y

    pudge = cv2.imread('pudjik2.jpg')

    cropped = crop_face(main_img, scaleFactor=1.01)
    weigth_main_img = int(cropped.shape[1])
    height_main_img = int(cropped.shape[0])

    points_pudge = (weigth_main_img , height_main_img)
    resize_pudge = cv2.resize(pudge, points_pudge, interpolation = cv2.INTER_LINEAR)

    main_img_pil = cv2.imwrite('image-2.jpg', main_img)
    pudge_pil = cv2.imwrite('image-1.jpg', resize_pudge)

    cordix = xx 
    cordiy = yy

    mmain_image = Image.open('image-2.jpg')
    rresize_pudge = Image.open('image-1.jpg')
    mmain_image.paste(rresize_pudge, (int(cordix), int(cordiy)))

    mmain_image.save("pp.jpg")
    return mmain_image.show()
    

root = Tk()


root.title("Фотофильтр")
root.geometry('600x450')
root.config(bg="#F5CFBA")

space = Label(root, text='')
space.pack()
space.config(bg="#F5CFBA")

label = Label(root, text='Привет', font=("Arial", 15), bg = '#F5CFBA', fg='#647575')
label.pack()

space1 = Label(root, text='')
space1.pack()
space1.config(bg="#F5CFBA")

btn_ser = tk.Button(text="Выбрать файл и обработать  в сером стиле", command=obr_ser_stile, bg = '#F1F5D3', fg='#647575')
btn_ser.pack()

space2 = Label(root, text='')
space2.pack()
space2.config(bg="#F5CFBA")

btn_negative = tk.Button(text="Выбрать файл и обработать в стиле негатив", command=obr_negative, bg = '#F1F5D3', fg='#647575')
btn_negative.pack()

space3 = Label(root, text='')
space3.pack()
space3.config(bg="#F5CFBA")

btn_bw = tk.Button(text="Выбрать файл и обработать в черно белый", command=obr_bw, bg = '#F1F5D3', fg='#647575')
btn_bw.pack()

space4 = Label(root, text='')
space4.pack()
space4.config(bg="#F5CFBA")

spinbox_noise = tk.Spinbox(from_=0, to= 100, bg = '#F1F5D3', fg='#647575')
spinbox_noise.pack()
btn_noise = tk.Button(text="Выбрать файл и обработать c шумами", command=obr_noise, bg = '#F1F5D3', fg='#647575')
btn_noise.pack()

space5 = Label(root, text='')
space5.pack()
space5.config(bg="#F5CFBA")

spinbox_sepia = tk.Spinbox(from_=0, to= 100, bg = '#F1F5D3', fg='#647575')
spinbox_sepia.pack()

btn_sepia = tk.Button(text="Выбрать файл и обработать в стиле сепия", command=obr_sepia, bg = '#F1F5D3', fg='#647575')
btn_sepia.pack()

space6 = Label(root, text='')
space6.pack()
space6.config(bg="#F5CFBA")

spinbox_brightness = tk.Spinbox(from_=-100, to= 100, bg = '#F1F5D3', fg='#647575')
spinbox_brightness.pack()
btn_brightness = tk.Button(text="Выбрать файл и настроить яркость", command=obr_brightness, bg = '#F1F5D3', fg='#647575')
btn_brightness.pack()

space7 = Label(root, text='')
space7.pack()
space7.config(bg="#F5CFBA")

btn_up = tk.Button(text="Улучшить фотографию", command=upgrade_photo, bg = '#F1F5D3', fg='#647575')
btn_up.pack()

root.mainloop()





