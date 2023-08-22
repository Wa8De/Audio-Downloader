from youtube_dl import YoutubeDL

audioDownloader=YoutubeDL({format:'bestaudio'})

while True:
    try:
        print('Youtube Downloader'.center(40,'_'))
        URL=input('Enter URL : ')
        audioDownloader.extract_info(URL)
    except Exception:
        print("Couldn't Do it ")
    finally:
        option=int(input('\n1.Download again \n2. Exit\n\nOption here : '))
        if option!=1:
            break