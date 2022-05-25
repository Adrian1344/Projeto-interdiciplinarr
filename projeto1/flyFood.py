import time



def permutation(lst):

    if len(lst) == 1:
        return [lst]
    else:
        path = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for y in permutation(xs):
                path.append([x] + y)
        return path


def coordinate(mat, sd):
    lsi = []
    for w in sd:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if w in mat[i][j]:
                    lsi.append([i, j])
                elif len(lsi) == len(mat):
                    break
    return lsi


def count_distance(mat2, lst):
    poli = None
    min = float('inf')
    for row in permutation(lst):
        tr = coordinate(mat2, row)
        r = coordinate(mat2, ['R'])[0]
        current = r
        d = 0
        for next in tr:
            d += abs(current[0] - next[0]) + abs(current[1] - next[1])
            current = next

        d += abs(current[0] - r[0]) + abs(current[1] - r[1])
        if min > d:
            min = d
            poli = row

    return min, poli



M, N = input().split()
matrix = []

for i in range(int(M)):
    p = [i for i in input().split()]
    matrix.append(p)

way = []
for j in matrix:
    for y in j:
        if y != '0' and y != 'R':
            way.append(y)

d, caminho = count_distance(matrix, way)

print(f'A menor distância é {d} associada a {caminho} ')
print(matrix)