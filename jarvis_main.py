

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
import smtplib
import pywhatkit as pwt
import requests
import pyautogui  

 
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
    strTime = datetime.datetime.now().strftime("%H:%M")
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
        speak(f"Sir, the time is {strTime}")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
        speak(f"Sir, the time is {strTime}")
    else:
        speak("Good Evening sir!")
        speak(f"Sir, the time is {strTime}")

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

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com,587')
#     server.ehlo()
#     server.starttls()
#     server.login('yours email','pass')
#     server.close()



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

        query = takeCommand().lower()
        if "set alarm" in query:  
            from alarm import alarm
            alarm()

        
                
                    
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
            
       
            
        elif 'open Facebook' in query:
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
            
        elif "send whatsapp message" in query:  
            pwt.sendwhatmsg("+919588415360","this is testing protocol",0 ,2 )   
             
             
        # elif 'open camera' or 'webcam' in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        #     cap.release()
        #     cv2.destroyAllWindows()    
            
        elif "ip address" in query:
              ip = get('https://api.ipify.org').text  
              speak(f"sir your IP address is {ip}")
         
        elif "temperature in" in query:    
            Temperature() 
        elif "temperature" in query:
              IP_Address = get('https://api.ipify.org').text
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
                to = "enter sender mail id"
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send ")
                
        elif "send whatsapp messag" in query:
            pwt.sendwhatmsg("+9588415360","hello")
                   
                
                                
        #      # Download the helper library from https://www.twilio.com/docs/python/install
             
        # elif "send message" in query:
        #         import os
        #         from twilio.rest import Client


        #         # Find your Account SID and Auth Token at twilio.com/console
        #         # and set the environment variables. See http://twil.io/secure
        #         account_sid = os.environ['ACb2a03da59675d0c0f2d8c1d8ab3d300f']
        #         auth_token = os.environ['9faa98948d1a483022f1b200ca35acd3']
        #         client = Client(account_sid, auth_token)

        #         message = client.messages \
        #             .create(
        #                 body='This text message is from your friend sharad for a testing purpose',
        #                 from_='+18158624742',
        #                 to='+917030327453'
        #             )
        #         print(message.sid)    
             
    # # Import modules
    #             import smtplib, ssl

    #             # Please replace below with your email address and password
    #             email_from = 'sender_email@gmail.com'
    #             password = 'xxx'
    #             email_to = 'receiver_email@gmail.com'

    #             # Plain Text string as the email message
    #             email_string = 'This is a test email sent by Python.'

    #             # Connect to the Gmail SMTP server and Send Email
    #             # Create a secure default settings context
    #             context = ssl.create_default_context()
    #             # Connect to Gmail's SMTP Outgoing Mail server with such context
    #             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #                 # Provide Gmail's login information
    #                 server.login(email_from, password)
    #                 # Send mail with from_addr, to_addrs, msg, which were set up as variables above
    #                 server.sendmail(email_from, email_to, email_string)
                                    
                
        # elif "how much power left" in query or "how much power we have" or "battery" in query:
        #     import psutil
        #     battery = psutil.sensors_battery()
        #     percentage = battery.percent
        #     speak(f"sir our system have {percentage} percentage battery")   
        #     break
        
        # elif 'current' in query:

        #         # g = geocoder.ip('me')
        #         # self.speak(g.latlng)

        #         send_url = "http://api.ipstack.com/check?access_key=7da92f317c51e1d9f8da7290b9bb4f84"
        #         geo_req = requests.get(send_url)
        #         geo_json = json.loads(geo_req.text)
        #         lat = geo_json['latitude']
        #         long = geo_json['longitude']
        #         city = geo_json['city']
        #         query.speak("Your location is in ")
        #         query.speak(city)
        #         print(city)
        #         webbrowser.open("https://www.google.nl/maps/place/" + city + "")
        #         # print(lat)
        #         # print(long)
        #         query.speak(lat)
        #         query.speak(long)
        #         query.sleep(5)   
        
        elif "where i am" in query:
            speak("wait sir, let me check")   
            try:
                op = "https://goo.gl/maps/sYZjV2QXCsNy4oDX8"
                webbrowser.open(op)
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure but i think we are in {city} of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are")
                pass
        

        elif "volume up" in query:
            pyautogui.press("volumeup")
            
        elif "volume down" in query:
            pyautogui.press("volumedown")    
        
        elif "volume mute" in query:
            pyautogui.press("volumemute")         
            
       
        elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com")
                speak("Here are some news...")
                time.sleep(5)
              
              
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)      
              
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
            speak(f"sir it's {strTime}")
            speak("I am ready sir, please tell me what can i do for you?")   
                  
        elif 'go to sleep' in query:
            speak("Ok sir, you can Call Me Anytime")
            break
        elif 'good job' in query:
          speak("thank you sir, i am always there for you sir")

            
