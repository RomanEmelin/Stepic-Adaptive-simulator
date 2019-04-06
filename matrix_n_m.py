'''
Write a program that takes a matrix as input, performs its transposition, and outputs the result.

Input format:

The first line contains two integers Bat, the number of rows and columns, respectively.

Then Follow n lines containing m integers separated by a space.

Output format :

The program should output m the contents of the rows of the transposed matrix. Elements of the matrix should be separated by a space.

Example Input 1:
2 3
1 2 3
4 5 6
Sample Output 1:
1 4
2 5
3 6

Example Input 2:
2 2
1 2
3 4

Sample Output 2:
1 3
2 4
'''
n, m = map(int, input().split())
mtrx = [[int(i) for i in input().split()] for j in range(n)]    #I just changed the data output from the matrix by coordinates.=))

for i in range(m):
    for y in range(n):
        print(mtrx[y][i], end = ' ')
    print()    
