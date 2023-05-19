import tkinter as tk
from tkinter import ttk
from sensor_list import SENSOR_DICT
from tkinter import *
from PIL import Image, ImageTk

class Element(ttk.Frame):
    def __init__(self,parent, controller, show_home, sensor):
        super().__init__(parent)
        self.controller = controller
        self.sensor_name = sensor


        self.columnconfigure(0, weight=1)
        
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=6)
        
        status_part = tk.Frame(self, bg="black")
        status_part.grid(row=0, column=0, sticky="NEWS")
        
        
        status_part.rowconfigure(0, weight=1)

        status_part.columnconfigure(0, weight=3)
        status_part.columnconfigure(1, weight=20)
        status_part.columnconfigure(2, weight=2)
        
        back_button_part = tk.Frame(status_part, bg='black')
        back_button_part.grid(row=0, column=0, sticky="NEWS", pady=10,ipadx=0, ipady=0)
        back_button_part.place(relx=0.1, rely=0.5, anchor='c')          # 안맞으면...그냥 해야함... 나도 이유 모름... 그냥.... 그냥 함...  아니면 골 때려짐
        back_button_part.rowconfigure(0, weight=1)
        back_button_part.columnconfigure(0, weight=1)
        back_button_part.columnconfigure(1, weight=1)
        back_button_part.bind("<Button-1>", show_home)
        
        # self.get_button(back_button_part, show_home, "img/parts/back_button.png", 25, 25,0, 0, 'NE')
        self.get_image(back_button_part, "img/parts/back_button.png", 30, 30,0, 0, 'E', command=show_home)
        back_label = Label(back_button_part, text='MAIN', font=('Arial', 30), fg='white', bg='black', pady=3)
        back_label.grid(row=0, column=1, sticky='NW')
        
        # 나중에 정리....
        def back_click(event):
            show_home()
        
        back_label.bind("<Button-1>", back_click)
        
        ###############################################################################################################
        # main frame
        
        main_part = tk.Frame(self, bg='red')
        main_part.grid(row=1, column=0, sticky='NEWS')
        main_part.columnconfigure(0, weight=1)
        main_part.rowconfigure(0, weight=4)
        main_part.rowconfigure(1, weight=5)
        
        ######################## 1 2 1 1 1 ########################
        
        ### Sensor Description Part
        sensor_description_part = tk.Frame(main_part, bg='green')
        sensor_description_part.grid(row=0, column=0, sticky='NEWS')
        sensor_description_part.columnconfigure(0, weight=2)
        sensor_description_part.columnconfigure(1, weight=9)
        sensor_description_part.rowconfigure(0, weight=1)
        sensor_description_part.rowconfigure(1, weight=2)
        
        
        ###########################################################################
        ######################## 이미지 변경을 위해 고쳐야함 ########################
        ###########################################################################
        image_path = 'img/sensor/' + self.sensor_name + '.png'
        # image_name = 'img/sensor/' + controller.sensor_name + '.png'
        # self.get_image(sensor_description_part, image_name, 80, 80, 0, 0, 'NEWS', rowspan=2)
        sensor_img = Image.open(image_path)
        resized_img = sensor_img.resize((70, 70), Image.ANTIALIAS)
        sensor_image = ImageTk.PhotoImage(resized_img)
        self.img_label = Label(sensor_description_part, image=sensor_image, bg='green')
        self.img_label.image = sensor_image
        self.img_label.grid(row=0, column=0, rowspan=2, sticky='NEWS')
        

        # 1 - Sensor name
        title = Label(sensor_description_part, bg='red', text='TVOC!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        title.grid(row=0, column=1, sticky='NEWS')
        
        # 2 - Sensor description
        img = Label(sensor_description_part, bg='yellow', text='description!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        img.grid(row=1, column=1, sticky='NEWS')
        
        
        
        
        ### Sensor Gauge & Range Part
        sensor_value_part = tk.Frame(main_part, bg='black')
        sensor_value_part.grid(row=1, column=0, sticky='NEWS')
        sensor_value_part.columnconfigure(0,weight=1)
        sensor_value_part.rowconfigure(0,weight=3)
        sensor_value_part.rowconfigure(1,weight=4)
        sensor_value_part.rowconfigure(2,weight=3)
        # 1 - Sensor value
        value = Label(sensor_value_part, bg='orange', text='52g/m^3')
        value.grid(row=0, column=0, sticky='W')
        # 1 - Sensor gauge
        self.get_image(sensor_value_part, 'img/gauge/gage-12.png',700,50,row=1,column=0, sticky='NEWS')
        # gauge = Label(sensor_value_part, bg='magenta')
        # gauge.grid(row=1, column=0, sticky='NEWS')
        # 1 - Sensor range
        range = Label(sensor_value_part, bg='cyan')
        range.grid(row=2, column=0, sticky='NEWS')
        
        
        
        
        
        
        
    def get_image(self, frame, path, width, height, row, column,sticky, command=None,rowspan=1):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Label(frame, image=photo_img, bg='black')
        img_label.image = photo_img
        img_label.grid(row=row, column=column, rowspan=rowspan, sticky=sticky)
        def local_click(event):
            command()
        img_label.bind("<Button-1>", local_click)

    def get_button(self, frame,command, path, width, height, row, column,sticky):
        img = Image.open(path)
        resized_img = img.resize((width,height), Image.ANTIALIAS)
        photo_img = ImageTk.PhotoImage(resized_img)
        img_label = Button(frame, image=photo_img, bg='black', command=command,bd=0)        # bd = border
        img_label.image = photo_img
        img_label.grid(row=row, column=column, sticky=sticky)
        
        
        
        
        
        
        
    


    def change_image(self,sensor_name):
        img = PhotoImage(file=SENSOR_DICT[sensor_name][1])
        self.img_label.configure(image=img)
        self.img_label.image = img
        