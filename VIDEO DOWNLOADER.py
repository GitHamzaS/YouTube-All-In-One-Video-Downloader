# Write "pip install pytube" on Terminal without quotes

from pytube import Playlist, YouTube

def Video_Downloader():
    global press
    try:
        def press():
            if "playlist" in link1:
                pl = Playlist(link1)
                print("Playlist has found")
                print(f'Downloading : {pl.title}')
                print("Please Wait Videos are Downloading.... ")
                for video in pl.videos:
                    video.streams.get_highest_resolution().download()
                print("Successful Downloaded all Videos of the Playlist")
            else:
                youtube1 = YouTube(link1)
                print(f"Title : {youtube1.title}")

                Video_or_audio = input("What you want to Download, Audio or Video: ")
                Video_or_audio = Video_or_audio.lower()
                if Video_or_audio == "video":
                    video2 = input("Choose the option *** Auto *** or **** Manual Download **** : ")
                    video2 = video2.lower()
                    if video2 == "manual":
                        print("Please wait streams are loading....")
                        videos = youtube1.streams.all()
                        vid = list(enumerate(videos))
                        for i in vid:
                            print(i)

                        strm = int(input("Choose the starting number to Select the Quality e.g (10 : "))
                        print("File is downloading.....")
                        videos[strm].download()
                        print("Successfully Downloaded")

                    elif video2 == "auto":
                        print("Please wait file is downloading....")
                        video_quality = youtube1.streams.get_highest_resolution()
                        video_quality.download()
                        print("Successfully Downloaded")
                    else:
                        print("Please Choose the right one")


                elif Video_or_audio == "audio":
                    print("Please wait audio streams are loading....")
                    audios = youtube1.streams.filter(only_audio=True)
                    aud = list(enumerate(audios))
                    for i in aud:
                        print(i)

                    strm = int(input("Choose the starting number to Select the Quality e.g (3 : "))
                    print("File is downloading.....")
                    audios[strm].download()
                    print("Successfully Downloaded")
                else:
                    print("please choose the right one")
                    print(press())

    except Exception as e:
        print("Something went wrong, please choose the right link and try again")

    link1 = input("Enter youTube Link: ")
    print(press())

    loop = input("Do you want to download another YouTube video (Yes) or (No): ")
    loop = loop.lower()
    if loop == "yes":
        print(Video_Downloader())
    else:
        exit()

(Video_Downloader())