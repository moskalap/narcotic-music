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
`
with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

    # degrees.append(random.randint(0,127))

    degrees.sort()
    # MIDI note number
    print(degrees)
    track = 0
    channel = 0
    time = 0  # In beats
    duration = 5  # In beats
    tempo = 120  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
    # automatically)
    MyMIDI.addTempo(track, time, tempo)
    for tracks in range(1, 5):
        for tacts in range(1, 20):
            for notes in range(1, 8):
                for i in range(1, 50):
                    for pitch in range(21, (tracks % 4) * 30, random.randint(1, 12)):
                        MyMIDI.addNote(track, channel, pitch, time + i, duration + tracks * i, volume)

    with open("major-scales.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)