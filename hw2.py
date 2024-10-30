import data

# Write your functions for each part in the space below.

# Part 1
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
def shorter_duration_than(time1:data.Duration, time2:data.Duration) -> bool:
    if time1.minutes < time2.minutes:
        return True
    if time1.minutes == time2.minutes:
        if time1.seconds < time2.seconds:
            return True
    return False


# Part 3
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


# Part 6
