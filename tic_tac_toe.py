B = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
win = 0
times = 0
while win == 0:
    row1 = int(input('Player 1 row:'))
    col1 = int(input('Player 1 col:'))
    B[row1][col1] = 'x'
    times += 1
    print(f'{B[0][0]} {B[0][1]} {B[0][2]}\n{B[1][0]} {B[1][1]} {B[1][2]}\n{B[2][0]} {B[2][1]} {B[2][2]}')
    for i in range(3):
        if B[i][0] == B[i][1] == B[i][2] == 'x':
            win = 1
            print('Player 1 wins')
    for j in range(3):
        if B[0][j] == B[1][j] == B[2][j] == 'x':
            win = 1
            print('Player 1 wins')
    if B[0][0] == B[1][1] == B[2][2] == 'x' or B[0][2] == B[1][1] == B[2][0] == 'x':
        win = 1
        print('Player 1 wins')
    if times == 9:
        win = 1
        print('Draw')
    if win == 0:
        row2 = int(input('Player 2 row:'))
        col2 = int(input('Player 2 col:'))
        B[row2][col2] = 'o'
        times += 1
        print(f'{B[0][0]} {B[0][1]} {B[0][2]}\n{B[1][0]} {B[1][1]} {B[1][2]}\n{B[2][0]} {B[2][1]} {B[2][2]}')
        for i in range(3):
            if B[i][0] == B[i][1] == B[i][2] == 'o':
                win = 1
                print('Player 2 wins')
        for j in range(3):
            if B[0][j] == B[1][j] == B[2][j] == 'o':
                win = 1
                print('Player 2 wins')
        if B[0][0] == B[1][1] == B[2][2] == 'x' or B[0][2] == B[1][1] == B[2][0] == 'x':
            win = 1
            print('Player 2 wins')
