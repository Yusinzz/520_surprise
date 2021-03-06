# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *


surprise = Tk()

# 設定邊界
surprise.geometry("300x200")
# 設定title
surprise.title('520解謎遊戲')
# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	
	while True:
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# 等一秒鐘
		time.sleep(1)

		# Get current time
		# current_time = datetime.datetime.now().strftime("%H:%M:%S")
		# print(current_time,set_alarm_time)

		# 確認是否有設定到520 
		if set_alarm_time == "5:2:0":
			print("嘟嘟我愛你")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

#加 Labels, Frame, Button, Optionmenus
Label(surprise,text="嘟嘟昂",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(surprise,text="請輸入通關密語",font=("Helvetica 15 bold")).pack()
#123
frame = Frame(surprise)
frame.pack()

hour = StringVar(surprise)
hours = ('0','1','2','3','4','5','6','7','8','9')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(surprise)
minutes = ('0','1','2','3','4','5','6','7','8','9')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(surprise)
seconds = ('0','1','2','3','4','5','6','7','8','9')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(surprise,text="說愛我",font=("Helvetica 15"),command=Threading).pack(pady=20)

# 執行
surprise.mainloop()
