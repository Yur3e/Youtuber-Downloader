# **Youtube Downloader**

Este é um projeto simples de um aplicativo de download de vídeos do YouTube desenvolvido em Python usando a biblioteca tkinter para criar a interface gráfica e a biblioteca pytube para lidar com a funcionalidade de download.


![YoutubeDownloaderv1 0 1](https://github.com/Yur3e/Youtuber-Downloader/assets/88630655/13b264f8-b70c-4391-a6e9-9332bbec784f)


## **OBS:** O código teve de ser remodelado por conta das mudanças realizadas pelo Youtube em seu próprio algoritmo.


## **Funcionalidades**

O aplicativo permite que o usuário cole um link de vídeo do YouTube e selecione se deseja baixar apenas o áudio, apenas o vídeo ou ambos. O usuário também pode escolher o diretório de destino para salvar o arquivo baixado.


## **Requisitos**

- Python 3.x
- Bibliotecas:
 -- tkinter
 -- yt-dlp
 -- filedialog
 -- os

## **Como executar o projeto:**
### 1. Certifique-se de ter o Python 3.x instalado em seu sistema.
### 2. Clone ou baixe este repositório.
### 3. Clone o repositório do projeto:
  ```git clone <URL_DO_REPOSITÓRIO>```
### 4. Navegue até o diretório do projeto:
  ```cd youtube-downloader```
### 5. Execute o arquivo main.py:
  ```python main.py```
### 6. O aplicativo será iniciado e você poderá colar o link do vídeo do YouTube e selecionar as opções de download.

## **Notas adicionais**

- Certifique-se de ter uma conexão estável com a internet para que o aplicativo possa acessar os vídeos do YouTube.

- O aplicativo usa a biblioteca filedialog do tkinter para abrir uma janela de seleção de diretório para o usuário escolher o local de destino do download. Portanto, o aplicativo pode não funcionar corretamente em sistemas operacionais que não suportam essa funcionalidade.

- Caso esteja tendo erro para baixar os vídeos, tente instalar o FFMPEG e por no Path, para mais informações acesse: (www.ffmpeg.org/download.html#build-windows)

Sinta-se à vontade para contribuir para este projeto ou adaptá-lo às suas necessidades.
