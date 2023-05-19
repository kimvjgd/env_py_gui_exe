import tkinter as tk
from tkinter import ttk
from home_screen import Home
from element_screen import Element
from wifi_screen import WifiScreen
from wifi_connection_screen import WifiConnectionScreen
from wifi_detail_screen import WifiDetailScreen
from info_screen import InfoScreen
from keyboard_screen import KeyboardSreen
from ethernet_screen import EthernetScreen
from mac_address import get_mac_address



# 나중에 링크 풀어줘야한다.
from uart_data_thread import UartDataThread

 

FULL_SCREEN = False             # (True/False) - (Full Screen/Fixed Size Screen)
PRIMARY_COLOR = "#2e3f4f"
DEVICE_NUMBER = 1

class EnvSensor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TVOC = tk.StringVar(value=0)
        self.CO2 = tk.StringVar(value=0)
        self.PM25 = tk.StringVar(value=0)
        self.PM10 = tk.StringVar(value=0)
        self.CH2O = tk.StringVar(value=0)
        self.Sm = tk.StringVar(value=0)
        self.NH3 = tk.StringVar(value=0)
        self.CO = tk.StringVar(value=0)
        self.NO2 = tk.StringVar(value=0)
        self.H2S = tk.StringVar(value=0)
        self.LIGHT = tk.StringVar(value=0)
        self.SOUND = tk.StringVar(value=0)
        self.Rn = tk.StringVar(value=0)
        self.O3 = tk.StringVar(value=0)
        self.temperature = tk.StringVar(value=0)
        self.humidity = tk.StringVar(value=0)
        self.device_number = DEVICE_NUMBER
        self.mac_address = get_mac_address()
        self.wifi_ssid = tk.StringVar(value='')
        self.wifi_pw = tk.StringVar(value='')
        
        self.eth0_connection = False            # 초기값은 0으로 잡아준다.
        self.wlan0_connection = False
        

        style = ttk.Style(self)
        style.theme_use("clam")
        
        style.configure("Home.TFrame", background=PRIMARY_COLOR)
        
        self["background"] = PRIMARY_COLOR
        
        self.title("Env LAB")
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)
        # self.sensor_name = tk.StringVar(value='TVOC')
        self.sensor_name = 'TVOC'
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="NEWS")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        container.config(width=800, height=480)
        
        self.frames = dict()
        
        #### frames ####
        
        # For Home
        self.home_frame = Home(container, self, lambda: self.show_element_frame(Element), lambda: self.show_frame(WifiScreen), lambda: self.show_frame(InfoScreen), lambda: self.show_frame(EthernetScreen))
        self.home_frame.grid(row=0, column=0, sticky="NESW")
        ############################################################################################################################################
        
        # For Element
        self.element_frame = Element(container, self, lambda: self.show_frame(Home), sensor=self.sensor_name)      # just for sample TVOC
        self.element_frame.grid(row=0, column=0, sticky="NESW")
        ############################################################################################################################################
        
        # For Wifi
        self.wifi_frame = WifiScreen(container, self, lambda: self.show_frame(Home), lambda: self.show_frame(WifiDetailScreen))
        self.wifi_frame.grid(row=0, column=0, sticky="NEWS")
        ############################################################################################################################################
        
        # For Wifi Connection Screen
        self.wifi_connection_frame = WifiConnectionScreen(container, self, lambda: self.show_frame(WifiScreen))
        self.wifi_connection_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        # For Wifi Detail Screen
        self.wifi_detail_frame = WifiDetailScreen(container, self, lambda:self.show_frame(WifiScreen), lambda: self.show_frame(KeyboardSreen))
        self.wifi_detail_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################
        
        # For Info Screen
        self.info_frame = InfoScreen(container, self, lambda:self.show_frame(Home))
        self.info_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        # For Ethernet Screen
        self.ethernet_frame = EthernetScreen(container, self, lambda:self.show_frame(Home))
        self.ethernet_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################
        
        # For Keyboard Screen
        self.keyboard_frame = KeyboardSreen(container, self, self.wifi_detail_frame.password_entry, lambda:self.show_frame(WifiDetailScreen))
        self.keyboard_frame.grid(row=0, column=0, sticky='NEWS')
        ############################################################################################################################################

        
        
        self.frames[Home] = self.home_frame
        self.frames[Element] = self.element_frame
        self.frames[WifiScreen] = self.wifi_frame
        self.frames[WifiConnectionScreen] = self.wifi_connection_frame
        self.frames[WifiDetailScreen] = self.wifi_detail_frame
        self.frames[InfoScreen] = self.info_frame
        self.frames[EthernetScreen] = self.ethernet_frame
        self.frames[KeyboardSreen] = self.keyboard_frame
        
        # First Screenu
        self.show_frame(Home)

    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
    
    def show_element_frame(self, container):
        # Element UI고치느라 주석
        self.element_frame.change_image(self.sensor_name)  
        frame = self.frames[container]
        frame.tkraise()
    
        





if __name__== '__main__':

    app = EnvSensor()
    u = UartDataThread(app)
    u.start()

    app.home_frame.get_all_data()
    app.home_frame.time_update()
    
    # 꼭 풀어줘야함 519
    app.home_frame.lan_connection_update()
    app.wifi_frame.get_wifi_list()
    app.wifi_frame.get_current_wifi()
    
    app.geometry("800x480")
    app.attributes('-fullscreen', FULL_SCREEN)
    app.mainloop()
# self.get_image(sensor_description_part, 'img/sensor/CH2O.png', 80, 80, 0, 0, 'NEWS', rowspan=2)
