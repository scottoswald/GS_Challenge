class Tracklist():

    def __init__(self):
        self.tracklist = []

    def see_tracklist(self):
        return self.tracklist

    def add_track(self, track):
        if not isinstance(track, str):
            raise TypeError("Track name must be a string")
        else:
            self.tracklist.append(track)