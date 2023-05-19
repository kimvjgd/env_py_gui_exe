# from wifi import Cell, Scheme
# import subprocess

# def get_wifi_list():
#     cells = Cell.all('wlan0')
#     for cell in cells:
#         print(cell.ssid)
    
#     try:
#         result = subprocess.check_output(["iwgetid", "-r"])
#         print("현재 연결된 WiFi의 SSID:", result.decode().strip())
#         # self.current_wifi_label.config(text=result.decode().strip())
#         for cell in cells:
#             print(cell.ssid)
#         # 여기서 gui update해줘야한다.
#     except:
#         result = ''
        
#     # self.current_wifi_label.after(1000, self.get_wifi_list)
    
# get_wifi_list()

import wifi
import subprocess
import re

def get_current_wifi_info():
    try:
        output = subprocess.check_output(["nmcli", "dev", "wifi", "list"])
        output = output.decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            # print(line)
            if "*" in line:
                # Extract the Wi-Fi information from the line
                wifi_info = re.findall(r"\S+", line)
                return [wifi_info[2], wifi_info[-3]]            # name & strength를 반환
                
                
                # print(wifi_info)
    except subprocess.CalledProcessError:
        return None
def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlan0', ssid)

    if cell:
        return cell

    return False


def connect_wifi(ssid, password):
    cmd = 'nmcli device wifi connect {} password {}'.format(ssid, password)
    subprocess.call(cmd, shell=True)

def Connect(ssid, password=None):
    cell = FindFromSearchList(ssid)

    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, password)
    scheme.save()
    return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    return False
def wifi_Search():
    wifilist = []
    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        if cell.ssid != '':
            signal = abs(cell.signal)
            if signal <= 50:
                wifilist.append([cell.ssid, 'a'])
            elif signal <= 65:
                wifilist.append([cell.ssid, 'b'])
            else:
                wifilist.append([cell.ssid, 'c'])
    
    '''
    cell.signal
                <= 50           -> Good connection strength => a
                50 < && < 65    -> SoSo connection strength => b
                65 <=           -> Bad  connection strength => c

    '''

    return wifilist

    




# get_current_wifi_info()

'''
IN-USE  BSSID              SSID                   MODE   CHAN  RATE        SIGNA                     L  BARS  SECURITY
        2C:D2:6B:61:C9:7C  NEXT340-ca5305         Infra  6     65 Mbit/s   100                          ▂▄▆█  WPA2
        B4:B0:24:C3:96:2E  mirresys               Infra  7     405 Mbit/s  100                          ▂▄▆█  WPA2
        B6:B0:24:A3:96:2E  --                     Infra  7     405 Mbit/s  100                          ▂▄▆█  WPA1 WPA2
        88:36:6C:FD:19:9E  DIRECT-ABOFFIEPCmsJP   Infra  7     270 Mbit/s  100                          ▂▄▆█  WPA2
        B4:B0:24:C3:96:30  mirresys               Infra  161   405 Mbit/s  90                           ▂▄▆█  WPA2
        B6:B0:24:D3:96:2E  --                     Infra  161   405 Mbit/s  90                           ▂▄▆█  WPA1 WPA2
        90:9F:33:A9:0B:8C  sangsanglab            Infra  13    405 Mbit/s  79                           ▂▄▆_  WPA2
*       90:9F:33:A8:0B:8C  sangsanglab_5G         Infra  149   405 Mbit/s  77                           ▂▄▆_  WPA2
'''




########################################################################################
# ehternet or wlan notification
import psutil

# def check_network_connection():
#     """Check if Ethernet or Wi-Fi is connected"""
#     interfaces = psutil.net_if_stats()
#     print(interfaces)
#     for interface, stats in interfaces.items():
#         if interface == 'lo':  # skip localhost
#             continue
#         if stats.isup and (interface.startswith('en') or interface.startswith('eth') or interface.startswith('wlan')):
#             return True
#     return False

# # Example usage
# if check_network_connection():
#     print("Network is connected")
# else:
#     print("Network is disconnected")

#############################

def get_current_connection_state():
    # type - dictionary
    interfaces = psutil.net_if_stats()
    # print('eth0: ',interfaces['eth0'].isup)
    # print('wlan0: ',interfaces['wlan0'].isup)

    eth0_connection = interfaces['eth0'].isup
    wlan0_connection = interfaces['wlan0'].isup
    return [eth0_connection, wlan0_connection]

