import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class InfoScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        self.mac_address = controller.mac_address                                  
        super().__init__(parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=3)
        self.rowconfigure(1,weight=18)
        # self.rowconfigure(1,weight=4)
        # self.rowconfigure(2,weight=5)
        # self.rowconfigure(3,weight=4)
        # self.rowconfigure(4,weight=5)
        
        
        status_part = tk.Frame(self, bg='black')
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        status_part.rowconfigure(0, weight=1)
        status_part.columnconfigure(0, weight=1)
        status_part.columnconfigure(1, weight=10)
        status_part.columnconfigure(2, weight=1)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=0,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        self.get_image(back_button_part, "img/parts/back_button.png", 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='BACK', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        # 나중에 정리....
        def back_click(event):
            show_home()
        back_label.bind("<Button-1>", back_click)
        

        value_part = Frame(self, bg='black')
        value_part.grid(row=1, column=0, sticky='NEWS')
        value_part.rowconfigure(0, weight=4)
        value_part.rowconfigure(1, weight=5)    
        value_part.rowconfigure(2, weight=4)
        value_part.rowconfigure(3, weight=5)

        ## value_part
        device_number_label = Label(value_part, text='Device Number', font=('Arial',30), fg='white', bg='black')
        device_number_label.grid(row=0, column=0,padx=20)
        
        device_number_value_label = Label(value_part, text=controller.device_number, font=('Arial',25), fg='white', bg='black')
        device_number_value_label.grid(row=1, column=0, padx=50)
        
        mac_address_label = Label(value_part, text='Mac Address', font=('Arial',30), fg='white', bg='black')
        mac_address_label.grid(row=2, column=0,padx=20)
        
        mac_address_value_label = Label(value_part, text=self.mac_address, font=('Arial',25), fg='white', bg='black')
        mac_address_value_label.grid(row=3, column=0, padx=50)

        
        
        
        
    def get_image(self, frame, path, width, height, row, column,sticky, command=None):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)


        