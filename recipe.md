# Tracklist Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Tracklist():
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Sets up an empty list
        pass # No code here yet

    def add_track(self, track):
        # Parameters:
        #   track: string representing name of track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        #   Throws error if track is not a string
        pass # No code here yet

    def see_tracklist(self):
        # Returns:
        #   A list of strings representing tacks
        # Side-effects:
        #   Throws an exception if no tra is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initialising an emoty tracklist
#see_tracklist returns an empty list
"""
tracklist = Tracklist()
tracklist.see_tracklist()
# [] 

"""
After adding a track
#see_tracklist returns a list of one track
"""
tracklist = Tracklist()
tracklist.add_track("Yellow submarine")
tracklist.see_tracklist() 
# ["Yellow submarine"]


"""
After adding multiple tracks
#see_tracklist returns a list with multiple tracks
"""
tracklist = Tracklist()
tracklist.add_track("Yellow submarine")
tracklist.add_track("All my loving")
tracklist.add_track("Yesterday")
tracklist.see_tracklist() 
# ["Yellow submarine", "All my loving", "Yesterday"]


"""
After adding a track that is not a string
#add_track raises an error
"""
tracklist = Tracklist()
tracklist.add_track(5) 
# TypeError

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
