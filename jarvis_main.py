
from importlib.resources import contents
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
from requests import get
import requests
from bs4 import BeautifulSoup
import pywhatkit


 
 
# sapi5 it is used to get the voices microsoft speeech
engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
# print(voices[1].id)
engin.setProperty('voice', voices[1].id)
engin.setProperty('rate',220)


def speak(audio):
    engin.say(audio)
    print(audio)
    engin.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening sir!")

    speak("I am your virtual assistant. Please tell me how may i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
   
    wishMe()
    
    while True:
        # if 1:
        query = takeCommand().lower()
        if "google" in query:     
        # Searching from Web     
            # webbrowser.register('chrome', None)
            # webbrowser.open("https://www.google.com")
            # speak("Okay sir, google is opening")
            from SearchNow import searchGoogle
            searchGoogle(query)
     
                
                    
        elif 'youtube' in query:
            # webbrowser.register('chrome', None)
            # webbrowser.open("https://www.youtube.com")
            # speak("Okay sir youtube is opening")
            speak("This is what i found for your search!")
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            query = query.replace("jarvis","")
            web = "https://www.youtube.com/results?search_query=" + query
            # webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done sir")
            
            # from SearchNow import SearchYoutube   
            # SearchYoutube(query)
        
        elif 'wikipedia' in query:
            # speak('Searching Wikipedia...')
            # query = query.replace("wikipedia", "")
            # results = wikipedia.summary(query, sentences=2)
            # speak("According to Wikipedia")
            # print(results)
            # speak(results)  
            # from SearchNow import searchGoogle
            # searchwikipedia(query)  
                speak("Searching from wikipedia....")
                query = query.replace("wikipedia","")
                query = query.replace("search wikipedia","")
                query = query.replace("jarvis","")
                results = wikipedia.summary(query,sentences= 1)
                speak("According to wikipedia...")
                # print(results)
                speak(results)
            
            
            
        elif 'open facebook' in query:
            webbrowser.register('chrome', None)
            webbrowser.open("https://www.facebook.com")
            speak("Okay sir, facebook is opening")
            
      
        elif 'open whatsapp' in query:
            webbrowser.register('chrome', None)
            webbrowser.open("https://www.whatsapp.com")  
            speak("Okay sir what'sapp is opening")
        
        elif 'close chrome' in query:    
         os.system("taskkill /im chrome.exe /f")
             
        elif 'play music' in query:
            music_dir = 'D:\\Music\\Favorite song'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open notepad' in query:    
            speak("Okay sir, notepad is opening")
            os.system("start notepad")
            
                 
            
        elif 'close notepad' in query:      
            speak("Okay sir")
            os.system("taskkill /im notepad.exe /f")  
            speak("Notepad closed")
        
        elif 'close notepad' in query:      
            speak("Okay sir")
            os.system("taskkill /im notepad.exe /f")  
            speak("Notepad closed")
            
        elif "send what'sapp message" in query:  
            kit.sendwhatmsg("9588415360","this is testing protocol",2,24)   
             
             
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()    
        elif "ip address" in query:
              ip = get('https://api.ipify.org').text  
              speak(f"sir your IP address is {ip}")
         
        elif "temperature in" in query:    
            Temperature() 
        elif "temperature" in query:
              search = "temperature"
              url = f"https://www.google.com/search?q={search}"
              r = requests.get(url)
              data = BeautifulSoup(r.text,"html.parser")
              temp = data.find("div",class_="BNeawe").text
              speak(f"current {search} is {temp}")
      
        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand().lower()
                to = "kamblemansing101@gmail.com"
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send ")
                
                
              
              
              
              
              
        #conversations  
        
 
        elif "hello" in query:
            speak("Hello sir, How are you?")
            
        elif "i am fine" in query:
            speak("that's great, sir") 
            
        elif "how are you" in query:
            speak("I am Fine sir, thanks for asking")    
            
        elif "thank you" in query:
            speak("you are welcome, sir")   
            
        elif "wake up" in query:
            
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"it's {strTime}")
            speak("I am ready sir, please tell me what can i do for you?")   
                  
        elif 'go to sleep' in query:
            speak("Ok sir, you can Call Me Anytime")
            break
        elif 'good job' in query:
          speak("thank you sir, i am always there for you sir")

            
