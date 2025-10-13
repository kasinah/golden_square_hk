# {{PROBLEM}} Class Design Recipe

class_test_music_tracker

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class music_tracker:
    # User-facing properties:
    #   name: string

    trackList = []
    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add_track(self,track):
        trackList.append(self.track)
        return trackList
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given no tracks added
it returns existing list 
"""
musicTracker = music_tracker()
res = musicTracker.add_track()
assert res == 0

"""
Given that a track provided 
single track is addedd
"""
musicTracker = music_tracker("tr")
res = musicTracker.add_track()
assert "tr" in res


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
