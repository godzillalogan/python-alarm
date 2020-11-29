import time
from playsound import playsound
from datetime import datetime
alarmtime =input("輸入XX(小時):YY(分鐘)")
while True:
    Icltime = datetime.now().strftime('%H:%M')
    if Icltime == alarmtime:
        print("幹~時間到了~~~~~要起床了~~~")

        print("播放","KONO DIO DA.mp3")
        playsound("KONO DIO DA.mp3")
        time.sleep(1)

        print("播放","ZA WARUDO.mp3")
        playsound("ZA WARUDO.mp3")
        time.sleep(1)

        print("播放","OLAOLA.mp3")
        playsound("OLAOLA.mp3")
        time.sleep(1)

        print("播放","OLAOLA.mp3")
        playsound("OLAOLA.mp3")
        #time.sleep(43)
        break
    else:
        print("還可以繼續睡喔~~~爽爽~~~還沒",alarmtime)
        time.sleep(10)