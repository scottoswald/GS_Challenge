class Tracklist():

    def __init__(self):
        self.tracklist = []

    def see_tracklist(self):
        return self.tracklist

    def add_track(self, track):
        self.tracklist.append(track)