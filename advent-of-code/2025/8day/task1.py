
import numpy as np
from operator import mul
from functools import reduce

def parse_input(path: str) -> list[np.array]:
    res = []
    for line in open(path).readlines():
        res.append(np.array([int(el) for el in line[:-1].split(",")]))
    return res

def print_readable_set(s: set) -> None:
    print(f"=== SET START === len({len(s)})")
    for el in s:
        for e in el:
            print(int(e), end=", ")
        print("")
    print(f"=== SET END ===")

def solution(path: str, n: int) -> int:
    junctions = parse_input(path)
    len_junctions = len(junctions)
    dist = np.zeros((len_junctions, len_junctions))
    for i in range(len_junctions):
        for j in range(i + 1, len_junctions):
            dist[i][j] = np.linalg.norm(junctions[i] - junctions[j])
    dist[dist == 0] = np.inf
    sorted_idxs = np.unravel_index(np.argsort(dist, axis=None), dist.shape)
    res: list[set] = []
    junctions = [tuple(el) for el in junctions]
    for x, y in zip(sorted_idxs[0][:n], sorted_idxs[1][:n]):
        find_x = -1
        find_y = -1
        for idx, s in enumerate(res):
            if junctions[x] in s:
                find_x = idx
            if junctions[y] in s:
                find_y = idx
                if find_x != -1:
                    break
        if find_x == -1 and find_y == -1:
            new_set = set([junctions[x], junctions[y]])
            res.append(new_set)
            continue
        if find_x == find_y:
            continue

        if find_x != -1 and find_y != -1:
            res[find_x].update(res[find_y])
            res.pop(find_y)
            continue

        if find_x != -1:
            res[find_x].add(junctions[y])
        if find_y != -1:
            res[find_y].add(junctions[x])

    return reduce(mul, sorted((len(el) for el in res), reverse=True)[:3], 1)

if __name__ == "__main__":
    print(solution("valid_input.txt", n = 1000))
