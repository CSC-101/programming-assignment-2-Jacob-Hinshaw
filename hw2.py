import data

# Write your functions for each part in the space below.

# Part 1
# This function takes 2 inputs of class Point and returns a Rectangle regardless of the points inputted.
def create_rectangle(point1:data.Point, point2:data.Point) -> data.Rectangle:
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
# This function takes two inputs of class Duration and if the duration of the first duration is shorter than
# the second duration, the function returns True. Otherwise, it returns False.
def shorter_duration_than(time1:data.Duration, time2:data.Duration) -> bool:
    if time1.minutes < time2.minutes:
        return True
    if time1.minutes == time2.minutes:
        if time1.seconds < time2.seconds:
            return True
    return False


# Part 3
# This function takes an input of a list of Songs and a duration. It will return a list of songs from the
# input list that are shorter than the given duration.
def song_shorter_than(input1:list[data.Song], bound:data.Duration) -> list[data.Song]:
    output = []
    for song in input1:
        if song.duration.minutes < bound.minutes:
            output.append(song)
        if song.duration.minutes == bound.minutes:
            if song.duration.seconds < bound.seconds:
                output.append(song)
    return output

# Part 4
# This function takes an input of a list of Songs and a list of integers. It uses the list of integers and
# uses them as indexes for the list of songs and adds the duration of all the songs given.
def running_time(input_list1:list[data.Song], input_list2:list[int]) -> data.Duration:
    output = data.Duration(0,0)
    for num in input_list2:
        if 0 <= num <= len(input_list1):
            output.minutes += input_list1[num].duration.minutes
            output.seconds += input_list1[num].duration.seconds
    while output.seconds >= 60:
        output.minutes += 1
        output.seconds -= 60
    return output

# Part 5
# This function takes a list of a list of city names as a string as links as well as a second input of a route
# as a list of strings and it checks if the route is viable with the given links and returns a boolean value
def validate_route(links:list[list[str]], route:list[str]) -> bool:
    if len(route) <= 1:
        return True
    for i in range(len(route)-1):
        city1 = route[i]
        city2 = route[i+1]
        if [city1, city2] not in links and [city2, city1] not in links:
            return False
    return True

# Part 6
# This function takes a list of integers and looks for the longest contiguous series of the same integer.
# It returns the index of the first integer in the contiguous series.
def longest_repetition(numbers:list[int]) -> any:
    if len(numbers) == 0:
        return None
    if len(numbers) == 1 or len(numbers) == 2:
        return 0
    big_idx = 0
    start_idx = 0
    current_num = numbers[0]
    tally = 1
    max_tally = 1
    for idx in range(1, len(numbers)):
        if numbers[idx] == current_num:
            tally += 1
        else:
            if tally > max_tally:
                big_idx = start_idx
                max_tally = tally
            tally = 1
            current_num = numbers[idx]
            start_idx = idx
    if tally > max_tally:
        big_idx = start_idx
    return big_idx

