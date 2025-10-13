

"""
Given no tracks added
it returns existing list 
"""
from lib.music_Tracker import *


def test_add_track():
    ins = MusicTracker()
    assert ins.add_track("track 1") == "added"


