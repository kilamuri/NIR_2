from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import easygui
import cv2
import numpy as np 

def open_img(path_img):
    pil_img = Image.open(path_img)
    width, height = pil_img.size
    new_height  = 550 
    new_width = int(new_height * width / height)

    pil_img = pil_img.resize((new_width, new_height))
    test = ImageTk.PhotoImage(pil_img)
    panel = Label(root, image = test)
    panel.image = test
    panel.place(x = 25, y = 25)
    
def open_file():
    global file_path
    file_path = easygui.fileopenbox(filetypes=["*.jpg", "*.png", "*.gif", "*.jpeg", "*.bmp"])
    open_img(file_path)

def eye_detect():
    path = "haarcascade_eye.xml"
    eyeCascade = cv2.CascadeClassifier(path)

    img = cv2.imread(file_path)
    # в случае кириллицы не открывается файл - декодируем его
    if (img is None):
        img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frame = img

    eyes = eyeCascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))

    for (x, y, w, h) in eyes:
        frame[y+10:y+h-10, x:x+w, 0] = np.random.normal(size=(h-20, w))
        frame[y+10:y+h-10, x:x+w, 1] = np.random.normal(size=(h-20, w))
        frame[y+10:y+h-10, x:x+w, 2] = np.random.normal(size=(h-20, w))

    cv2.imwrite("result.jpg", frame)
    open_img("result.jpg")

# дизайн формы
root = Tk()
root.title("Закраска глаз") 
root.geometry('800x600')

font_button = font.Font(size=14, weight="normal")

btn1 = Button(root, width = 20,text = "Открыть фотку", command = open_file, font = font_button)
btn2 = Button(root, width = 20,text = "Сделать хуету", command = eye_detect, font = font_button)
btn1.place(x = 500, y = 25)
btn2.place(x = 500, y = 80)

root.mainloop() 
