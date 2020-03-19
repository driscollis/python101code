# bowling_ball.py
import ball

class BowlingBall(Ball):
    
    def roll(self):
        print(f'You are rolling the {self.ball_type} ball')
        
if __name__ == '__main__':
    ball = BowlingBall()
    ball.roll()