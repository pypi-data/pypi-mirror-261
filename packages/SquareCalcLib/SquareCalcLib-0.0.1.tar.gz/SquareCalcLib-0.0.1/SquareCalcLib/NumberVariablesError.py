class NumberVariablesError(Exception):
    """
    The error class of the entered values
    :return: NumberVariablesError - type error
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
