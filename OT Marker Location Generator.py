import math
import sys

## Controls
spacing = 5

## Init Variables
songLocation = 0

## Script Start
minutesInput = input("Total Minutes? ")

try:
    minutes = int(minutesInput)
    seconds = int(input("Total Seconds? "))
except:
    try:
        minutes = int(math.floor(float(minutesInput)))
        seconds = int(math.floor((float(minutesInput)%1)*100))
    except:
        print("")
        print("--------------")
        print("Error on Input")
        print("Please type int or float only on prompt")
        print("Exiting")
        print("--------------")
        print("")
        sys.exit()

songLength = (minutes * 60) + seconds

## Triggers
actionMarkerId = " !_e09b49b56869964487d5db37808e0667"
stopActionMarker = " !1016"
endOfLine = " 0 1 0"

## Basic Addition Function using User's input
def addSongLength(time):
    time = (time + songLength)
    return (time)

def addSpacingLength(time):
    time =(time + spacing)
    return (time)

for i in range(1,17):
    location = str(i)
    tnumber = str(int(i/2+.5))
    tnumswitch = i%2

    if i == 16:
        print(location+" "+str(songLocation)+stopActionMarker+endOfLine)
    
    if tnumswitch == 1:
        print(location +" "+str(songLocation)+" "+'"Track '+ tnumber +' Audio"'+endOfLine)
        songLocation = addSongLength(songLocation) 
    
    if tnumswitch == 0:
        print(location+" "+str(songLocation)+actionMarkerId+endOfLine)
        songLocation = addSpacingLength(songLocation)
