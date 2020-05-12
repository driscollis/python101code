class Amount:

    def __init__(self):
        # private attribute
        self._amount = None

    def get_amount(self):
        return self._amount

    def set_amount(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._amount = value
        else:
            print(f'Value must be an int or float')

    amount = property(get_amount, set_amount)

if __name__ == '__main__':
    amt = Amount()
    print(f'The current amount is {amt.amount}')
    amt.amount = 'the'
    print(f'The current amount is {amt.amount}')
    amt.amount = 5.5
    print(f'The current amount is {amt.amount}')
