import tkinter as tk
from tkinter import ttk
import math

# Durées par défaut en minutes
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
paused = False
current_count = 0  # Temps restant en secondes lors de la pause

def reset_timer():
    global reps, paused, timer, current_count
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Pomodoro", foreground="#ecf0f1")
    check_label.config(text="")
    reps = 0
    paused = False
    current_count = 0
    start_button.config(state="normal")
    pause_button.config(text="Pause")

def start_timer():
    global reps, paused, timer
    start_button.config(state="disabled")
    paused = False
    pause_button.config(text="Pause")
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", foreground="#e74c3c")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", foreground="#f39c12")
    else:
        count_down(work_sec)
        timer_label.config(text="Work", foreground="#27ae60")

def count_down(count):
    global timer, current_count
    current_count = count
    minutes = math.floor(count / 60)
    seconds = count % 60
    seconds = f"0{seconds}" if seconds < 10 else seconds
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0 and not paused:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        work_sessions = math.floor(reps / 2)
        marks = "✔" * work_sessions
        check_label.config(text=marks)

def toggle_pause():
    global paused, timer, current_count
    if not paused:
        paused = True
        if timer is not None:
            window.after_cancel(timer)
        pause_button.config(text="Resume")
    else:
        paused = False
        pause_button.config(text="Pause")
        count_down(current_count)

def skip_session():
    global timer, paused
    if timer is not None:
        window.after_cancel(timer)
    paused = False
    pause_button.config(text="Pause")
    start_timer()

def update_durations():
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    try:
        WORK_MIN = int(work_entry.get())
        SHORT_BREAK_MIN = int(short_break_entry.get())
        LONG_BREAK_MIN = int(long_break_entry.get())
        config_status_label.config(text="Durées mises à jour !", foreground="#27ae60")
    except ValueError:
        config_status_label.config(text="Veuillez entrer des valeurs entières.", foreground="#e74c3c")

# Configuration de la fenêtre principale avec un fond sombre moderne
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, background="#2c3e50")

# Thème ttk moderne
style = ttk.Style(window)
style.theme_use("clam")
style.configure("TButton",
                font=("Helvetica", 12, "bold"),
                padding=10,
                foreground="#ffffff",
                background="#3498db")
style.map("TButton", background=[("active", "#2980b9")])
style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1")
style.configure("TFrame", background="#2c3e50")

# Label du titre centré
timer_label = ttk.Label(window, text="Pomodoro", font=("Helvetica", 40, "bold"))
timer_label.grid(column=0, row=0, columnspan=4, pady=10)

# Frame de configuration pour modifier les durées
config_frame = ttk.Frame(window)
config_frame.grid(column=0, row=1, columnspan=4, pady=10)

work_label = ttk.Label(config_frame, text="Work (min):", font=("Helvetica", 12))
work_label.grid(column=0, row=0, padx=5)
work_entry = ttk.Entry(config_frame, width=5, font=("Helvetica", 12))
work_entry.insert(0, str(WORK_MIN))
work_entry.grid(column=1, row=0, padx=5)

short_break_label = ttk.Label(config_frame, text="Short Break (min):", font=("Helvetica", 12))
short_break_label.grid(column=2, row=0, padx=5)
short_break_entry = ttk.Entry(config_frame, width=5, font=("Helvetica", 12))
short_break_entry.insert(0, str(SHORT_BREAK_MIN))
short_break_entry.grid(column=3, row=0, padx=5)

long_break_label = ttk.Label(config_frame, text="Long Break (min):", font=("Helvetica", 12))
long_break_label.grid(column=4, row=0, padx=5)
long_break_entry = ttk.Entry(config_frame, width=5, font=("Helvetica", 12))
long_break_entry.insert(0, str(LONG_BREAK_MIN))
long_break_entry.grid(column=5, row=0, padx=5)

update_button = ttk.Button(config_frame, text="Set Durations", command=update_durations)
update_button.grid(column=6, row=0, padx=5)

config_status_label = ttk.Label(config_frame, text="", font=("Helvetica", 10))
config_status_label.grid(column=0, row=1, columnspan=7, pady=5)

# Canvas pour afficher le décompte du timer
# Le fond du canvas est mis à la même couleur que le fond de la fenêtre
canvas = tk.Canvas(window, width=300, height=200, background="#2c3e50", highlightthickness=0)
timer_text = canvas.create_text(150, 100, text="00:00", fill="#ecf0f1", font=("Helvetica", 40, "bold"))
canvas.grid(column=0, row=2, columnspan=4, pady=20)

# Boutons Start, Pause, Skip et Reset, centrés
start_button = ttk.Button(window, text="Start", command=start_timer)
start_button.grid(column=0, row=3, padx=10, pady=20)

pause_button = ttk.Button(window, text="Pause", command=toggle_pause)
pause_button.grid(column=1, row=3, padx=10, pady=20)

skip_button = ttk.Button(window, text="Skip", command=skip_session)
skip_button.grid(column=2, row=3, padx=10, pady=20)

reset_button = ttk.Button(window, text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3, padx=10, pady=20)

# Label pour afficher les marques de progression centré
check_label = ttk.Label(window, font=("Helvetica", 24))
check_label.grid(column=0, row=4, columnspan=4, pady=20)

window.mainloop()