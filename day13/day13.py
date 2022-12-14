import json
import functools


def parse_input(filename):
    with open(filename) as f:
        packets = f.read().split('\n\n')
        packets = [i.split() for i in packets]
        packets = [[json.loads(i[0]), json.loads(i[1])] for i in packets]
        return packets


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0
    elif isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            res = compare(l[i], r[i])
            if res != 0:
                return res
        if len(l) < len(r):
            return -1
        if len(l) > len(r):
            return 1
        return 0
    else:
        if isinstance(l, int):
            l = [l]
        elif isinstance(r, int):
            r = [r]
        return compare(l, r)


def calculate_sum_of_right(packets):
    sum = 0
    for i, packet in enumerate(packets):
        if compare(packet[0], packet[1]) == -1:
            sum = sum + i + 1
    return sum


def calculate_decoder_key(packets):
    packets_flat = []
    for packet in packets:
        packets_flat = packets_flat + packet
    packets_flat.append([2])
    packets_flat.append([6])
    packets_flat_sorted = sorted(packets_flat, key=functools.cmp_to_key(compare))
    return ((packets_flat_sorted.index([2])+1) * (packets_flat_sorted.index([6])+1))
