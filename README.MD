# Octatrack “Stems”
 
As far as I know there’s no way for Octatrack users to bounce their tracks as stems. I found an automated way of doing it. 
In this document I will explain how to setup everything you need to get this project working. I found the easiest way to accomplish 
this was using the Reaper DAW. Included with this fill will be a project template and a Custom Action file. I will also attach a link 
to a spreadsheet that I use to get my marker locations.
 
## So how does this work?

With the SWS/S&M extensions in Cockos Reaper, you are allowed to use something called Marker Actions. Marker Actions allow 
you to basically run shortcuts/actions. The other method that completes this all is Midi CC. 

All of the values I use in my example are default settings. If you need to adjust for your customized setup do so accordingly. 

### Install/Setup

Obviously you will need to install the Reaper Daw (http://reaper.fm) and SWS/S&M (http://www.sws-extension.org). Once you install 
those two pieces of software you will be ready to run with this next portion of the setup.

To explain this setup, I will give you a brief rundown. I made a custom action that steps through a couple actions. Currently it is 
setup to Transport:Stop>Wait 1 second>Go to next marker>Transport:Record. This action will allow to send transport start/stop commands to the 
Octatrack so you can automate restarting your song sequence. The 1 second wait is only in that command to make sure everything gets executed before 
it starts recording again. For the Mute/Unmute portion of the automation I’m using Midi CC. In the project file I’m attaching, there’s a track named 
“MIDI CC Control”. In that track there’s a midi file at specific locations that will mute/unmute the tracks accordingly. 

To setup the midi control make sure to open your preferences// Option>Preferences>Midi Devices. Enable output on whatever hardware you’re using 
to connect to the Octatrack midi In port. Turn off “Send Clock to output” and make sure you’re not sending “SPP to output”. Without getting into too much 
detail this is the setup I prefer. Disabling the SPP is highly important. Click ok and exit out of the preferences. 
	
Open the routing for the “MIDI CC Control” track and on Midi hardware output select whatever midi interface you’re using with the Octatrack. Make 
sure that the “Send to Original Channel” is selected. In the Octatrack you need to allow for it to receive transport and CC control. I DO NOT use any 
clock sync. If you want to test your setup go to the beginning of the track in reaper and press play. Track 1 should “Solo” and the track should start playing. 

Open the action list and import the custom action that I have attached. DO NOT create the custom action yourself. The Marker Actions 
rely on Action ID’s. The setup I have references my action id. It may work if you create it exactly but to make sure that there’s no problem just 
use my setup. While you’re in the action list search for “Marker Actions” click on “Enable Marker Actions” IDK if it’s enabled by default but it cannot 
hurt to click that action. 
	
### Running
Now you are ready to run the program. With everything set up and ready to go, click on your song sequence in your octatrack. Arm “OT Audio” track 
for recording. Click record. 

### Scripts
Python Script added to use the Copy Paste function of SWS marker Utility

Drake Champagne

