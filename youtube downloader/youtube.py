import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        YouTube_link = link.get()
        youtube_object = YouTube(YouTube_link)
        video = youtube_object.streams.get_highest_resolution()
        video.download()
    except:
        print("youtube link is invalid")
    print("download complete")

# ssystem setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# define app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("youtube downloader")

# adding ui elements
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(padx = 10, pady = 10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height= 40,textvariable=url_var)
link.pack()


#download button
download = customtkinter.CTkButton(app, text="download", command = startDownload) 
download.pack(padx = 10, pady =10)
app.mainloop()