import tkinter as tk
import time


def display():
	currenttime=time.strftime("%H:%M:%S")
	clock["text"]=currenttime
	window.after(1000,display)


window=tk.Tk()
window.title("CLOCK")
clock=tk.Label(window,font="ariel 100 ",bg="black",fg="green")
clock.grid(row=0,column=0)
display()
window.mainloop()
