from tkinter import *
import os
from tkinter import filedialog
import yt_dlp

class Downloader:
    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube Downloader")
        self.window.resizable(0, 0)
        self.window.geometry("1280x720+300+200")
        self.window.iconbitmap("assets\\iconbitmap.ico")

        self.video = False

        self.img_logo = PhotoImage(file="assets\\logo.png")

        self.frame = Frame(self.window, bg="#363636")
        self.frame.pack(fill="x")

        self.label_logo = Label(self.frame, image=self.img_logo, bg="#363636")
        self.label_logo.pack()

        self.framesearch = Frame(self.window, pady=20)
        self.framesearch.pack()

        self.label_insert = Label(self.framesearch, text="LINK: ", font="arial 12")
        self.label_insert.pack(side="left")

        self.link = Entry(self.framesearch, font="arial 20", width=50)
        self.link.pack(side="left")

        self.play = Button(self.framesearch, bg="red", text=">", bd=0, fg="white",
                           width=6, height=2, command=lambda: self.download(self.link.get())).pack()

        self.window.mainloop()

    def download(self, link):
        pasta = filedialog.askdirectory()
        if pasta:
            ydl_opts = {
                'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(link, download=False)
                    title = info['title']
                    ydl.download([link])
                    print(f"Download de '{title}' concluído.")
                except yt_dlp.utils.DownloadError:
                    print("Não foi possível encontrar a melhor qualidade para download.")
                except yt_dlp.utils.ExtractorError:
                    print("Erro ao extrair informações do vídeo.")
                except yt_dlp.utils.SameFileError:
                    print("O arquivo já existe.")
                except yt_dlp.utils.UnsupportedError as e:
                    print(f"Formato não suportado: {e}")
                except yt_dlp.utils.DownloadError as e:
                    if 'Se não achar, certifique-se de que a URL é válida.' in str(e):
                        print("URL inválido. Certifique-se de que você inseriu um URL válido.")
                    elif 'Não é possível fazer o download da página da Web' in str(e):
                        print("Não foi possível baixar a página. Verifique sua conexão com a internet.")
                    else:
                        print("Erro durante o download do vídeo.")
                except Exception as e:
                    print(f"Erro desconhecido: {e}")
        else:
            print("Nenhum diretório selecionado.")

Downloader()
