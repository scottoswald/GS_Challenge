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

def test_adding_multiple_tracks():
    tracklist = Tracklist()
    tracklist.add_track("Yellow submarine")
    tracklist.add_track("All my loving")
    tracklist.add_track("Yesterday")
    result = tracklist.see_tracklist() 
    assert result == ["Yellow submarine", "All my loving", "Yesterday"]

def test_adding_not_a_string_raises_an_error():
    tracklist = Tracklist()
    with pytest.raises(TypeError) as e:  
        tracklist.add_track(5) 
    error_message = str(e.value)
    assert error_message == "Track name must be a string"

