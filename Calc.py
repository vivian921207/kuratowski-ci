from itertools import permutations
from typing import List, Tuple

def cut_two(graph: List[List[bool]], deg: List[int], n: int):
    while True:
        finish = True
        for i in range(1, n + 1):
            if deg[i] == 2:
                x = [j for j in range(1, n + 1) if graph[i][j]]
                deg[i] = 0
                if graph[x[0]][x[1]]:
                    deg[x[0]] -= 1
                    deg[x[1]] -= 1
                else:
                    graph[x[0]][x[1]] = graph[x[1]][x[0]] = True
                graph[x[0]][i] = graph[x[1]][i] = False
                graph[i][x[0]] = graph[i][x[1]] = False
                finish = False
                break
        if finish:
            break

def is_5(graph: List[List[bool]], deg5: List[int]) -> bool:
    if len(deg5) != 5:
        return False
    for p in permutations(deg5):
        exist = True
        for i in range(5):
            for j in range(5):
                if i != j and not graph[p[i]][p[j]]:
                    exist = False
                    break
            if not exist:
                break
        if exist:
            return True
    return False

def is_3(graph: List[List[bool]], deg3: List[int]) -> bool:
    if len(deg3) != 6:
        return False
    for p in permutations(deg3):
        group1 = p[:3]
        group2 = p[3:]
        exist = True
        for i in range(3):
            for j in range(i + 1, 3):
                if graph[group1[i]][group1[j]]:
                    exist = False
                    break
            if not exist:
                break
        if exist:
            for i in range(3):
                for j in range(i + 1, 3):
                    if graph[group2[i]][group2[j]]:
                        exist = False
                        break
                if not exist:
                    break
        if exist:
            for i in range(3):
                for j in range(3):
                    if not graph[group1[i]][group2[j]]:
                        exist = False
                        break
                if not exist:
                    break
        if exist:
            return True
    return False

def main():
    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        edges: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(m)]
        found = False
        for mask in range(1, 1 << m):
            graph = [[False] * (n + 1) for _ in range(n + 1)]
            deg = [0] * (n + 1)
            for j in range(m):
                if mask & (1 << j):
                    u, v = edges[j]
                    graph[u][v] = graph[v][u] = True
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if graph[i][j]:
                        deg[i] += 1
            cut_two(graph, deg, n)
            deg5 = [i for i in range(1, n + 1) if deg[i] == 4]
            deg3 = [i for i in range(1, n + 1) if deg[i] == 3]
            if is_5(graph, deg5) or is_3(graph, deg3):
                found = True
                break
        print("No" if found else "Yes")

if __name__ == "__main__":
    main()
