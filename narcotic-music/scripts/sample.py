import random


class Sample:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def generate_sample(sample_columns=10, sample_rows=36, step=1, pitch=15, intense=75, flow=60, seed_ratio=45,
                        seed_range=5, down_willing_ratio=50):

        a = [["." for k in range(sample_columns)] for x in range(sample_rows)]
        a[pitch][0] = "X"
        for i in range(sample_columns):
            r = random.randint(0, 100)
            if r < intense:  # intense of fulfilling matrix
                if 0 < pitch < sample_rows:
                    a[pitch][i] = "X"
                    if random.randint(0, 100) < seed_ratio:  # seed
                        for j in range(random.randint(0, 5)):
                            x = random.randint(-seed_range, seed_range)
                            if 0 < pitch + x < sample_rows:
                                a[pitch + x][i] = "X"

                    t = random.randint(1, 100)
                    if t < flow:
                        b = random.randint(1, 100)
                        if b > down_willing_ratio:  # down_willing_ratio - the greater -> more often notes pitch go low
                            pitch += step
                        else:
                            pitch -= step

        s = Sample(sample_columns, sample_rows)
        s.matrix = a
        return s

    @staticmethod
    def generate_bass_sample(length=20, jump=2, intense=75, rude=50):
        a = [["." for k in range(length)] for x in range(12)]

        a[6][0] = "X"
        should_change = False
        rythmdiv = random.randint(2, 4)
        breakpoint = length // rythmdiv
        actual = 6
        for i in range(length):
            r = random.randint(0, 100)
            if r < intense:  # intense of fulfilling matrix
                if 0 < actual < 12:
                    a[actual][i] = "X"
                    if i % breakpoint == 0:
                        should_change = True
                    if should_change:
                        if random.randint(0, 100) > rude:
                            should_change = False
                            actual += jump * (random.choice([-1, 1]))

        s = Sample(length, 12)
        s.matrix = a
        return s
