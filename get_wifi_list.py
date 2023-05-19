# orangepi 에서는 이렇게 해야한다. - PC에서는 error가 뜨는 것이 맞다.

from wifi import Cell, Scheme

cells = Cell.all('wlan0')
for cell in cells:
    print(cell.ssid)