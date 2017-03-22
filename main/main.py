import random


from midiutil.MidiFile3 import MIDIFile
def get_pitch(note, octave):
    return{
        'a':21,
        'b':23,
        'c':24,
        'd':26,
        'e':28,
        'f':29,
        'g':31
    }[note]+12*octave

def add_note(note, octave, variation):
    return{
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': []

    }




track = 0
channel = 0
time = 0  # In beats
duration = 10  # In beats
tempo = 120  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
    # automatically)
MyMIDI.addTempo(track, time, tempo)

MyMIDI.addNote(track, channel, get_pitch('c', 3), time+4, duration, volume)
MyMIDI.addNote(track, channel, get_pitch('c', 2), time+3, duration, volume)
MyMIDI.addNote(track, channel, get_pitch('e', 3), time+2, duration, volume)
MyMIDI.addNote(track, channel, get_pitch('g', 3), time+1, duration, volume)
time=5
MyMIDI.addNote(track, channel, get_pitch('c', 3), time+1, duration, volume)
MyMIDI.addNote(track, channel, get_pitch('a', 2), time+2, duration, volume)
MyMIDI.addNote(track, channel, get_pitch('f', 3), time+3, duration, volume)
MyMIDI.addNote(track, channel, get_pitch('b', 3), time+4, duration, volume)

with open("major-scales.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)







