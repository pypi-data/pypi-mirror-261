# SquareCalcLib
## A project to confirm knowledge on the platform hh.ru
### Date: 08.03.2024

A project to confirm knowledge on the platform **hh.ru**.

Library for calculating the areas of an ellipse and a triangle.

Stack of technologies used:
- _Python 3.10_

> [!NOTE]
> All modules are located in ***["SquareCalcLib"](/SquareCalcLib)***

> [!NOTE]
> Input values for the module **"find_square_triangle"**:
> 
> _To find the area of a triangle, you can enter both 3 sides and 2 sides and the angle **BETWEEN THEM**_
> - sides: list[float] - list of sides of the triangle
> - angle: float = None - the value in degrees of the angle between the two sides of the triangle

> [!NOTE]
> Input values for the module **"find_square_ellipse"**:
>
> _If you are sure that your shape is a circle, then you can not enter the "small_semi_axis" parameter, but represent "large_semi_axis" as the radius of the circle_
> - large_semi_axis: float - the value of the length of the large semi-axis of the ellipse 
> - small_semi_axis: float = None - the value of the length of the small semi-axis of the ellipse

> [!NOTE]
> NumberVariablesError 
> The error class of the entered values
> 
> Types of errror:
> - ZeroOrNegativeSemiAxis - semi-axis cannot be negative or equal to zero
> - IncorrectValuesSidesTriangle - the values of the sides of a triangle cannot be negative
> - SumSidesTriangle - the value of any one side cannot be greater than the sum of the values of the other sides
> - ValueAngleError - The angle cannot be less than or equal to zero or the angle cannot be more than 180 degrees