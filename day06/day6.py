from collections import deque


def find_marker(input_string, windowsize=4):
    queue = deque()
    char_count = 0
    for char in input_string:
        queue.appendleft(char)
        char_count = char_count + 1
        if len(queue) == windowsize:
            if len(set(queue)) == windowsize:
                return char_count
            queue.pop()
    return None
