def count_impossible_areas(n, areas):
    def is_impossible(area):
        target = 2 * area + 1
        # Check if the target can be expressed as (2*x + 1) * (2*y + 1)
        for odd_factor in range(1, int(target**0.5) + 1, 2):  # odd numbers only
            if target % odd_factor == 0:
                other_factor = target // odd_factor
                x = (odd_factor - 1) // 2
                y = (other_factor - 1) // 2
                if x > 0 and y > 0:
                    return False  # area is possible
        return True  # area is impossible

    impossible_count = sum(1 for area in areas if is_impossible(area))
    return impossible_count

import sys

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    areas = list(map(int, data[1:]))
    result = count_impossible_areas(n, areas)
    sys.stdout.write(str(result) + "\n")
