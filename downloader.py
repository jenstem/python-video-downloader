from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Video Downloader")


canvas = Canvas(root, height=300, width=400)
canvas.pack()

# App label
app_label = Label(root, text="Video Downloader", fg="blue", font=("Arial", 20))
canvas.create_window(200, 20, window=app_label)


root.mainloop()