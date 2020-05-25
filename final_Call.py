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
import urllib
import json
from bs4 import BeautifulSoup as soup
import wikipedia
import random
from time import strftime
###########################################################

def Response(audio):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(audio)

###########################################################

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

########################################################################

def assistant(command):
    if 'open' in command:
        text="Open command inserted"
        Response(text)
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            #print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            Response('The website you have requested has been opened for you.')
        #fullfilment()
    elif 'close' in command:
        Response("Goodbye Have a nice time")
        sys.exit()
    elif 'shutdown' in command:
        Response('Bye bye Sir. Have a nice day')
        sys.exit()
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            Response('Hello Arkadip. Good morning')
        elif 12 <= day_time < 18:
            Response('Hello Arkadip. Good afternoon')
        else:
            Response('Hello Arkadip. Good evening')
    elif 'help me' in command:
        Response("""
        You can use these commands and I'll help you out:
        1. Open reddit subreddit : Opens the subreddit in default browser.
        2. Open xyz.com : replace xyz with any website name
        3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
        4. Current weather in {cityname} : Tells you the current condition and temperture
        5. Hello
        6. play me a video : Plays song in your VLC media player
        7. change wallpaper : Change desktop wallpaper
        8. news for today : reads top news of today
        9. time : Current system time
        10. top stories from google news (RSS feeds)
        11. tell me about xyz : tells you about xyz
        """)
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            Response(str(res.json()['joke']))
        else:
            Response('oops!I ran out of jokes')

    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list[:15]:
                Response(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
        
    elif 'current weather' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            Response('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
            
    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        Response('Current time is %d hours %d minutes' % (now.hour, now.minute))
        
    elif 'email' in command:
        Response('Who is the recipient?')
        recipient = myCommand()
        if 'rajat' in recipient:
            Response('What should I say to him?')
            content = myCommand()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('your_email_address', 'your_password')
            mail.sendmail('sender_email', 'receiver_email', content)
            mail.close()
            Response('Email has been sent successfuly. You can check your inbox.')
        else:
            Response('I don\'t know what you mean!')
        
    elif 'launch' in command:
        reg_ex = re.search('launch (.*)', command)
        if reg_ex:
            #appname = reg_ex.group(1)
            #appname1 = appname+".exe"
            #subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
            os.system("start "+reg_ex.group(1)+":")
            Response('I have launched the desired application')
       # fullfilment()
        
    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                Response(ny.content[:500].encode('utf-8'))
        except Exception as e:
                Response(e)
    elif 'search' in command:
        url = 'https://www.google.com/search?q=' +command
        webbrowser.open(url)
        Response('The website you have requested has been opened for you.')
        #fullfilment()

########################################################################

'''
def initial(command):
    if 'help' in command :
        Response('Hey, I am Nova,    Please give a command or say "help me" and I will tell you what all I can do for you.')
        assistant(myCommand())
'''   
########################################################################

def call():
    assistant(myCommand())
 #   flag=1
 #   while flag!=0:
 #      fullfilment()


Response("Welcome, Arkadip")
call()  

