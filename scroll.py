import tkinter as tk

def on_scroll(event):
    print("Scrolling...")
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()
root.bind("<MouseWheel>", on_scroll)
root.mainloop()