import speech_recognition as sr
import webbrowser
import pyttsx3
# import whisper
import musicLibrary as ml
import feedparser
import os
# import openai
recognizer = sr.Recognizer()
engine=pyttsx3.init()
def chat_with_gpt(prompt):
    return "I'm sorry, I cannot respond right now. My brain is offline due to quota limits."
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    print(c)
    if c.startswith("open"):
        if " google" in c.lower():
            webbrowser.open("https://google.com")
        elif "youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "chat gpt" in c.lower():
             webbrowser.open("https://chatgpt.com")
        elif "chrome" in c.lower():
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
        elif "brave" in c.lower():
            os.startfile("C:\Program Files\BraveSoftware\Brave-Browser\Application")
    elif c.lower().startswith("play"):
        l=c.lower().split()
        if len(l)==2:
            song=l[1]
            link1=ml.music[song]
            webbrowser.open(link1)
        elif len(l)==3:
            l1=[]
            l1.append(l[1])
            l1.append(l[2])
            st1="".join(l1)
            link2=ml.music[st1]
            webbrowser.open(link2)
        else:
            l2=[]
            for i in range(1,len(l)):
                l2.append(l[i])
            st2="".join(l2)
            link3=ml.music[st2]
            webbrowser.open(link3)
    elif "news" in c.lower():
        headlines = get_indian_news()
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}") 
            speak(headline)
            
    else:
        chat_with_gpt(c)


def get_indian_news():
    feed_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    news_feed = feedparser.parse(feed_url)

    headlines = [entry.title for entry in news_feed.entries[:5]]  # top 5
    return headlines

if __name__=="__main__":
    speak("Initializing jarvis... ")
    while True:
        r=sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("listening...") #1st time hearing word(wake)
                audio=r.listen(source,timeout=4,phrase_time_limit=2)
                # with open("test.wav", "wb") as f:
                #      f.write(audio.get_wav_data())

            word=r.recognize_google(audio)
            if word.lower()=="jarvis":
                print("Jarvis active...")
                speak("yes") #jarvis responding
                with sr.Microphone() as source:
                    print("listening...") #hearing main word
                    audio=r.listen(source,timeout=5,phrase_time_limit=1)
                command=r.recognize_google(audio)
                processcommand(command)
                    
            print("recognizing...")
            print(word)

        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Error {}".format(e))



