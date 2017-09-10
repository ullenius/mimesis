import random


class Random(random.Random):
    """Custom Random() class for the possibility of extending."""

    def __init__(self):
        random.Random.__init__(self)

    def randints(self, amount=None, a=1, b=100):
        """Generate list of random integers.

        :param amount: Amount of elements.
        :param a: minimum
        :param b: maximum
        :return: List of random integers.
        """

        if not amount:
            amount = 3

        return [self.randint(a, b)
                for _ in range(amount)]