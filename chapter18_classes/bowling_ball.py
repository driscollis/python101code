# bowling_ball.py
import ball

class BowlingBall(ball.Ball):

    def roll(self):
        print(f'You are rolling the {self.ball_type} ball')

if __name__ == '__main__':
    ball = BowlingBall('green', 10, 15, 'bowling')
    ball.roll()

