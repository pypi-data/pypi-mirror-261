def find_square_ellipse(large_semi_axis: float, small_semi_axis: float = None) -> float:
    """
    A function that calculates the area of an ellipse
    :param large_semi_axis: the value of the length of the large semi-axis of the ellipse
    :param small_semi_axis: the value of the length of the small semi-axis of the ellipse
    :return: square –  the value of the ellipse area
    """
    import math

    from NumberVariablesError import NumberVariablesError

    if large_semi_axis <= 0:
        raise NumberVariablesError('Incorrect value of the large semi-axis of the ellipse.\n'
                                   'The large semi-axis cannot be negative or equal to zero\n'
                                   'Error: ZeroOrNegativeSemiAxis')
    elif small_semi_axis:
        if small_semi_axis <= 0:
            raise NumberVariablesError('Incorrect value of the small semi-axis of the ellipse.\n'
                                       'The small semi-axis cannot be negative or equal to zero\n'
                                       'Error: ZeroOrNegativeSemiAxis')
        else:
            square = round((math.pi * large_semi_axis * small_semi_axis), 2)
            return square
    else:
        square = round((math.pi * large_semi_axis ** 2), 2)
        return square


if __name__ == '__main__':
    print(find_square_ellipse(2))
