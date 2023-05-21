# pyinstaller -w 
# --add-data './img/extra/*:img/extra' 
# --add-data './img/gauge/*:img/gauge' 
# --add-data './img/humidity/*:img/humidity'
# --add-data './img/parts/*:img/parts'
# --add-data './img/sensor/*:img/sensor'
# --add-data './img/temperature/*:img/temperature'
# --add-data './img/wifi/*:img/wifi'
# --add-data './img/wifi/strength/*:img/wifi/strength' 
# app.py

# 이거 양식은 이게 맞는데...
# pyinstaller -w --add-data './img/extra/*:img/extra' --add-data './img/gauge/*:img/gauge' --add-data './img/humidity/*:img/humidity' --add-data './img/parts/*:img/parts' --add-data './img/sensor/*:img/sensor' --add-data './img/temperature/*:img/temperature' --add-data './img/wifi/*:img/wifi' --add-data './img/wifi/strength/*:img/wifi/strength' app.py


