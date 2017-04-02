import random
from scripts.track import Track
from scripts.song import Song

class Composer:
    """Class responsible for composing music"""

    def __init__(self,
                 length,  # length of song in beat
                 instruments_list=[33, 43, 56],
                 tempo=550,  # tempo of song in beat per minute
                 output="my_file.mid",  # path to output file
                 samples=3,  # amount of samples to duplicate in track
                 bass_sample=False,  # flag saying if bass line is required
                 sample_length=15,  # length of sample to generate
                 step=1,  # average difference of pitch note change
                 tracks=1,
                 intense=100,  # intense of sample in time
                 flow_ratio=75,  # frequency of note pitch change ratio <-(0,100)
                 seed_ratio=70,  # frequency of seeding in harmonical samples<-(0,100)
                 seed_range=8,  # range of seeding in harmonical samples <-(0,100)
                 down_willing_ratio=50,  # ratio of getting low witch pitch in harmonical samples
                 jump=2,  # avarega pitch diference in bass line
                 rude=50,  # ratio of ignoring parameters, and gerating random in bassline
                 key="c",  # key in which music is generated
                 losing=0  # ratio of ignoring notes in generating midi

                 ):
        """Initializes a composer"""
        self.key = key
        self.rude = rude
        self.jump = jump
        self.tracks = tracks
        self.down_willing_ratio = down_willing_ratio
        self.seed_range = seed_range
        self.seed_ratio = seed_ratio
        self.flow_ratio = flow_ratio
        self.step = step
        self.intense = intense
        self.sample_length = sample_length
        self.bass_sample = bass_sample
        self.samples = samples
        self.output = output
        self.losing = losing
        self.tempo = tempo
        self.length = length
        self.instrument = instruments_list

    def compose(self):

        self.song = Song(self.tracks, self.length)

        for i in range(0, self.tracks):
            self.song.add_track(
                Track(start=i * (self.length // self.tracks), instrument=random.choice(self.instrument) - 1,
                      length=self.length, samples=self.samples, bass=False,
                      sample_lengths=self.sample_length,
                      step=self.step, intense=self.intense, flow=self.flow_ratio, tempo=self.tempo,
                      seed_ratio=self.seed_ratio, seed_range=self.seed_range,
                      down_willing_ratio=self.down_willing_ratio, key=self.key))
        if self.bass_sample:
            self.song.add_track(Track(0, 35, self.length, self.tempo, 1, True, 15, intense=90, key=self.key))
        self.song.save_song(self.output)
