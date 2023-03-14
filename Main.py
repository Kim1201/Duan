import tkinter as tk
from PIL import Image,ImageTk
import requests
#from tkinter import Tk, mainloop, TOP
root=tk.Tk()
root.title("Dự báo thời tiết ")
root.geometry("1000x600")
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

 # tạo Icon
image_icon=ImageTk.PhotoImage(file='Icon./icon.png')
root.iconphoto(False,image_icon)




img=Image.open('./dubaothoitiet.png')
img=img.resize((1000,600),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)


# ảnh nền
bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=1000,height=600)
bg_lbl.place(x=0,y=0,width=1000,height=600)

#Tiêu đề
heading_title=tk.Label(bg_lbl,text='Dự báo thời tiết các nước Đông Nam Á',fg='Black',bg='Cyan',font=('times new roman',22,'bold'))
heading_title.place(x=290,y=18)
# khung 
frame_one=tk.Frame(bg_lbl,bg="#42c2f4",bd=1)
frame_one.place(x=280,y=80,width=500,height=50)

# thanh tìm kiếm
txt_box=tk.Entry(frame_one,font=('times new roman',33),width=15)
txt_box.grid(row=+0,column=0,sticky='w')
btn=tk.Button(frame_one,text='get weather',fg='Black',font=('times new roman',18,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=3,padx=15)            
# màu thanh tìm kiếm
frame_two=tk.Frame(bg_lbl,bg="#FFFFFF",bd=1)
frame_two.place(x=50,y=150,width=900,height=430)
# màu khung 
result=tk.Label(frame_two,font=40,bg='white')
result.place(relwidth=1,relheight=1)



root.mainloop()