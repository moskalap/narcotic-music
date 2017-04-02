import random

from scripts.note import Note
from scripts.sample import Sample


class Track:
    def __init__(self,
                 start,
                 instrument,
                 length=200,
                 tempo=450,
                 samples=3,
                 bass=True,
                 sample_lengths=15,
                 sample_rows=36,
                 step=1,
                 pitch=15,
                 intense=75,
                 flow=80,
                 seed_ratio=20,
                 seed_range=2,
                 down_willing_ratio=50,
                 key="c"

                 ):
        self.key = key
        self.bass = bass
        self.tempo = tempo
        self.start = start
        self.length = length
        self.instrument = instrument
        if bass:
            self.board = {time: [] for time in range(0, length)}

            self.sample = Sample.generate_bass_sample()
            self.convert_sample_to_note(self.sample, start, length, "c", 15)

        else:

            self.board = {time: [] for time in range(0, length)}
            self.samples = []
            for i in range(samples):
                self.samples.append(Sample.generate_sample(
                    sample_lengths, sample_rows, step, pitch, intense, flow, seed_ratio, seed_range,
                    down_willing_ratio))
            self.join_samples(self.key)

    def show_samples(self):
        for sample in self.samples:
            print("Sample")
            sample.print_sample()
        print("bass")
        self.bass_sample.print_sample()

    def join_samples(self, key="c", changes=None):
        if not changes:
            changes = self.length // len(self.samples)
        for i in range(0, len(self.samples)):
            pitch_start = 15 + 12 * 2
            self.convert_sample_to_note(self.samples[i], i * changes, (i + 1) * changes, key, pitch_start)

    def convert_sample_to_note(self, sample, start, end, key, pitch, shadowing=90,
                               volume_range=list(range(90, 100)), duration_range=list(range(1, 2)),
                               delay_range=list(range(1, 8))):
        diff = 0
        board_len = end - start
        possible = Note.get_possible_notes(key)
        copies = board_len / len(sample.matrix)
        R_MAX = 15 + pitch
        for time in range(start, end):
            level = random.choice([-1, 0, 1, 2])
            if time % len(sample.matrix[0]) == 0:
                if random.randint(0, 100) < 40 and not self.bass:
                    shadow = random.randint(-len(sample.matrix[0]), -5)
                    shadow += time
                    diff = 4
                    for q in range(0, len(sample.matrix[0])):
                        for w in range(0, len(sample.matrix)):
                            if sample.matrix[w][(shadow + q) % len(sample.matrix[0])] == "X":
                                pitch = R_MAX - w + 12 * diff
                                if pitch in possible and shadow + q > 0:
                                    n = Note(time=shadow + q, duration=1,
                                             pitch=pitch)
                                    self.board[shadow + q].append(n)
                if not self.bass:
                    diff = random.choice([0, 2])

            for note in range(0, len(sample.matrix)):

                if sample.matrix[note][(time - start) % len(sample.matrix[0])] == "X":

                    pitch = R_MAX - note + 12 * diff
                    if pitch in possible and random.randint(0, 100) < 100:
                        n = Note(time=time, duration=1+random.choice(duration_range),
                                 pitch=pitch)
                        self.board[time].append(n)
