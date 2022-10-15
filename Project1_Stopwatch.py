from cgitb import reset
import tkinter as Tkinter
from datetime import datetime
from tracemalloc import stop, start

counter = 0
running = False

name = str(input("Enter Your Name: "))

def counterlabel(label):
    def count():
        if running:
            global counter
            if counter == 0:
                display = f"Welcome {name}"
                # before ::
                display = 'Ready!'
                # after ::
                display = '@osmanmuratgul'
                # and running ;
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display

            label.after(1000, count)
            counter += 1

    count()

def Start(label):
    global running
    running = True
    counterlabel(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
    
    
def Start(label):
    global running
    running = True
    counterlabel(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Reset(label):
    global counter
    counter = 0
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    else:
        label['text'] = '00:00:00'

root = Tkinter.Tk()
root.title("Stopwatch")
renk = input("RChoose Color(English): ")

root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='Ready!', fg=renk, font='Verdana 40 bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Ready', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Pause', width=6, state='disabled', command=stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()
