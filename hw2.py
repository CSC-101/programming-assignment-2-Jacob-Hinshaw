import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1:data.Point, point2:data.Point) -> data.Rectangle:
#    if point1.x >= point2.x and point1.y <= point2.y:
#        point_top_left = point2
#        point_bottom_right = point1
#    if point1.x <= point2.x and point1.y >= point2.y:
#        point_top_left = point1
#        point_bottom_right = point2
#    return data.Rectangle(point_top_left, point_bottom_right)
    if point1.x >= point2.x:
        large_x = point1.x
        small_x = point2.x
    else:
        large_x = point2.x
        small_x = point1.x
    if point1.y >= point2.y:
        large_y = point1.y
        small_y = point2.y
    else:
        large_y = point2.y
        small_y = point1.y
    return data.Rectangle(data.Point(small_x, large_y), data.Point(large_x, small_y))


# Part 2


# Part 3


# Part 4


# Part 5


# Part 6
