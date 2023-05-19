import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class EthernetScreen(ttk.Frame):
    def __init__(self, parent, controller, show_home):
        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.columnconfigure(0, weight=1)
        status_part = tk.Frame(self, bg='black')
        status_part.grid(row=0, column=0, sticky='NEWS')

        self.connection_status = 'Auto'         # Auto & Manual <- default=Auto  ; 나중에 enum으로 고칠 예정
        
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
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

        main_part = Frame(self, bg='black')
        main_part.grid(row=1, column=0, sticky='NEWS')
        main_part.columnconfigure(0, weight=1)
        main_part.rowconfigure(0,weight=1)
        main_part.rowconfigure(1,weight=1)
        main_part.rowconfigure(2,weight=1)
        main_part.rowconfigure(3,weight=1)
        main_part.rowconfigure(4,weight=1)
        main_part.rowconfigure(5,weight=1)
        main_part.rowconfigure(6,weight=2)
        
####################################################################################################################        
        setting_edit_label = Label(main_part, text='IP 설정 편집', font=('Arial', 23), fg='white', bg='black')
        setting_edit_label.grid(row=0, column=0, sticky="W", padx=20)

        setting_combobox_frame = Frame(main_part, bg='black')
        setting_combobox_frame.grid(row=1, column=0, sticky='NWS', padx=20)
        setting_combobox_frame.rowconfigure(0, weight=1)
        setting_combobox_frame.columnconfigure(0, weight=1)
        
        values = ['Manual', 'Auto']
        style = ttk.Style()
        style.configure('W.TCombobox',arrowsize = 22)
        # cBox = ttk.Combobox(self, style='W.TCombobox')
        # combobox = ttk.Combobox(setting_combobox_frame, width=60, height=30, values=values, state='readonly')
        combobox = ttk.Combobox(setting_combobox_frame, width=60, height=20, values=values,style='W.TCombobox', state='readonly')
        combobox.config(font=('Arial', 23))
        combobox.option_add('*TCombobox*Listbox.font', ('Arial', 23))  # Set the font for the list items

        combobox.set('Auto')
        combobox.grid(row=0, column=0, sticky='NEWS')
####################################################################################################################
        on_img = Image.open('img/parts/toggle_on.png')
        resized_on_img = on_img.resize((65,37), Image.ANTIALIAS)
        self.on = ImageTk.PhotoImage(resized_on_img)
        off_img = Image.open('img/parts/toggle_off.png')
        resized_off_img = off_img.resize((65,37), Image.ANTIALIAS)
        self.off = ImageTk.PhotoImage(resized_off_img)

        IPv4_label = Label(main_part, text='IPv4', font=('Arial', 23), fg='white', bg='black')
        IPv4_label.grid(row=2, column=0, sticky="W", padx=20)
        IPv4_toggle_frame = Frame(main_part, bg='black')
        IPv4_toggle_frame.grid(row=3, column=0, sticky='W',padx=20)
        IPv4_toggle_frame.columnconfigure(0, weight=1)
        IPv4_toggle_frame.rowconfigure(0,weight=1)
        IPv4_toggle_frame.rowconfigure(1,weight=8)
        
        self.IPv4_toggle = Button(IPv4_toggle_frame, image=self.off, activebackground='black', bg='black',bd=0, border=None, borderwidth=0, command=None)        ##########################
        self.IPv4_toggle.grid(row=0, column=0, sticky='NEWS')
        
####################################################################################################################
        IPv6_label = Label(main_part, text='IPv6', font=('Arial', 23), fg='white', bg='black')
        IPv6_label.grid(row=4, column=0, sticky="W", padx=20)
        IPv6_toggle_frame = Frame(main_part, bg='black')
        IPv6_toggle_frame.grid(row=5, column=0, sticky='W',padx=20)

        self.IPv6_toggle = Button(IPv6_toggle_frame, image=self.off, activebackground='black', bg='black',bd=0, border=None, borderwidth=0, command=None)        ##########################
        self.IPv6_toggle.grid(row=0, column=0, sticky='NEWS')
        
####################################################################################################################        
        
        complete_frame = Frame(main_part, bg='black')
        complete_frame.grid(row=6, column=0, sticky='NEWS')
        complete_frame.rowconfigure(0, weight=1)
        complete_frame.columnconfigure(0, weight=1)
        complete_label = Label(complete_frame, text='Complete',font=('Arial', 26), bd=None, borderwidth=0, border=0, bg='black', fg='white')
        complete_label.grid(row=0, column=0, sticky='E')
        
        
    
    
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