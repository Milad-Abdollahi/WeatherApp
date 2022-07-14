from tkinter import *
import requests

root = Tk()

HEIGHT = 300
WIDTH = 300

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9bef40589add85943e01424f5b92b750&units=metric'
    try:
        response = requests.get(url)
        current_weather = response.json()
        city_name = current_weather['name']
        current_temp = current_weather['main']['temp']
        weather_description = current_weather['weather'][0]['description']
        weather_label['text'] = f'''{str(city_name)} 
        
{str(weather_description)} 

{str(current_temp)}'''
    except:
        weather_label['text'] = 'API response error'

background_image = PhotoImage(file='weather_background_image.png')
background_label = Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame = Frame(root, bg='')
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

btn = Button(frame, text='آب و هوا', font=35, command=lambda: get_weather(entry_bar.get()))
btn.place(relx=0.65, rely=0.1, relheight=0.8, relwidth=0.3)

entry_bar = Entry(frame, font=40)
entry_bar.place(relx=0.05, rely=0.1, relwidth=0.55, relheight=0.8)

lower_frame = Frame(root, bd=5)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.65, relwidth=0.75, anchor='n')

weather_label = Label(lower_frame, font=('Bold', 18))
weather_label.place(relwidth=1, relheight=1)

root.mainloop()
