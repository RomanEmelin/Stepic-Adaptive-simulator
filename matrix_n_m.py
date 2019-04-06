n, m = map(int, input().split())
mtrx = [[int(i) for i in input().split()] for j in range(n)]

for i in range(m):
    for y in range(n):
        print(mtrx[y][i], end = ' ')
    print()    
