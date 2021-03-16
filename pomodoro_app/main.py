from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    label_1.config(text="Timer", fg=GREEN)
    label_2.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text="Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_1.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_1.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    if count // 60 < 10:
        minutes = f"0{count//60}"
    else:
        minutes = count//60
    if count % 60 < 10:
        seconds = f"0{count % 60}"
    else:
        seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_loads = reps // 2
        label_2.config(text="✔" * work_loads)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label_1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_1.grid(column=1, row=0)

label_2 = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
label_2.grid(column=1, row=3)

button_1 = Button(text="Start", highlightthickness=0, command=start_timer)
button_1.grid(column=0, row=2)

button_2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_2.grid(column=2, row=2)


window.mainloop()
