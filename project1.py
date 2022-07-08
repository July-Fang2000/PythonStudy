import time
import webbrowser

print("This program started on"+ time.ctime())
for i in range(3):
    time.sleep(2*60*60)
    webbrowser.open("https://learn-udacity.top/itpg172945/Intro%20to%20Programming/index.html")