from midiutil.MidiFile3 import MIDIFile


class Song:
    def __init__(self, tracks, length):
        self.song = None
        self.tracks = tracks
        self.length = length
        self.actual_track = 0
        self.tracks_list = []

    def add_track(self, track):
        self.tracks_list.append(track)

    def save_song(self, output="my_file.mid"):
        self.song = MIDIFile(len(self.tracks_list))
        for t in self.tracks_list:
            self.song.addTempo(self.actual_track, t.start, t.tempo)
            self.add_pitches(t)
            self.actual_track += 1
        with open(output, "wb") as output_file:
            self.song.writeFile(output_file)

    def add_pitches(self, track):
        for list in track.board.values():
            for note in list:
                self.song.addNote(self.actual_track, self.actual_track, note.get_pitch(), note.time, note.duration, 100)
        self.song.addProgramChange(self.actual_track, self.actual_track, track.start, track.instrument)
