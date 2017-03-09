class Track:
    def __init__(self, track_no):
        self.tacts = []
        self.track_no=track_no
    def add_tact (self, tact):
        self.tacts.append(tact)

class Song:
    def __int__(self, title, tempo, metre):
        self.title = title
        self.tempo = tempo
        self.metre = metre
        self.tracks = []

    def add_tact (self, track):
        self.tracks.append(track)

