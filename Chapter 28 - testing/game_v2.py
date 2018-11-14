# game_v2.py

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
        spare_begin = 0
        spare_end = 2
        for roll in range(numOfRolls):
            spare = sum(self.pins[spare_begin:spare_end])
            if self.pins[x] == 10:
                self.score = self.pins[x] + self.pins[x+1] + self.pins[x+2]
            elif spare == 10:
                self.score = spare + self.pins[x+2]
                x += 1
            else:
                self.score += self.pins[x]
            x += 1
            if x == 11:
                break
            spare_begin += 2
            spare_end += 2
        print(self.score)