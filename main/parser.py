import argparse
from argparse import RawTextHelpFormatter


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
        self.parser.add_argument("-o", "--output",
                                 help="specify a path to output file\n\n",
                                 default="my_midi_file.mid")
        self.parser.add_argument("-k", "--key", help="specify a key in which create midi\n"
                                                     "The keys are: c c# d e f# g a b \n"
                                                     "Default: c\n\n", default="c")

        self.parser.add_argument("-len", "--length", help="sets a length of song in beats\ndefault 200\n\n",
                                 default=200, type=int)

        self.parser.add_argument("-tm", "--tempo",
                                 help="specify tempo in bpm\ndefault 400\n\n",
                                 default=400,
                                 type=int)
        self.parser.add_argument("-s", "--samples",
                                 help="specify an amount of different samples, which will be used in tracks\ndefault 3\n\n",
                                 default=3, type=int)
        self.parser.add_argument("-t", "--tracks",
                                 help="specify an amount to tracks to generate\n default 1\n\n", default=2, type=int)
        self.parser.add_argument("-sl", "--sample_length", help="sets a length of single sample\ndefault 10\n\n",
                                 default=10,
                                 type=int)
        self.parser.add_argument("-b", "--bass", help="generates a bass line in song", action="store_true")
        self.parser.add_argument("-st", "--step",
                                 help="specify an average note pitch difference in harmonical sequences\ndefault 2\n\n",
                                 default=2,
                                 type=int)
        self.parser.add_argument("-i", "--intense", help="intensity of notes in sample in percentage\ndefault 75\n\n",
                                 default=75,
                                 type=int)
        self.parser.add_argument("-fr", "--flow_ratio",
                                 help="specify a pitch change frequency ratio [0-100]\ndefault 75\n\n",
                                 default=75,
                                 type=int)
        self.parser.add_argument("-sr", "--seed_ratio",
                                 help="frequency of seeding pitch in harmonical samples[0-100]\ndefault 30\n\n",
                                 default=30,
                                 type=int)
        self.parser.add_argument("-srng", "--seed_range",
                                 help="range of seeding in harmonical samples[0-10]\ndefault 5\n\n",
                                 default=5,
                                 type=int)
        self.parser.add_argument("-j", "--jump", help="average pitch change in bassline\ndefault 2\n\n", type=int,
                                 default=2)
        self.parser.add_argument("-r", "--rude", help="ratio of ignoring parameters[0-100]\ndefault 10\n\n", default=10,
                                 type=int)
        self.parser.add_argument("-l", "--losing", help="ratio of ignoring notes in generating midi[0-100]\ndefault "
                                                        "10\n\n",
                                 default=10, type=int)
        self.parser.add_argument("-dr", "--down_ratio",
                                 help="ratio of getting low in notes pitch [0-100]\ndefault 50\n\n", type=int,
                                 default=50)
        self.parser.add_argument("-inst", "--instruments", help=self.read_instruments(),
                                 nargs='+', default=[34, 44, 57], type=int)
        self.args = self.parser.parse_args()
        print(self.args.instruments)

    def get_args(self):
        return self.args

    def read_instruments(self):
        with open("instruments.txt") as f:
            content = f.readlines()
        comm = "list of instruments to use\nfor example\n-inst 1 2 3 4 5 6\nInstruments:\n"
        for x in content:
            comm += x
        return comm
