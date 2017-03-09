import random

from midiutil.MidiFile3 import MIDIFile

degrees  = [random.randint(0,100)]

for i in range  (0,100):
    degrees.append(random.randint(30,100))
degrees.sort()
# MIDI note number
print (degrees)
track    = 0
channel  = 0
time     = 0    # In beats
duration = 15    # In beats
tempo    = 160   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)