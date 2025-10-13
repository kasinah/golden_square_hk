class MusicTracker:
    # User-facing properties:
    # None directly exposed, internal list of tracks.

    def __init__(self):
        self._tracks = [] 


    def add_track(self, track):
        if track.strip() != "":
            self._tracks.append(track)
            return "added"
        else:
            return self._tracks 


    def list_tracks(self):
        return self._tracks
