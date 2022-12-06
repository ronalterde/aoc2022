from collections import deque


def find_marker(s, windowsize=4):

    d = deque()
    i = 0
    for c in s:
        d.appendleft(c)
        i = i+1
        if len(d) == windowsize:
            if len(set(d)) == windowsize:
                return i
            d.pop()
    return None
