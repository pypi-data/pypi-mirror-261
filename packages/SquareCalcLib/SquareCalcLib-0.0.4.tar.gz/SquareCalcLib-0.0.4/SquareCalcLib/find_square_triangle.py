def find_square_triangle(sides: list[float], angle: float = None) -> tuple[float, bool]:
    """
    A function that calculates the area of a triangle
    :param sides: list of sides of the triangle
    :param angle: the value in degrees of the angle between the two sides of the triangle
    :return: square –  the value of the area of the triangle
             flag_rectangular_triangle –  True/False is the triangle - rectangular
    """

    import math

    from NumberVariablesError import NumberVariablesError

    flag_rectangular_triangle = False

    if len(sides) != 2 and len(sides) != 3:
        raise NumberVariablesError('Incorrect number of sides in a triangle.\n'
                                   'The sides of a triangle cannot be more or less than two with angle or three.\n'
                                   'Error: IncorrectNumberInputVariables')
    elif min(sides) <= 0:
        raise NumberVariablesError('Incorrect values of the sides of the triangle.\n'
                                   'The sides of a triangle cannot be negative or equal to zero.\n'
                                   'Error: IncorrectValuesSidesTriangle')
    elif len(sides) == 2:
        if angle:
            if angle <= 0 or angle > 180:
                raise NumberVariablesError('Incorrect value of the angle between the sides\n'
                                           'The angle cannot be less than or equal to zero.\n'
                                           'The angle cannot be more than 180 degrees.\n'
                                           'Error: ValueAngleError')
            else:
                side_a = sides[0]
                side_b = sides[1]
                radian_angle = math.radians(angle)
                square = round((1 / 2) * side_a * side_b * math.sin(radian_angle), 2)

                side_c = round((side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(radian_angle)) ** (1 / 2), 2)
                sides.append(side_c)
                sides.sort()
                if square == round((1 / 2) * (side_a * side_b), 2):
                    flag_rectangular_triangle = True

                return square, flag_rectangular_triangle

        else:
            raise NumberVariablesError('Incorrect value of the angle between the sides\n'
                                       'The sides of a triangle cannot be more or less than two with angle or three.\n'
                                       'The angle between the sides is not specified.')

    elif len(sides) == 3:
        side_a = sides[0]
        side_b = sides[1]
        side_c = sides[2]
        if side_a >= side_b + side_c \
                or side_b >= side_a + side_c \
                or side_c >= side_a + side_b:
            raise NumberVariablesError('Incorrect values of the sides of the triangle.\n'
                                       'A triangle with these sides cannot exist\n'
                                       'Error: SumSidesTriangle')
        else:
            half_perim = (1 / 2) * (side_a + side_b + side_c)
            square = (half_perim * (half_perim - side_a) * (half_perim - side_b) * (half_perim - side_c)) ** (1 / 2)
            sides.sort()
            if square == round((1 / 2) * (sides[0] * sides[1]), 2):
                flag_rectangular_triangle = True
            return square, flag_rectangular_triangle


if __name__ == '__main__':
    print(find_square_triangle([3, 4], 90))
