import os
import sys
import time
import threading
import tkinter as tk
from PIL import Image, ImageTk  
from playsound import playsound
from tkinter import font, messagebox

class PomodoroApp:
    # 🍅 The full app is encapsulated by this class 🍅 
    # This is a Castlevania themed Pomodoro app with costumizible work and break timers and cycles
    # App can be stopped and restarted at any point or Reset and change timer/cycle values
    
    def __init__(self, root):
        # Get the directory of the current file
        if getattr(sys, 'frozen', False):
            # PyInstaller bundle
            self.base_path = os.path.join(os.path.dirname(sys.executable), '..', 'Resources')
        else:
            if '__file__' in locals():
                self.base_path = os.path.dirname(os.path.abspath(__file__))
            else:
                # Fallback: Use current working directory if __file__ is not defined
                self.base_path = os.getcwd()
        #  Defining instance variables
        self.root = root
        self.root.title("My 🍅 Timer") # main title
        self.is_running = False # flag for running the timer, default is False
        self.work_mins = 25 # default work duration in minutes
        self.break_mins = 5 # default break duration in minutes
        self.time_left = self.work_mins * 60 # remaining time converted to seconds
        self.is_working = True # flag to distinguish working timer and break timer
        self.cycles = 1 # default number of cycles
        self.cycle_number = 0 # current cycle number
    
        # Load the PNG background
        self.background_image = Image.open(self.rel_path_to("images/background.png"))  # load PNG file
        self.background_image = self.background_image.resize((400, 300), Image.LANCZOS)  # resize to fit the window
        self.background_photo = ImageTk.PhotoImage(self.background_image) # load to image

        # Create a label for the background
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)  # fill the window with the background image
        
        # Fonts used for text, input numbers, and timer
        self.font_text = font.Font(family="Angel wish", size=20, weight='bold', slant="italic")
        self.font_number = font.Font(family="Cloister Black", size=16, weight="normal")
        self.font_timer = font.Font(family="The Centurion", size=40, weight="bold", slant="italic")

        # Defining args for positioning
        self.work_label_pack = ['w', 10, (15,2)] # args for position and padding of work time label
        self.pack_args = ['w', 10, 2] # args for position and padding of remaining labels
        
        # Input for Work time
        self.work_label = tk.Label(root, text=' Work Time ', font=self.font_text, bd=0) # text label
        self.work_label.pack(anchor=self.work_label_pack[0], padx=self.work_label_pack[1], pady=self.work_label_pack[2])
        self.work_entry = tk.Entry(root, font=self.font_number, width=3, justify='center') # input label
        self.work_entry.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.work_entry.insert(0, str(self.work_mins)) # inserts default value
        
        # Input for break time
        self.break_label = tk.Label(root, text=' Break Time ', font=self.font_text, bd=0, highlightthickness=0)
        self.break_label.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.break_entry = tk.Entry(root, font=self.font_number, width=3, justify='center')
        self.break_entry.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.break_entry.insert(0, str(self.break_mins)) # default value
        
        # Input for cycle
        self.cycle_label = tk.Label(root, text='Cycles', font=self.font_text)
        self.cycle_label.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.cycle_entry = tk.Entry(root, font=self.font_number, width=2, justify='center')
        self.cycle_entry.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.cycle_entry.insert(0, str(self.cycles)) # default value
        
        # Timer display label using a custom background
        self.timer_bg_og = Image.open(self.rel_path_to("images/bg1.png"))
        self.timer_bg_og_resize = self.timer_bg_og.resize((170, 95), Image.LANCZOS) 
        self.timer_bg = ImageTk.PhotoImage(self.timer_bg_og_resize)
        self.timer_label = tk.Label(root, image=self.timer_bg, text=self.format_time(self.time_left), font=self.font_timer, 
                                    compound='center', bd=0, padx=0, pady=0) # adding background to the label
        
        # Button frame using a custom background
        self.buttons_bg_og = Image.open(self.rel_path_to("images/bg1.png"))
        self.tbuttons_bg_og_resize = self.buttons_bg_og.resize((270, 33), Image.LANCZOS)
        self.buttons_bg = ImageTk.PhotoImage(self.tbuttons_bg_og_resize)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="bottom", pady=10)
        self.button_label = tk.Label(self.button_frame, image=self.buttons_bg)
        self.button_label.pack(fill="both", expand=True)

        # Start, Stop and Reset buttons inside the Button frame
        self.start_button = tk.Button(self.button_label, text='Start', font=self.font_text, command=self.start_timer, bd=0, 
                                      highlightbackground='#470000', width=3, height=1) # giving a dark red bg color
        self.start_button.pack(side='left', padx=10)
        
        self.stop_button = tk.Button(self.button_label, text='Stop', font=self.font_text, command=self.stop_timer, bd=0, 
                                     highlightbackground='#470000', width=3, height=1)
        self.stop_button.pack(side='left', padx=15)
        
        self.reset_button = tk.Button(self.button_label, text='Reset', font=self.font_text, command=self.reset_timer, bd=0, 
                                      highlightbackground='#470000', width=3, height=1)
        self.reset_button.pack(side='right', padx=10)
        
        # Set starting window size (width x height)
        self.root.geometry("")  # Auto adjusts window size according the the packed labels

    def start_timer(self):
        # Get user input for the timers
        try:
            self.work_mins = float(self.work_entry.get())
            self.break_mins = float(self.break_entry.get())
            self.cycles = int(self.cycle_entry.get())
            self.time_left = self.work_mins * 60
            # Hide input fields
            self.work_label.pack_forget()
            self.work_entry.pack_forget()
            self.break_label.pack_forget()
            self.break_entry.pack_forget()
            self.cycle_label.pack_forget()
            self.cycle_entry.pack_forget()
            # Show timer label
            self.timer_label.place(relx=0.5, rely=0.5, anchor='center')
            self.root.geometry("300x200") # resizing window
            # Start running the timer
            self.is_running = True # set the running flag
            self.root.title(f"Work Timer 🍅") # change title
            self.play_sound_threaded(self.rel_path_to('sounds/SoulSteal.wav')) # sound for start of work timer
            self.run_timer()
        except ValueError:
            messagebox.showerror("Invalid input", "Enter int or decimal for the timers and int for cycles, ex.: 1 - 0.5 - 1") 
        if self.work_mins <= 0 or self.break_mins <= 0 or self.cycles <= 0:
            messagebox.showerror("Invalid input", "Timers and cycles must be greater than zero.")
        return
    
    def run_timer(self):
        if  self.is_running:
            if self.time_left > 0:
                self.time_left -= 1 # decrease time left value
                self.timer_label['text'] = self.format_time(self.time_left) # update timer label
                self.root.after(1000, self.run_timer) # call run_timer again after 1 second
            else:
                self.switch_timer() # if time left is 0 switch the other timer
    
    def switch_timer(self):
        if self.is_working: # if previous timer was work change to break
            self.root.title(f"Break Timer 🍅")
            self.time_left = self.break_mins * 60 # set timer for the break
            self.timer_label['text'] = self.format_time(self.time_left)
        else: # if previous timer was break change to work
            self.root.title(f"Work Timer 🍅")
            self.time_left = self.work_mins * 60 # set timer for work
            self.cycle_number += 1 # increment cycle number
            
        self.is_working = not self.is_working # change working flag to opposito, to alternate timers
        
        if self.cycle_number < self.cycles: # if number of cycles less than desired number continue running the timer
            if self.is_working:
                playsound(self.rel_path_to('sounds/SoulSteal.wav')) # play sound for work timer
            else:
                playsound(self.rel_path_to('sounds/DarkMeta.wav')) # play sound for break timer
            self.run_timer()
        else:
            self.root.geometry("300x200")
            self.play_sound_threaded(self.rel_path_to('sounds/Impressive.wav'))
            self.root.title(f"The end 🍅") # change title to end title
            self.timer_bg_og_resize = self.timer_bg_og.resize((260, 100), Image.LANCZOS) 
            self.timer_bg = ImageTk.PhotoImage(self.timer_bg_og_resize)
            self.timer_label.config(image=self.timer_bg, text="🍅 Finished! 🍅", font=self.font_timer)
            self.is_running = False 
    
    def stop_timer(self):
        self.play_sound_threaded(self.rel_path_to('sounds/What.wav')) # sound for stop button
        self.is_running = False # restarts the timer as well by setting flag to false
    
    def reset_timer(self):
        self.play_sound_threaded(self.rel_path_to('sounds/AsYouWish.wav'))
        self.root.title(f" My 🍅 Timer ")
        # Show input fields again
        self.work_label.pack(anchor=self.work_label_pack[0], padx=self.work_label_pack[1], pady=self.work_label_pack[2])
        self.work_entry.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.break_label.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.break_entry.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.cycle_label.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        self.cycle_entry.pack(anchor=self.pack_args[0], padx=self.pack_args[1], pady=self.pack_args[2])
        # Hide timer
        self.timer_label.place_forget() 
        self.root.geometry("") 
        self.is_running = False
        self.time_left = self.work_mins * 60 # reset to default
        self.cycle_number = 0 # reset to default
        self.timer_label['text'] = self.format_time(self.time_left) # reset to default
       
    def format_time(self, time_in_seconds): # formats time in minutes to int number of seconds in a string
        minutes, seconds = divmod(time_in_seconds, 60)
        return f"{int(minutes):02}:{int(seconds):02}"

    def play_sound_threaded(self, sound_file): # plays sound in a thread to keep GUI active
        threading.Thread(target=playsound, args=(sound_file,)).start()
    
    def rel_path_to(self, file):
            return os.path.join(self.base_path, file)


def main():
    root = tk.Tk() # creates tkinter object
    app = PomodoroApp(root)
    root.mainloop() # starts the App

if __name__ == "__main__":
    main()