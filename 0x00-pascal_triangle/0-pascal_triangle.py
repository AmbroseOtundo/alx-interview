#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []

    # Return an empty list if n is not positive
    if n <= 0:
        return triangle

    # Generate each row of the triangle
    for i in range(n):
        # The first and last element of each row is always 1
        row = [1]

        # If this is not the first row, generate the elements of the row
        if i > 0:
            # Generate the elements of the row by adding the adjacent elements of the previous row
            for j in range(i - 1):
                row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            # The last element of the row is also 1
            row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle
