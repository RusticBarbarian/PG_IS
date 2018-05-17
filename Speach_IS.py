import win32com.client as win
import pyautogui as q
import webbrowser as w


speak = win.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name?")
answer = q.prompt("Enter your name.")

if answer == "Isaac":
    speak.Speak ("Hello " + answer + " nice to meet you.")

elif answer == "Vaughn":
    speak.Speak ("Nice headband")

else:
    speak.Speak("Hi there, what are you doing on this computer?")

speak.Speak("What is your favorite sport?")
sport = q.prompt("Enter your favorite sport.")

if sport == "Basketball":
    speak.Speak ("I hope you are a Celtics fan, otherwise you are about to be sad.")
    w.open("https://www.youtube.com/watch?v=o17Tqa9Z0QE")

else:
    speak.Speak ("Nice, that is a good choice!")
    w.open("https://www.youtube.com/results?search_query="+sport)


