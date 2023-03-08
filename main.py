from MUi import *
import datetime
from V1weatherres import *
from PyQt5.QtCore import QThread,QPoint
from PyQt5.QtWidgets import QMainWindow,QApplication
import requests
import urllib.request
import sys
from configparser import ConfigParser

config_file="config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url= 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

from functools import lru_cache,cache
@cache
@lru_cache




class Window(QMainWindow,QThread):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Exit_button.clicked.connect(self.close)
        self.ui.Minimize_button.clicked.connect(self.showMinimized)
        self.ui.Refresh_button.clicked.connect(self.search)

    def mousePressEvent(self,event):
        self.oldPosition=event.globalPos()
    def mouseMoveEvent(self,event):
        delta=QPoint(event.globalPos()-self.oldPosition)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPosition=event.globalPos()

    def mainlogic(self,city):
        result=requests.get(url.format(city,api_key))
        if result:
            json = result.json()
            city = json['name']
            country = json['sys']
            temp_kelvin=json['main']['temp']
            temp_cel=int((float(temp_kelvin))-273.15)
            pres=json['main']['pressure']
            hum=json['main']['humidity']
            vis=json['visibility']
            vis1=vis/1000
            sunrise1=json['sys']['sunrise']
            sunrise2=datetime.datetime.fromtimestamp(sunrise1)
            sunrise3=sunrise2.strftime('%H:%M')
            sunset1=json['sys']['sunset']
            sunset2=datetime.datetime.fromtimestamp(sunset1)
            sunset3=sunset2.strftime('%H:%M')
            win=json['wind']['speed']
            desc=json['weather'] [0] ['description']
            weather1= json['weather'] [0] ['main']
            time1=datetime.datetime.now()
            time2=time1.strftime('%I:%M %p')
            date1=datetime.datetime.now()
            date2=date1.strftime('%d-%m-%y')
            day=time1.strftime('%A')

            final = [city, country, temp_kelvin, temp_cel, weather1, pres, hum, vis1, sunrise3, sunset3,win,desc,time2,date2, day]
            return final
        else:
            self.ui.Display_error_message.setText("City not Found...")

    def search(self):
        try:
            urllib.request.urlopen('http://google.com')
            self.ui.Display_error_message.setText("")
            city = self.ui.City_edit.text()
            weather = self.mainlogic(city)
            if weather:
                self.ui.Temperature_edit.setText(f"{weather[3]}")
                self.ui.Air_pressure_edit.setText(f"{weather[5]}")
                self.ui.Sunrise_edit.setText(f"{weather[8]}")
                self.ui.Sunset_edit.setText(f"{weather[9]}")
                self.ui.Visibility_edit.setText(f"{weather[7]}")
                self.ui.Wind_edit.setText(f"{weather[10]}")
                self.ui.weather_info.setText(f"{weather[11]}")
                self.ui.label_4.setText(f"{weather[12]}")
                self.ui.Date_edit.setText(f"{weather[13]}")
                self.ui.day_edit.setText(f"{weather[14]}")
                self.ui.Humidity_edit.setText(f"{weather[6]}")
                a=self.ui.weather_info.text()
                if a=="haze":
                    self.ui.Weather_change_icon.setIcon(QtGui.QIcon(u":/icons/haze.png"))
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-pixabay-163323.jpg);\n"
    "border-radius:30px;")
                elif a=="rain":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/rainy-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-benjamin-suter-3617453.jpg);\n"
    "border-radius:30px;")
                elif a=="thunderstom":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/thunderstorm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-andre-furtado-1162251.jpg);\n"
    "border-radius:30px;")
                elif a=="snow":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/snow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-bri-schneiter-346529.jpg);\n"
    "border-radius:30px;") 
                elif a=="mist":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/fog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-pixabay-163323.jpg);\n"
    "border-radius:30px;") 
                elif a=="shower rain":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/rainy-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-benjamin-suter-3617453.jpg);\n"
    "border-radius:30px;") 
                elif a=="few clouds":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-cliford-mervil-2469122.jpg);\n"
    "border-radius:30px;") 
                elif a=="scattered clouds":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/thunderstorm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-cliford-mervil-2469122.jpg);\n"
    "border-radius:30px;") 
                elif a=="broken clouds":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/fog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-cliford-mervil-2469122.jpg);\n"
    "border-radius:30px;") 
                elif a=="light rain":
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/rainy-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-benjamin-suter-3617453.jpg);\n"
    "border-radius:30px;") 
                else:
                    icon9 = QtGui.QIcon()
                    icon9.addPixmap(QtGui.QPixmap(":/icons/Clear Sky.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.ui.Weather_change_icon.setIcon(icon9)
                    self.ui.label.setStyleSheet("border-image: url(:/wallpaper/pexels-pixabay-36717.jpg);\n"
    "border-radius:30px;")


            else:
                self.ui.Display_error_message.setText("Something Went Wrong")
        except:
            self.ui.Display_error_message.setText("No Internet...")





            
            
            
app = QApplication(sys.argv)
gui = Window()
gui.show()
sys.exit(app.exec_())