import datetime
import time
import winsound


def alarm(Timing):
  altime = str(datetime.datetime.now().strftime(Timing,"%I:%M %p"))

altime = altime
print("altime")
Horeal = altime[:2]
Horeal = int(Horeal)
Mireal = altime[3:5]
Mireal = int(Mireal)
print(f"Done, alarm is set for {timing}")

while True:
       if Horeal==datetime.datetime.now().hour:
           if Mireal==datetime.datetime.now().minute:
               print("alarm is runing")
               winsound.PlaySound('abc',winsound.SND_LOOP)

           elif Mireal<datetime.datetime.now().minute:
               break   
           
           
