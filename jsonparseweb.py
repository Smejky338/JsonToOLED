import json
import urllib
from luma.oled.device import sh1106
from luma.core.serial import spi
import RPi.GPIO as GPIO

serial = spi(device=0, port=0)
device = sh1106(serial)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #change pin?
GPIO.add_event_detect(24, GPIO.FALLING, callback=NextPage(), bouncetime=300) # VCC normal, GND pressed
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #change pin?
GPIO.add_event_detect(23, GPIO.FALLING, callback=PrevPage(), bouncetime=300) # VCC normal, GND pressed
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #change pin?
GPIO.add_event_detect(21, GPIO.FALLING, callback=LsDown(), bouncetime=300) # VCC normal, GND pressed
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #change pin?
GPIO.add_event_detect(20, GPIO.FALLING, callback=LsUp(), bouncetime=300) # VCC normal, GND pressed
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) #change pin?
GPIO.add_event_detect(19, GPIO.FALLING, callback=Select(), bouncetime=300) # VCC normal, GND pressed

pgnum=0
sel=0
jobs = load_web_jobs("http://10.34.3.55:8080/view/RHEL6/api/json")

#github.com/qery/qMenuSystem vzor

def Title(text):
  with canvas(device) as draw:
    draw.text(5, 0, text, fill="white")
    draw.rectangle((0,0, 128, 9), outline="white") #fill="black"

def Item(index, text, text2):
  with canvas(device) as draw:
    # draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((0, 10 + a * i * 11), text, fill="white")
    draw.text((98, 10 + b * i * 11), text2, fill="white")

def Highlight(index, text):
  with canvas(device) as draw:
    draw.rectangle((0, 8 + a * i * 11, 128, 19 + a * i * 11), fill="white")
    draw.text((0, 10 + a * i * 11), text, fill="black")
    draw.text((98, 10 + b * i * 11), text2, fill="black")

def DisplayPgNum():
  global pgnum
  with canvas(device) as draw:
    draw.text(60, 56, num, fill="white")


def NextPage():
  global num
  device.clear()
  if num+5<len(jobs):
    num=num+5
    print_jobs(jobs, num, len(jobs)-1)
def PrevPage():
  global num
  device.clear()
  if (num=num-5)<0:
    num = 0
  print_jobs(jobs, num, num+5)

def LsDown():
  global sel +=1
  #prepis Item a Highlight

def LsUp():
  global sel -=1
  # prepis Item a Highlight


def Select(): #on GPIO input
  #rozlisit jestli jsem v print menu nebo v jednotlivych seznamech jobu
  #odkaz na dle indexu highlightu v bocnim poli adres na jsony

  if ()

def print_menu(): # stranky predavat v parametru, ohlidat ne mimo rozsah, highlight reset na 1. pri nextpage,


open('rhel.json') as data_file:
  data = json.load(data_file)
  vysl=[]
  vysl.append([data['jobs'][i]['name'], data['jobs'][i]['color']])

def load_web_jobs(url):
  #nezkouseno, pro nacitani z URL
  url="http://10.34.3.55:8080/view/RHEL6/api/json"
  response=urllib.urlopen(url)
  data = json.loads(response.read())
  vysl = []
  for i in range(len(data['jobs'])):
    vysl.append([data['jobs'][i]['name'], data['jobs'][i]['color']])
  return vysl

def print_jobs(jobs, num, numend):
  #Item(jobs[i][1]) jobs[i][0]
  for i in range(num, numend):
    if ():
      Highlight()
    else:
      Item()

def print_scroll_jobs(jobs):
  with canvas(virtual) as draw:
    for i in range(num, num+5):
      draw.text((0, 10+a*i*11), jobs[i][0], fill="white")
      draw.text((98, 10+b*i*11), jobs[i][1], fill="white")

    # update the viewport one position to the right, causing a refresh,
    # giving a scroll effect to the left
    for x in range(128):
        virtual.position = (x, 0)
        time.sleep(0.05)

print len(data['jobs'])
for i in range(len(data['jobs'])):
        print(data['jobs'][i]['name'])
        print(data['jobs'][i]['color'])
except KeyboardInterrupt:
    GPIO.cleanup()