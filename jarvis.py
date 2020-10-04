import pyttsx3  # use to convert text into speech (pip install pyttsx3)
import datetime
import speech_recognition as sr  # use to recognize the speech (pip install SpeechRecognition)
import wikipedia  # (pip install wikipedia)
import smtplib  # inbuild library use to have feature of sending emails
import webbrowser as wb  # for using a brower in our code
import os  # for using the shutdown,restart,logout functionality in our program
import pyautogui # for using the srnshot feature (pip install pyautogui)
import psutil # use for all features like cpu utilization,battery check etc..(pip install psutil)
import pyjokes # use to get the jokes from internet(pip install pyjokes)


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def jokes():
    speak(pyjokes.get_joke())
    #print(pyjokes.get_joke())


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("thank you for asking mam")
    speak("The current time is:")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("thank you for asking mam")
    speak("The current date is:")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning mam!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon mam!")
    elif hour >= 18 and hour < 24:
        speak("Good evening mam!")
    else:
        speak("Good night mam!")
    speak("I,Doreamon,am here to help you. please tell me how can i help you?")


def tkcmd():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(s)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('poonam031999@gmail.com', 'Poonam@123')
    server.sendmail('poonam031999@gmail.com', to, content)
    server.close()

def scrnshot():
    img = pyautogui.screenshot()
    img.save("D:\JARVIS\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

if __name__ == '__main__':
    wishme()
    while True:
        query = tkcmd().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'quit' in query:
            speak("Thank you for using my service!")
            quit()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = tkcmd()
                to = 'poonam031999@gmail.com'
                # sendEmail(to,content)
                speak("email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("sorry!email has not been sent.")
        elif 'chrome' in query:
            speak("what should i search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            wb.register('chrome', None, wb.BackgroundBrowser(chromepath))
            search = tkcmd().lower()
            wb.get('chrome').open_new_tab(search + '.com')
            # wb.get(chromepath).open_new_tab(search +'.com')
        elif 'logout' in query:
            os.sytem("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'songs' in query:
            song_dir = "C:\\Users\\hp\\Music"
            song = os.listdir(song_dir)
            speak("thank you for asking mam,here we go!")
            os.startfile(os.path.join(song_dir, song[0]))
        elif 'remember' in query:
            speak("What should i remember?")
            data = tkcmd()
            speak("You ask me to remember that"+data)
            rem = open("data.txt",'w')
            rem.write(data)
            rem.close()
        elif 'know anything' in query:
            rem = open("data.txt",'r')
            speak("you said me to remember that"+rem.read())
        elif 'screenshot' in query:
            scrnshot()
            speak("done!")
        elif 'cpu' in query:
            cpu()
        elif 'battery' in query:
            cpu()
        elif 'joke' in query:
            jokes()



