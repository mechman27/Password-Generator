from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer =  None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    time_label.config(text=f"Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks_label.config(text="", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    work_short_break = SHORT_BREAK_MIN * 60
    work_long_break = LONG_BREAK_MIN * 60
    if reps > 20:
        reps = 0
    reps += 1 
    if reps % 8 == 0:
        time_label.config(text=f"Break", fg=RED)
        countdown_timer(work_long_break)
        checkmarks_label.config(text="", fg=GREEN)
    elif reps % 2 == 0:
        time_label.config(text=f"Break", fg=PINK)
        countdown_timer(work_short_break)
    else:
        time_label.config(text=f"Work", fg=GREEN)
        countdown_timer(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_timer(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count-1 )
    else:
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        checkmarks_label.config(text=marks, fg=GREEN)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=10, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Intermediate/Day 28 Pomodoro method timer/tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 112, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time_label = Label(window, text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
time_label.grid(column=1, row=0)                                    
checkmarks_label = Label(window, text="", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

start_button = Button(window, text="Start", font=(FONT_NAME, 12), bg=YELLOW, highlightthickness=0, command = start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(window, text="Reset", font=(FONT_NAME, 12), bg=YELLOW, highlightthickness=0, command = reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()