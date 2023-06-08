from tkinter import *
import tkinter as tk
from pytube import YouTube
import os
from tkinter import filedialog

class Downloader:

    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube Downloader")
        self.window.resizable(0, 0)
        self.window.geometry("1280x720+300+200")

        self.window.iconbitmap(".\assets\iconbitmap.ico")

        self.audio = False
        self.video = False

        self.img_logo = PhotoImage(file=".\assets\logo.png")

        self.frame = Frame(self.window, bg="#363636")
        self.frame.pack(fill="x")

        self.label_logo = Label(self.frame, image=self.img_logo, bg="#363636")
        self.label_logo.pack()

        self.framesearch = Frame(self.window, pady=20)
        self.framesearch.pack()

        self.label_insert = Label(self.framesearch, text="Cole o link aqui: ", font="arial 12")
        self.label_insert.pack(side="left")

        self.link = Entry(self.framesearch, font="arial 20", width=50)
        self.link.pack(side="left")

        self.play = Button(self.framesearch, bg="red", text="➔", bd=0, fg="white",
                           width=6, height=2, command=lambda: self.download(self.link.get())).pack()

        self.framebutton = Frame(self.window)
        self.framebutton.pack()

        self.radio1 = Radiobutton(self.framebutton, text="Áudio", value=0, command=self.validate_audio).pack(side="left")
        self.radio2 = Radiobutton(self.framebutton, text="Vídeo", value=1, command=self.validate_video).pack(side="left")
        self.radio2 = Radiobutton(self.framebutton, text="Áudio e Vídeo", value=2, command=self.validate_audio_video).pack(side="left")

        self.window.mainloop()

    def validate_audio(self):
        self.audio = True
        self.video = False

    def validate_video(self):
        self.audio = False
        self.video = True

    def validate_audio_video(self):
        self.audio = False
        self.video = False

    def download(self, link):
        pasta = filedialog.askdirectory()
        yt = YouTube(link)

        if self.audio:
            stream = yt.streams.get_audio_only()
        elif self.video:
            stream = yt.streams.filter(only_video=True).first()
        else:
            stream = yt.streams.get_highest_resolution()

        if stream:
            stream.download(output_path=pasta)
            print("Download concluído.")
        else:
            print("Não foi possível encontrar a melhor qualidade para download.")

Downloader()
