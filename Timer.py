import tkinter
from tkinter import *
import pygame
import time

FONT ="Baskerville"
TIME_TEXT = None
canvas = None
window = Tk()
window.title("Timer      by Prajeet.B")
window.attributes("-topmost", True)

pause = False
image = None

def clear_screen():
    canvas.delete("all")
    input_hour.destroy()
    input_minute.destroy()
    input_second.destroy()

def pauseButton():
    global pause, pause_button, resume_button
    pause = True
    pause_button.destroy()
    resume_button = Button(text="Resume", command=resumeButton)
    resume_button.place(x=90,y=160)


def resumeButton():
    global pause, newh, newm, news, resume_button, pause_button
    pause = False
    resume_button.destroy()
    pause_button = Button(text="Pause", command=pauseButton)
    pause_button.place(x=100, y=160)
    timer(newh, newm, news)

def stopButton():
    canvas.delete("all")
    stop_button.destroy()
    reset()

def play_audio():

    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.load("Session complete audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    clear_screen()
    reset()


def timer(hour, minute, second):
    global TIME_TEXT, image
    global pause, newh, newm, news

    formatted_minute = f"{minute:02d}"
    formatted_second = f"{second:02d}"
    formatted_hour = f"{hour:02d}"
    canvas.itemconfig(TIME_TEXT, text=f"{formatted_hour}:{formatted_minute}:{formatted_second}")
    if hour == 0 and minute == 0 and second == 0:
        play_audio()
        return
    if hour > 0 and minute == 0 and second == 0:
        hour -= 1
        minute = 60
    if hour == 1 and minute == 0 and second == 0:
        hour -= 1
        minute = 60
    if second == 0:
        minute -= 1
        second = 60

    if pause is not True:
        window.after(1000, timer,hour, minute, second-1)
        newh = hour
        newm = minute
        news = second


def start():
    global  TIME_TEXT, image
    global stop_button, pause_button

    start_button.config(state="disabled")
    hour_data = int(input_hour.get())
    minute_data = int(input_minute.get())
    second_data = int(input_second.get())
    canvas.delete("all")
    input_hour.destroy()
    input_minute.destroy()
    input_second.destroy()
    image = PhotoImage(file="Halloween.png")
    canvas.create_image(150, 100, image=image)

    TIME_TEXT = canvas.create_text(150, 120, text=f"00:00:00", fill="red", font=(FONT, 35, "bold"))
    canvas.create_text(150, 85, text="Timer", fill="red", font=("Roman", 15))
    canvas.pack()

    stop_button = Button(text="Stop", command=stopButton)
    stop_button.place(x=150, y=160)
    pause_button = Button(text="Pause", command=pauseButton)
    pause_button.place(x=100, y=160)

    timer(hour_data, minute_data,second_data)
def reset():
    global input_hour, input_minute, input_second, canvas, start_button, image
    image = PhotoImage(file="Halloween.png")
    canvas.create_image(150,100, image=image)
    input_hour = Entry(width=10)
    input_hour.place(x=150,y=70)
    input_hour.insert(0, "0")
    input_minute = Entry(width=10)
    input_minute.place(x=150,y=100)
    input_minute.insert(0, "0")
    input_second = Entry(width=10)
    input_second.place(x=150,y=130)
    input_second.insert(0, "0")
    hour = canvas.create_text(110,80, text=f"Hour:", fill="black", font=(FONT, 15, "bold"))
    minute = canvas.create_text(110,110, text=f"Minute:", fill="black", font=(FONT, 15, "bold"))
    second = canvas.create_text(110,140, text=f"Second:", fill="black", font=(FONT, 15, "bold"))
    canvas.pack()

    start_button = Button(text="Start", command= start)
    start_button.place(x=150,y=160)


canvas = Canvas(width=300, height=200)
reset()
window.mainloop()









