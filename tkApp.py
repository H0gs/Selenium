import tkinter as Tk
# from tkinter import *
from PIL import ImageTk, Image
from testajr import getSongs
from selenium.common.exceptions import WebDriverException

window = Tk.Tk()
window.geometry("500x500")
frame = Tk.Frame(master=window)
frame.propagate(False)

gridFrame = Tk.Frame(master=window)

scrollOffSet = 0
paused = False

buttons = []

playlists = []

playlistData = open("playlists.txt", "r", errors="ignore")
for line in playlistData:
    playlist = []
    artist = line.strip().split(" /-\/-\ ")[0]
    type = line.strip().split(" /-\/-\ ")[1]
    line = line.replace(artist, "", 1)
    line = line.replace(type, "", 1)
    playlist.append(artist)
    playlist.append(type)

    print(artist, type)

    # line = line.replace(line.strip().split(" /-\/-\ ")[0], "", 1)
    # line = line.replace(line.strip().split(" /-\/-\ ")[1], "", 1)
    line = line.replace(" /-\/-\ ", "")
    songsList = []
    for data in line.split("}, "):
        dataDict = {}
        data = data.replace("{", "")
        data = data.replace("}", "")
        data = data.replace("]", "")
        for item in data.split(", '"):
            item = item.replace("'", "")
            item = item.replace('"', "")
            # print(item)
            if(item.split(":")[0] == "lengthInSeconds"):
                dataDict[item.split(":")[0]] = int(item.split(": ")[1].strip())
            else:
                dataDict[item.split(":")[0]] = item.split(": ")[1].strip()
        # print(data)

        songsList.append(dataDict)
        # print(dataDict)
    # print(songsList)
    playlist.append(songsList)
    playlists.append(playlist)

# print(playlists)

playlistData.close()



def searchArtist():
    shouldSearch = True
    for playlist in playlists:
        if(playlist[0].lower() == searchbox.get().lower()):
            print(playlist[2])
            shouldSearch = False
    if(shouldSearch):
        
        print(searchbox.get())
        search.config(text="Building Playlist...")
        search.update()
        try:
            playlist = getSongs(searchbox.get())
            if(playlist != []):
                # print(getSongs(searchbox.get()))
                search.config(text="Playlist Built!")
                playlistData = open("playlists.txt", "a")
                # playlistData.write(searchbox.get() + " /-\/-\ " "Artist" + " /-\/-\ " + str(playlist) + "\n")
                playlistData.write(searchbox.get() + " /-\/-\ " "Artist" + " /-\/-\ ")
                for char in str(playlist):
                    try:
                        playlistData.write(char)
                    except UnicodeError:
                        pass
                playlistData.write("\n")
                playlistData.close()
            else:
                search.config(text="Artist Not Found") 
        except WebDriverException as e:
            search.config(text="Internet Error")
            print(e)

def printParent(event, index):
    print(f"({event.x}, {event.y}), {buttons.index(event.widget)}")


def on_configure(event):
    print("Configured")

def changeImage():
    global paused
    if(paused):
        img2 = ImageTk.PhotoImage(Image.open("play.png"))
        play.configure(image=img2)
        play.image = img2
    else:
        img2 = ImageTk.PhotoImage(Image.open("pause.png"))
        play.configure(image=img2)
        play.image = img2
    paused = not paused
    # print(paused)

def makePlaylistIcons():
    for playlist in playlists:
        print()
    playImg = ImageTk.PhotoImage(Image.open("play.png"))
    button = Tk.Button(text=f"Button {i}")
    print(button.winfo_height())
    button.place(x=0, y=button.winfo_height() * i)
    button.place()
    button.bind("<Button-1>", lambda event, index=i: printParent(event, index))
    buttons.append(button)

for i in range(5):
    button = Tk.Button(text=f"Button {i}")
    print(button.winfo_height())
    button.place(x=0, y=button.winfo_height() * i)
    button.place()
    button.bind("<Button-1>", lambda event, index=i: printParent(event, index))
    buttons.append(button)

window.update() # Needs to be called so that you can get winfo_height() of widgets. \/
for i in range(len(buttons)):
    buttons[i].place(x=0, y=button.winfo_height() * i, anchor="nw")

hi = Tk.Label(text="Hello World!", master=gridFrame, fg="green", bg="blue")
playImg = ImageTk.PhotoImage(Image.open("play.png"))
play = Tk.Label(window, image = playImg)
play.place(relx = 0.5, rely = 0.85, anchor="center")
play.bind("<Button-1>", lambda event: changeImage())

nextImg = ImageTk.PhotoImage(Image.open("skip.png"))
next = Tk.Label(window, image=nextImg)
next.place(relx=0.63, rely=0.85, anchor="center")

backImg = ImageTk.PhotoImage(Image.open("back.png"))
back = Tk.Label(window, image=backImg)
back.place(relx=0.37, rely=0.85, anchor="center")


hi.grid(row=0, column = 0, sticky="n")
hi.bind("<Button-1>", lambda event: print("E"))
frame.pack(fill=Tk.BOTH, expand=True, side="left")
gridFrame.pack(side="right")
search = Tk.Button(window, text='Search Artist')
search.place(relx=0.5, rely=0, anchor="n")
search.bind("<Button-1>", lambda event: searchArtist())

searchbox = Tk.Entry()
searchbox.place(relx=0.5, rely=0.1, anchor="center")

print(window.winfo_height())

def on_scroll(event):
    global scrollOffSet
    if(event.x < buttons[0].winfo_width()): #Doesn't need to add an x value because its just 0
        if(buttons[0].winfo_y() + buttons[0].winfo_height() < window.winfo_height() and event.delta > 0) or (buttons[-1].winfo_y() > 0 and event.delta < 0):
            scrollOffSet += event.delta/120 * 3
            for i in range(len(buttons)):
                buttons[i].place(x=0, y=button.winfo_height() * i + scrollOffSet)
            # print(searchbox.get())


window.bind("<MouseWheel>", on_scroll)
window.bind("<Return>", lambda event: changeImage())

# window.bind('<Configure>', on_configure)
window.mainloop()