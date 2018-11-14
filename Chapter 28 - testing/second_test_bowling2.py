from game import Game
import unittest

class TestBowling(unittest.TestCase):
    """"""
 
    def test_all_ones(self):
        """Constructor"""
        game = Game()
        pins = [1 for i in range(11)]
    
        game.roll(11, pins)
        self.assertEqual(game.score, 11)

    def test_strike(self):
        """
        A strike is 10 + the value of the next two rolls. So in this case
        the first frame will be 10+5+4 or 19 and the second will be
        5+4. The total score would be 19+9 or 28.
        """
        game = Game()
        game.roll(11, [10, 5, 4])
        self.assertEqual(game.score, 28)
        
class Game:
    """"""
    
    def __init__(self):
        """Constructor"""
        self.score = 0
        self.pins = [0 for i in range(11)]

    def roll(self, numOfRolls, pins):
        """"""
        x = 0
        for pin in pins:
            self.pins[x] = pin
            x += 1
        x = 0
        for roll in range(numOfRolls):
            if self.pins[x] == 10:
                self.score = self.pins[x] + self.pins[x+1] + self.pins[x+2]
            else:
                self.score += self.pins[x]
            x += 1
        print(self.score)

if __name__ == '__main__':
    unittest.main()