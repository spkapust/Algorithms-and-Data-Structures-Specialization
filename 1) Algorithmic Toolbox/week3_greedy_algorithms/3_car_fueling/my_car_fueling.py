# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    laststop = 0
    refuels = 0
    stops.append(distance)
    for i in range(len(stops)-1):
        if tank + laststop >= stops[i] and tank + laststop < stops[i+1]:
            laststop = stops[i]
            refuels += 1
    if laststop + tank < distance:
        return -1
    else: return refuels


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
