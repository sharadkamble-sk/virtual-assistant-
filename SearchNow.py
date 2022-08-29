
import webbrowser
import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
  
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
        print("Say that again please...")
        return "None"
    return query

query = takeCommand().lower()

engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voice', voices[1].id)
engin.setProperty('rate',220)


def speak(audio):
    engin.say(audio)
    print(audio)
    engin.runAndWait()
    
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is What i found in google")
      
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
            
        except:
            speak("No speakable output available")    
          
def searchYoutube(query):
        if "youtube" in query:
            speak("This is what i found for your search!")
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            query = query.replace("jarvis","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done sir")
            
    # def  searchWikipedia(query):
    #         if "wikipedia" in query:
    #             speak("Searching from wikipedia....")
    #             query = query.replace("wikipedia","")
    #             query = query.replace("search wikipedia","")
    #             query = query.replace("jarvis","")
    #             results = wikipedia.summary(query,sentences= 2)
    #             speak("According to wikipedia...")
    #             print(results)
    #             speak(results)
    
    
    

            
            
                