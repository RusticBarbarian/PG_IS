import pyautogui as q
import webbrowser
import time

textbook = ["https://www.pearsonsuccessnet.com/snpapp/ois/getStudentHomepage.do?newServiceId=6000&newPageId=12100"]

classroom = ["https://classroom.google.com/u/1/c/NzUyNzc2OTEzOFpa"]

website = ["https://sites.google.com/a/gcds.net/spencer-history-8/homework-e-f-spring"]

login = ["https://www.google.com"]



login = q.prompt(
"""
Would you like to log in to your Gmail?

1) Yes
2) No 
"""
    )


answer = q.prompt(
    """
Do you need to acess
a) the textbook
b) the classroom
c) the website

"""
    )


if answer == "a":
    
   for i in textbook:
        webbrowser.open(i)
        
elif answer == "b":
    if login == "1":
       for i in login:
          webbrowser.open("https://www.google.com/")
    elif login == "2":
        for i in classroom:
            webbrowser.open(i) 

    
elif answer == "c":
    if login == "1":
       for i in login:
          webbrowser.open("https://www.google.com/")
    elif login == "2":
       for i in website:
        webbrowser.open(i)
        
time.sleep(9)
q.alert("Finished signing in?")

if answer == ("b"):
   for i in classroom:
      webbrowser.open(i)

elif answer == ("c"):
   for i in website:
      webbrowser.open(i)
