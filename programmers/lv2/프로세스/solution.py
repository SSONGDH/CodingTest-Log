from collections import deque

def solution(priorities, location):
    count = 0
    point = 0

    while priorities:
        point %= len(priorities)

        if priorities[point] == max(priorities):
            if location == point:
                count += 1
                break

            count += 1

            if point < location:
                location -= 1

            priorities.pop(point)

        else:
            point += 1

    return count
