from customtkinter import *
from PIL import Image
window = CTk() #создание окна
window.title("Чатик 1.1") #изменение названия
window.geometry("1080x500") #изменение размера
window.configure(fg_color ="purple") #изменение цвета заднего фона .configure может изменять все и как угодно
frame = CTkFrame(window,fg_color="white",width = 500, height= 400)
frame.place(x =0,y = 0)
enter_text = "Введіть текст"
enter = CTkEntry(window,width=410,height=90,placeholder_text=enter_text)
enter.place(x = 0, y = 400)
btn = CTkButton(window, width=90,height=90,hover_color="red", font = ("Arial", 30 , "bold") ) #создание кнопки
btn.place(x = 400,y=400)
picture_ctk = Image.open("pixil-frame-0.png")
picture_ctk = CTkImage(light_image=picture_ctk,size = (100,100))
btn.configure(image = picture_ctk,compound = "right",text = "Send" )



window.mainloop()