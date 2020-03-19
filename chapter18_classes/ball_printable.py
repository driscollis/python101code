# ball_printable.py

class Ball:

    def __init__(self, color: str, size: float, weight: float,
                 ball_type: str) -> None:
        self.color = color
        self.size = size
        self.weight = weight
        self.ball_type = ball_type

    def bounce(self):
        if self.ball_type.lower() == 'bowling':
            print("Bowling balls can't bounce!")
        else:
            print(f'The {self.ball_type} ball is bouncing!')

    def __repr__(self):
        return f'<Ball: {self.color} {self.ball_type} ball>'


if __name__ == "__main__":
    ball_one = Ball('black', 6, 12, 'bowling')
    ball_two = Ball('red', 12, 1, 'beach')

    print(ball_one)
    print(ball_two)