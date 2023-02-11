#download video from YouTube.com in folder "C:/Users/user/PycharmProject6/"

from pytube import YouTube

link = input('Enter your link on video: ')
video = YouTube(link)
quality = input('Choose High/Low: ')
if quality == 'High':
    output = video.streams.get_highest_resolution()
elif quality == 'Low':
    output = video.streams.get_lowest_resolution()
else:
    print("I don't know this command! Please check your message! It must be Low or High")

output.download()

#!!!!!import "pytube" in PyCharm or install it on ur pc!!!!!
