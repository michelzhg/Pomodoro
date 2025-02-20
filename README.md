# Pomodoro Timer

This project is my **Year-Long Computer Science Specialty Project** completed in "Année de Première" (equivalent to Year 12 in the UK). It is an application based on the Pomodoro Technique, developed in Python using the Tkinter library.

## The Pomodoro Technique

The Pomodoro Technique is a time management method that involves:
- **Working in focused intervals** of 25 minutes, called "Pomodoros."
- **Taking a short break** of 5 minutes after each work session.
- **Taking a longer break** (typically 20 minutes) after several work sessions (usually after 4 Pomodoros).

This technique helps to improve productivity, reduce mental fatigue, and manage time more effectively.

## Why Tkinter?

I chose to use the **Tkinter** library for this project because:
- **Built-in Library:** Tkinter comes pre-installed with Python, making it easy to deploy without additional dependencies.
- **Simplicity:** It allows for the creation of simple yet functional graphical user interfaces, which is ideal for a project of this level.
- **Beginner-Friendly:** These are my first steps in Python, so I wanted a library that is accessible and easy to learn.
- **Customization:** Tkinter offers enough flexibility to design and implement the desired features (start, pause, skip, and reset functionalities).

## Key Features

- **Customizable Durations:**  
  Users can set the duration for work sessions, short breaks, and long breaks via input fields.

- **Session Management:**  
  The program automatically cycles through the different sessions (work, short break, long break) according to the Pomodoro Technique.

- **Control Buttons:**  
  - **Start:** Begins the timer.
  - **Pause/Resume:** Pauses or resumes the current timer.
  - **Skip:** Immediately moves to the next session.
  - **Reset:** Resets the timer and progress.

- **Modern and User-Friendly Interface:**  
  The interface features a modern color palette and a centered layout for improved readability and intuitive use.

- **Visual Countdown:**  
  A countdown timer is displayed at the center with a background matching the window, and completed sessions are indicated by check marks.

## Installation and Usage

1. **Installation:**  
   Ensure you have Python (version 3.7 min) installed on your machine. Tkinter is typically included by default with Python.

2. **Running the Program:**  
   Clone or download the project repository, then run the main script:
   ```bash
   python pomodoro_timer.py
