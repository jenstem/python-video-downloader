from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Video Downloader")


canvas = Canvas(root, height=300, width=400)
canvas.pack()

# App label
app_label = Label(root, text="Video Downloader", fg="blue", font=("Arial", 20))
canvas.create_window(200, 20, window=app_label)


# Entry to accept video URL
url_label = Label(root, text="Enter video URL: ", font=("Arial", 12))
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)



root.mainloop()