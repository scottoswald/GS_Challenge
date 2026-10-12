import pytest
from lib.tracklist import Tracklist

def test_return_empty_tracklist():
    tracklist = Tracklist()
    result = tracklist.see_tracklist()
    assert result == []

def test_add_one_track():
    tracklist = Tracklist()
    tracklist.add_track("Yellow submarine")
    result = tracklist.see_tracklist() 
    assert result == ["Yellow submarine"]