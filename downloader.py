from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def download_video():
    """
    Downloads a video from the provided URL and converts it to an MP3 audio file.

    This function retrieves the video URL from the entry field, downloads the video
    in the highest resolution, extracts the audio, and saves both the video and audio
    files to the specified directory.
    """
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading video...")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)

    # Code for mp3 conversion
    audio_file = video_clip.audio_file
    audio_file.write_audiofile("audio.mp3")
    audio_file.close()
    shutil.move("audio.mp3", file_path)

    video_clip.close()
    shutil.move(mp4, file_path)
    print("Download complete!")


def get_path():
    """
    Opens a dialog for the user to select a directory to save downloaded files.

    This function updates the path_label with the selected directory path.
    """
    path = filedialog.askdirectory()
    path_label.config(text=path)


root = Tk()
root.title("Video Downloader")


canvas = Canvas(root, height=300, width=400)
canvas.pack()

# App label
app_label = Label(root, text="Video Downloader", fg='blue', font=("Arial", 20))
canvas.create_window(200, 20, window=app_label)


# Entry to accept video URL
url_label = Label(root, text="Enter video URL: ", font=("Arial", 12))
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)


# Path to download videos
path_label = Label(root, text="Select where to save video to: ", font=("Arial", 12))
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)


# Download button
download_button = Button(root, text="Download", font=("Arial", 12), command=download_video)
canvas.create_window(200, 250, window=download_button)

root.mainloop()
