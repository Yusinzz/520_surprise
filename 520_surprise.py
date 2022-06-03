# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		# current_time = datetime.datetime.now().strftime("%H:%M:%S")
		# print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if set_alarm_time == "5:2:0":
			print("嘟嘟我愛你")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

# Add Labels, Frame, Button, Optionmenus
Label(root,text="嘟嘟昂",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="請輸入通關密語",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('0','1','2','3','4','5','6','7','8','9')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('0','1','2','3','4','5','6','7','8','9')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('0','1','2','3','4','5','6','7','8','9')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="說愛我",font=("Helvetica 15"),command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
