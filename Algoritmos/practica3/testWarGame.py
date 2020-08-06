import warGame
import unittest

def test_war_game():
    assert warGame.runOperation(1, 0, 1) == None,   "Should be None"
    assert warGame.runOperation(1, 1, 2) == None,   "Should be None" 
    assert warGame.runOperation(2, 0, 5) == None,   "Should be None"
    assert warGame.runOperation(3, 0, 2) == 1,      "Should be 1"
    assert warGame.runOperation(3, 8, 9) == 0,      "Should be 0"
    assert warGame.runOperation(4, 1, 5) == 1,      "Should be 1"
    assert warGame.runOperation(4, 1, 2) == 0,      "Should be 0"
    assert warGame.runOperation(4, 8, 9) == 0,      "Should be 0"
    assert warGame.runOperation(1, 8, 9) == None,   "Should be None"
    assert warGame.runOperation(1, 5, 2) == -1,     "Should be -1"
    assert warGame.runOperation(3, 5, 2) == 0,      "Should be 0"

if __name__ == "__main__":
    test_war_game()
    print("Everything passed")