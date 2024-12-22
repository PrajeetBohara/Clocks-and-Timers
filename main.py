from tkinter import *
import time

PURPLE = "#7e5cad"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Timer")
#window.config(padx=50,pady=50)
#If we wanna make the window slightly bigger prefer to use config to extend the size of the window so
# that we don't mess up the placing of the image and only just increase the size of the screen by 50.


def timer(hour, minute, second):
    formatted_minute = f"{minute:02d}"
    formatted_second = f"{second:02d}"
    formatted_hour = f"{hour:02d}"
    canvas.itemconfig(time_text, text=f"{formatted_hour}:{formatted_minute}:{formatted_second}")
    if hour == 0 and minute == 0 and second == 0:
        return #exit this function without returning anything
    if minute == 0 and hour > 0 and second == 0:
        hour -= 1
    if hour == 1 and minute == 0 and second == 0:
        hour -= 1
        minute = 60
    if second == 0:
        minute -= 1
        second = 60

    window.after(1000, timer,hour, minute, second-1)

canvas = Canvas(width=300, height=200)#create a canvas of specific width and height
image = PhotoImage(file="Halloween.png") #we need PhotoImage class to import the images and handle them
canvas.create_image(150,100, image=image) #here in parameters the given values are the x,y position

time_text = canvas.create_text(150,120, text=f"00:00:00", fill="red", font=(FONT_NAME, 35, "bold"))
canvas.create_text(150,85, text="Timer", fill="red", font=("Roman", 15))
#this creates the text in canvas at specific location with fill color and the font
canvas.pack() #to display the canvas

timer(2,1, 5)

button = Button(text="Start")
button.pack()

window.mainloop()
