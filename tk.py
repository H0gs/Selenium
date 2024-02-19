import tkinter as tk
import time

window = tk.Tk()
frame = tk.Frame(master=window)
frameY = 0

# frame.pack(side="left")
frame.place(x=0, y=0)

window.size()
greeting = tk.Label(
    text="Hello, Tkinter", 
    width=30, 
    height=10, 
    fg="white", 
    bg="black",
    master=frame
)

def handle_click(event, te):
    print(te)
    print("The button was clicked!")

def button_callback(button_number):
    print(f"You clicked button {button_number}")

for i in range(20):    
    button = tk.Button(
        text="Click me!",
        width=10,
        height=5,
        bg="blue",
        fg="yellow",
        master=frame,
        command=lambda j=i: button_callback(j)
    )
    button.pack(side="top")
    
    # if(i < 3):
    #     button.pack(side="left")
    # else:
    #     button.pack(side="top")
    
    # button.bind("<Button-1>", lambda e="e": handle_click(e))

entry = tk.Entry()

entry.pack()
# greeting.pack() # When you pack a widget into a window, Tkinter sizes the window as small as it can be while still fully encompassing the widget. 
# text_box = tk.Text(width=20, height=20)
# text_box.pack()
# text_box.insert("1.0", "Hello")

def on_scroll(event):
    print("Scrolling...")


window.bind("<Button-4", on_scroll)
window.bind("<Button-5>", on_scroll)

# print(text_box.get(0.0))
# print(text_box.get(1.0, 1.3)) #1 is the line number, .0 or .3 is the char number in the line. Lines start at 1, characters at 0

greeting.pack()

def on_scroll(event):
    global frameY
    # print("Scrolling...")
    # canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    # print(frame.winfo_rootx(), frame.winfo_rooty())
    print(event.delta)
    frameY += event.delta/120
    frame.place(x=0, y=frameY)

canvas = tk.Canvas(window)
canvas.pack()
window.bind("<MouseWheel>", on_scroll)

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)


window.mainloop()
print("Script Ended Using X")