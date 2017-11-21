minutes = int(input("Total Minutes? "))
seconds = int(input("Total Seconds? "))
songLength = (minutes * 60) + seconds
spacing = 5
songLocation = 0
actionMarkerId = " !_e09b49b56869964487d5db37808e0667"
stopActionMarker = " !1016"
endOfLine = " 0 1 0"

##Basic Addition Fucntion using User's input
def addSongLength(time):
    time = (time + songLength)
    return (time)

def addSpacingLength(time):
    time =(time + spacing)
    return (time)

##Debugging
print "1 " + str(songLocation) + ' "Track 1 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "2 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "3 " + str(songLocation) + ' "Track 2 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "4 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "5 " + str(songLocation) + ' "Track 3 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "6 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "7 " + str(songLocation) + ' "Track 4 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "8 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "9 " + str(songLocation) + ' "Track 5 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "10 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "11 " + str(songLocation) + ' "Track 6 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "12 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "13 " + str(songLocation) + ' "Track 7 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "14 " + str(songLocation) + actionMarkerId + endOfLine
songLocation = addSpacingLength(songLocation)
print "15 " + str(songLocation) + ' "Track 8 Audio"' + endOfLine
songLocation = addSongLength(songLocation)
print "16 " + str(songLocation) + stopActionMarker + endOfLine
