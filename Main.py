
import pytz
import json
import datetime 
import time
from datetime import datetime
import tkinter as tk
from tkinter import*
from tkintermapview import TkinterMapView
from PIL import Image,ImageTk
import requests

root=tk.Tk()
root.title("Dự báo thời tiết ")
root.geometry("2000x900")
root.configure(bg="white")

def format_response(weather):
    #try:
    City=weather['name']
    condition=weather['weather'][0]['description']
    temp=weather['main']['temp']
    final_str='City:%nCondtion:%s\nTemprature:%s'%(City,condition,temp)
    #except:
       #final_str='there was a problem retrieving that informati'
    return final_str
#fe55eda2af23292a08e7a7514f1b332c
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def get_weather(city):
    weather_key='fe55eda2af23292a08e7a7514f1b332c'
    url ='https://api.openweathermap.org/data/2.5/weather'

    params={"APPID":weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    print(response.json())
    weather=response.json()
    print(weather['name'])
    print(weather['weather'](0)['description'])
    print(weather['main']['temp'])



 #def get_weather():
    #city=textfield.get()
    # geolocator= Nominatim(user_agent='geoapiExercises')
     #location= geolocator.geocode(city)
     #obj = TimezoneFinder()
     #result = obj.timezone_at(lmg=location.longitude,lat=location.latitude)
     #timezone.config(Text=result)'''

    # tạo Icon
image_icon=ImageTk.PhotoImage(file='Icon./icon.png')
root.iconphoto(False,image_icon)

img=Image.open('./manhinh.png')
img=img.resize((1000,1000),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

    # ảnh nền
bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=1000,height=900)
#bg_lbl.place(x=0,y=0,width=1000,height=600)
    #Tiêu đề
heading_title=tk.Label(bg_lbl,text='Dự báo thời tiết các tỉnh, thành phố Việt Nam',fg='Black',bg='#8fa0b1',font=('times new roman',22,'bold'))
heading_title.place(x=250,y=18)
    # khung tìm kiếm 
frame_one=tk.Frame(bg_lbl,bg="#8fa0b1",bd=1)
frame_one.place(x=280,y=80,width=500,height=50)
    # thanh tìm kiếm
txt_box=tk.Entry(frame_one,font=('times new roman',33),width=15)
txt_box.grid(row=+0,column=0,sticky='w')
btn=tk.Button(frame_one,text='get weather',fg='Black',font=('times new roman',18,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=3,padx=15)     
    # khung nội dung 
frame_two=tk.Frame(bg_lbl,bg="white",bd=1)
frame_two.place(x=50,y=150,width=900,height=430)

# màu khung bản đồ
Frame_new=tk.Frame(bg="#CDB79E",bd=1)
Frame_new.place(x=1000,y=1,width=520,height=788)


    # màu khung 
result=tk.Label(frame_two,font=60,bg='white')
#result.place(relwidth=1,relheight=1)
    # tạo khung 
Round_box=ImageTk.PhotoImage(file="Icon/Hinhnen.png")
tk.Label(root,image=Round_box,bg="#57adff").place(x=100,y=200,width=600,height=360)
    # Tạo logo
image_logo=ImageTk.PhotoImage(file='Icon./iconkhung.png')
tk.Label(image=image_logo).place(x=50,y=10,width=200,height=145)
    #tạo danh mục ,cách nhau 30
tk.Label1=Label(root,text="Hôm nay ngày 17/03/2023",font=('Helvetica',11),fg="black")
tk.Label1.place(x=100,y=175)

tk.Label2=Label(root,text="Hôm nay ngày 17/03/2023",font=('Helvetica',11),fg="black")
tk.Label2.place(x=160,y=310)

tk.Label3=Label(root,text="Hôm nay ngày 17/03/2023",font=('Helvetica',11),fg="black")
tk.Label3.place(x=160,y=370)

tk.Label4=Label(root,text="Hôm nay ngày 17/03/2023",font=('Helvetica',11),fg="black")
tk.Label4.place(x=160,y=432)


    #tạo clock
clock=tk.Label(root,text="12:01 pm",font=('Helvetica',50),fg="black",bg='white')
clock.place(x=660,y=175)

home=pytz.timezone('Asia/Ho_Chi_Minh')
local_time=datetime.now(home)
current_time=local_time.strftime('%I:%M %p')
clock.config(text=current_time)

# tạ khung
Frame=Frame(root,width=908,height=250,bg='#CCCCFF')
Frame.place(x=52,y=580)

firstbox=ImageTk.PhotoImage(file='Icon./maunen1.png')
secondbox=ImageTk.PhotoImage(file='Icon./maunen1.png')
thirdbox=ImageTk.PhotoImage(file='Icon./maunen1.png')
fourthtbox=ImageTk.PhotoImage(file='Icon./maunen1.png')
#secondbox=ImageTk.PhotoImage(file='Icon./maunen.png')
Label(Frame,image=firstbox,bg='#212120').place(x=5,y=5)

day1=Label(image=firstbox,font='arial 30',bg='white')
day1.place(x=58,y=587)

fisrt = datetime.now()
day1.config(text=fisrt.strftime('%A'))

Label(Frame,image=secondbox,bg='#212120').place(x=230,y=5)
Label(Frame,image=thirdbox,bg='#212120').place(x=455,y=5)
Label(Frame,image=fourthtbox,bg='#212120').place(x=680,y=5)

#Frame_new=tk.Frame(bg="#CDB79E",bd=1)
#Frame_new.place(x=1000,y=1,width=520,height=788)

#map_widget = (root,Frame_new,width=30,height=60,corner_radius=0)
#map_widget.pack(fill='both',expand=True)
 



root.mainloop() 
