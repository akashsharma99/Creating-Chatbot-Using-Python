import speech_recognition as sr
import os
import sys
import re
import win32com.client as wincl
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib.request as ur
import json
from bs4 import BeautifulSoup as soup
import wikipedia
import random
from time import strftime
import random
###########################################################


def Response(audio):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(audio)


###########################################################
'''
def myCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
       # print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
       # print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        Response("Not able to hear it! Lets have another try")
        command = myCommand();
    return command

###############################################################

def fullfilment():
    Response("Is your requirement fullfiled yes or not ")
    command=myCommand()
    if 'yes' in command:
        flag=0
        Response("Thanks,good to hear")
    elif 'no' in command:
        Response("Continue Please, It's my duty to help")
        assistant(myCommand())
'''


def options(title_list):
    command = input("Enter which song,")  # command=myCommand()
    if 'first one' in command or 'first' in command:
        return (0)
    elif 'second one' in command or 'second' in command:
        return (1)
    elif 'third one' in command or 'third' in command:
        return (2)


########################################################################


def assistant():
    mysong = input("Name of the song: ")
    path = 'D:\Python_Download'
    if mysong:
        flag = 0
    url = "https://www.youtube.com/results?search_query=" + mysong.replace(
        ' ', '+')
    response = ur.urlopen(url)
    html = response.read()
    soup1 = soup(html, "lxml")
    url_list = []
    title_list = []
    href_v = []
    for vid in soup1.findAll(attrs={'class': 'yt-uix-tile-link'}):
        if ('https://www.youtube.com' +
                vid['href']).startswith("https://www.youtube.com/watch?v="):
            flag = 1
            final_url = 'https://www.youtube.com' + vid['href']
            url_list.append(final_url)
            title_list.append(vid['title'])
            href_v.append(vid['href'])
    str = ""
    shorted_list = title_list[0:3]
    print(len(shorted_list))
    #Response("Which one should i play")
    for ele in shorted_list:
        str += ele
        str += " . "
    print(str)
    # Response(str)
    title = options(title_list)
    ydl_opts = {}
    print(title)
    os.chdir(path)
    href = title_list[title].replace(
        "|", "_") + "-" + href_v[title][9:len(href_v[title])] + ".mp4"
    url = url_list[title]
    if os.path.isfile(os.path.join(path, href)):
        os.startfile(os.path.join(path, href))
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        os.startfile(os.path.join(path, href))


########################################################################
while True:
    assistant()
'''
def initial(command):
    if 'help' in command :
        Response('Hey, I am Nova,    Please give a command or say "help me" and I will tell you what all I can do for you.')
        assistant(myCommand())
'''
########################################################################
#   flag=1
#   while flag!=0:
#      fullfilment()

Response("Give Your Command Arkadip, I am listening")
assistant(myCommand())
