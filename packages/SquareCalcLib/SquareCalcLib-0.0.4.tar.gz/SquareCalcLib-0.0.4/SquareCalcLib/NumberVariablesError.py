class NumberVariablesError(Exception):
    """
    The error class of the entered values

    types of errror:\n
    - ZeroOrNegativeSemiAxis - semi-axis cannot be negative or equal to zero
    - IncorrectValuesSidesTriangle - the values of the sides of a triangle cannot be negative
    - SumSidesTriangle - the value of any one side cannot be greater than the sum of the values of the other sides
    - ValueAngleError - The angle cannot be less than or equal to zero or the angle cannot be more than 180 degrees

    :return: NumberVariablesError, {type error} - Exception
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return 'NumberVariablesError, {0}'.format(self.message)


if __name__ == '__main__':
    raise NumberVariablesError('Raise Error')
