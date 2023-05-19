import tkinter as tk
from tkinter import ttk
from keyboard_screen import KeyboardSreen

class GUITest(tk.Tk):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.title('GUI TEST')  
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0, weight=1)
        self.resizable(False, False)

        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky='NEWS')
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.config(width=800, height=480)
        self.frames = dict()

        # For Keyboard Screen
        self.keyboard_frame = KeyboardSreen(container, self)
        self.keyboard_frame.grid(row=0, column=0, sticky='NEWS')
        
        
if __name__=='__main__':
    app = GUITest()
    app.geometry("800x480")
    app.mainloop()



