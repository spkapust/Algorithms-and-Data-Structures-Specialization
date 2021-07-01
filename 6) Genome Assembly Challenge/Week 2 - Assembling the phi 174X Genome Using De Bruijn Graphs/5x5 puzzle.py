#python3
import sys

n=5
pieces = []
for _ in range(n*n):
    s = sys.stdin.readline().strip()
    piece = s[1:-1].split(',')
    pieces.append(piece)

up = 0
left = 1
down = 2
right = 3

grid = [[None for _ in range(n)] for _ in range(n)]
used_piece = [False for _ in range(n*n)]


def check_fit(r,c,piece):
    if r == 0 and piece[up] != 'black':
        return False
    if r == n-1 and piece[down] != 'black':
        return False
    if c == 0 and piece[left] != 'black':
        return False
    if c == n-1 and piece[right] != 'black':
        return False
    if r > 0 and piece[up] != pieces[grid[r-1][c]][down]:
        return False
    if c > 0 and piece[left] != pieces[grid[r][c-1]][right]:
        return False
    return True  
    
def find_next_piece(r,c):
    if r == n: return True
    for idx, piece in enumerate(pieces):
        if used_piece[idx]:
            continue
        elif check_fit(r,c,piece):
            used_piece[idx] = True
            grid[r][c] = idx
            if c == n-1: 
                nr = r + 1
                nc = 0
            else:
                nr = r
                nc = c + 1
            if find_next_piece(nr, nc):
                return True
            else:
                used_piece[idx] = False
                grid[r][c] = None
    return False

find_next_piece(0,0)

for i in range(n):
    for j in range(n):
        if j != 0: 
            print(';', end='')
        print('(', end='')
        print(','.join(pieces[grid[i][j]]), end='')
        print(')', end = '')
    print('')
        
         

