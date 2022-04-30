#alarm clock
from datetime import datetime
from playsound import playsound

alarm_tm = input("Enter the time: ")
alarm_hr = alarm_tm[0:2]
alarm_min = alarm_tm[3:5]
alarm_sec = alarm_tm[6:8]
alarm_prd = alarm_tm[9:11].upper()
print("Setting up alarm...")

while True:
    now = datetime.now()
    current_hr = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_prd == current_period):
        if(alarm_hr == current_hr):
            if(alarm_min == current_min):
                if(alarm_sec == current_sec):
                    print("Wakw up!...")
                    playsound("D:\31 oct song\Skylar_Grey_-_I'm_coming_home_(Lyrics)(256k).mp3")
                    break
                    
