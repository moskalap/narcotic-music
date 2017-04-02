


class Note:
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
    notes_by_pitch = {
        24: 'c',
        25: 'c#',
        26: 'd',
        27: 'd#',
        28: 'e',
        29: 'f',
        30: 'f#',
        31: 'g',
        32: 'g#',
        33: 'a',
        34: 'a#',
        35: 'b'

    }
    keys = {'c': 'c d e f g a b'.split(),
            'c#': 'c# d# e f# g# a# b'.split(),
            'd': 'd e f# g a b c#'.split(),
            'e': 'e f# g# a b c# d#'.split(),
            'f#': 'f# g# a# b c# d# e'.split(),
            'g': 'g a b c d e f#'.split(),
            'a': 'a b c# d e f# g#'.split(),
            'b': 'b c# d# e f# g# a#'.split()

            }

    @staticmethod
    def get_pitch_static(note, octave):
        return {'c': 24,
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
                }[note] + 12 * octave

    @staticmethod
    def get_possible_notes(key):
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
        keys = {'c': 'c d e f g a b'.split(),
                'c#': 'c# d# e f# g# a# b'.split(),
                'd': 'd e f# g a b c#'.split(),
                'e': 'e f# g# a b c# d#'.split(),
                'f#': 'f# g# a# b c# d# e'.split(),
                'g': 'g a b c d e f#'.split(),
                'a': 'a b c# d e f# g#'.split(),
                'b': 'b c# d# e f# g# a#'.split()

                }
        l = []
        for octave in range(0, 6):
            t = [notes[n] + 12 * octave for n in keys[key]]
            for i in range(0, len(t) - 1):
                if t[i] > t[i + 1]:
                    t[i + 1] += 12
            l += t

        return l

    def __init__(self, time, duration, note=None, octave=None, pitch=None):
        if pitch:
            p = pitch
            while p > 35:
                p -= 12

            self.note = self.notes_by_pitch[p]
            self.octave = (pitch - p) // 12
            self.duration = duration
            self.time = time
            self.pitch = pitch
        else:
            self.note = note
            self.octave = octave
            self.duration = duration
            self.time = time
            self.pitch = self.notes[note] + 12 * octave

    def get_pitch(self):
        return self.pitch

    def get_note(self):
        return self.note, self.octave

    def get_pitch_scale(self, scale, octave):
        l = [self.notes[n] + 12 * octave for n in self.keys[scale]]
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                l[i + 1] += 12
        return l

    def generate_melody(cls, key, octave, length):

        matrix = [[None for k in range(length)] for x in range(108)]
        for m in matrix:
            print(matrix.index(m), m)
