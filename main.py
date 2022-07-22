from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECS=60
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
times = 0
clock = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reseter():
    window.after_cancel(clock)
    canvas.itemconfig(Canvas_text, text = "00:00")
    timer_label.config(text="Timer!")
    global times
    times = 0
    check_mark1["text"]=""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer():
    global times
    times += 1
    if  times % 2 ==1:
        timer_label["text"] = "Work Champ!"
        timer_label["fg"] = PINK
        counter(WORK_MIN*SECS)
    elif times == 8:
        timer_label["text"] = "Big Boy Break!"
        timer_label["fg"] = RED
        counter(LONG_BREAK_MIN*SECS)
    else:
        timer_label["text"] = "Small Break!"
        timer_label["fg"] = GREEN
        counter(SHORT_BREAK_MIN*SECS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global times
    global clock

    rounds = math.floor(times/2)
    checker = "✔"

    mins = math.floor(count/60)
    secs= count % 60
    if secs==0:
        secs="00"
    elif secs < 10:
        secs = "0" + str(secs)
    canvas.itemconfig(Canvas_text,text=f"{mins}:{secs}")
    if count > 0:
        clock = window.after(1000,counter,count-1)
    else:
        timer()
        for x in range(rounds):
            checker += "✔"
    check_mark1.config(text=checker)


# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Pomodoro")
window.config(pady=70,padx=95,bg=YELLOW)


timer_label = Label(text="Timer!",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW,highlightthickness=0)
timer_label.grid(row=0,column=1)



canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tom_image = PhotoImage(file="tomato.png")
canvas.create_image(99.5,113,image=tom_image)
Canvas_text = canvas.create_text(99.5,130,text="00:00",font=(FONT_NAME,35,"italic"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start",highlightthickness=0,command=timer)
start_button.grid(row=2,column=0)


reset_button = Button(text="Reset",highlightthickness=0,command=reseter)
reset_button.grid(row=2,column=2)

check_mark1=Label(fg=GREEN,bg=YELLOW)
check_mark1.grid(row=3,column=1)


window.mainloop()