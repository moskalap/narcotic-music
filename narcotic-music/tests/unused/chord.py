import random
class Chord:
    notes = {'c': 24,
             'c#': 25,
             'd': 26,
             'd#': 27,
             'e': 28,
             'f': 29,
             'f#': 30,
             'g': 31,
             'g#': 32,
             'a': 33,
             'a#': 34,
             'b': 35,
             }
    chords = {
        "_M": [0, 4, 7],
        '_m': [0, 3, 7],
        '_dim': [0, 3, 7],
        '_M7': [0, 4, 11],
        '_M9': [0, 4, 11, 14],
        '_m7': [0, 3, 10],
        '_m9': [0, 3, 10, 14],
        '_m6': [0, 3, 9],
        '_7': [0, 4, 10],
        '_dim7': [0, 3, 9],
        '_sus': [0, 5, 7],
        '_6': [0, 4, 7, 9],
        '_6/9': [0, 4, 9, 14],
        '_+': [0, 4, 8]
    }
    instruments={
            'piano': [i for i in range(1, 9)],
            'percusion': [i for i in range(9, 18)],
            'organ': [i for i in range(17, 26)],
            'guitar': [i for i in range(25, 34)],
            'bass': [i for i in range(33, 42)],
            'strings': [i for i in range(41, 50)],
            'ensemble': [i for i in range(49, 58)],
            'brass': [i for i in range(57, 66)],
            'reed': [i for i in range(65, 74)],
            'pipe': [i for i in range(73, 82)],
            'lead': [i for i in range(81, 90)],
            'pad': [i for i in range(89, 98)],
            'effects': [i for i in range(97, 106)],
            'ethnic': [i for i in range(105, 114)],
            'percusive': [i for i in range(113, 122)],
            'seffects': [i for i in range(121, 129)]
        }
    chords_family={}
    scales={
        'a'
    }
    progresive={
        1:[1,2,3,4,5,6],
        2:[3,5],
        3:[2,4,6],
        4:[1,3,5,2],
        5:[1,6],
        6:[4,5,2]
    }

    def __init__(self):
        print("j")
        self.build_chord_family(self.notes, self.chords)
    def get_progression(self, note):
        scale=['d_M', 'd_m', 'f#_m', 'g_M', 'a_M', 'b_m']
        #scale=['c_M', 'd_m', 'e_m', 'f_M', 'g_M', 'a_m']

        index=scale.index(note)
        note=self.progresive[index+1]
        scale= scale[random.choice(note)-1]
        return scale

    def build_chord_family(self, notes, chords):
        for k in notes.keys():
            self.chords_family={k:{c:[notes[k]+j for j in chords[c]] for c in chords.keys()} for k in notes.keys()}

    def add_note(self, note, octave):
        self.notes.append(self.notes[note]+12*(octave-1))

    def get_notes(self):
        return self.notes
    def crate_note(self, note, octave, durationdelta, volume, dtime):
        note=note.split("_")
        return [self.chords_family[note[0]]['_'+note[1]], {'delta': octave, 'duration': durationdelta, 'volume': volume, 'dtime': dtime}]


