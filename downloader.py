from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *


# Function to download video
def download_video():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()


# Function to get path
def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


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


# Path to download videos
path_label = Label(root, text="Select path to save video to: ", font=("Arial", 12))
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)


# Download button
download_button = Button(root, text="Download", font=("Arial", 12), command=download_video)
canvas.create_window(200, 250, window=download_button)

root.mainloop()