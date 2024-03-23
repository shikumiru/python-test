# 三目並べ

OPEN = 0
FIRST = 1
SECOND = 2
DRAW = 3

tuen = 1
board = [[0,0,0],[0,0,0],[0,0,0]]

def show_turn():
    if turn == FIRST:
        return('先手')
    elif turn == SECOND:
        return('後手')
    else:
        return('手板尾値が不適切です')
    
# 手番の初期化
def init_turn():
    global turn
    turn = 1
    
# 手番の交代
def change_turn():
    global turn
    if turn == FIRST:
        turn = SECOND
    elif turn == SECOND:
        turn = FIRST
        
# 手番関連の関数テスト
def test_turn():
    init_turn()
    print(show_turn(),"の番です")
    change_turn()
    print(show_turn(),"の番です")
    change_turn()
    print(show_turn(),"の番です")
    
# 盤面関連の関数
def show_board():
    s = ' :0 1 2\n---------\n'
    for i in range(3):
        s = s + str(i) + ': '
        for j in range(3):
            cell = ''
            if board[i][j] == OPEN:
                cell = ''
            elif board[i][j] == FIRST:
                cekk = 'O'
            elif board[i][j] == SECOND:
                cell = 'X'
            else:
                cell = '?'
            s = s + cell + ''
        s = s + '\n'
    return s

# 盤面の初期化
def init_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = OPEN
            
# 盤面の i, j の位置を返す
def examine_board(i, j):
    return board[i][j]

# 盤面の i, j に手番 t を登録、状態を文字列で返す
def set_board(i, j, t):
    if (i>=0) and (i<3) and (j>=0) and (j<3):
        if (t>0) and (t<3):
            if examine_board(i, j) == 0:
                board[i][j] = t
                return 'OK'
            else:
                return 'Not empty'
        else:
            return 'illegal turn'
    else:
        return 'illegal slot'

# 盤面のテスト関数
def test_board1():
    init_board()
    print(show_board())
    print(set_board(0,0,1))
    print(show_board())
    print(set_board(1,1,2))
    print(show_board())
    print(set_board(1,1,1))
    print(show_board())
    
def check_board_horizontal(t):
    for j in range(3):
        if (board[0][j] == t) and (board[1][j] == t) and (board[2][j] == t):
            return True
    return False

def check_board_vertical(t):
    for j in range(3):
        if (board[0][j] == t) and (board[1][1] == t) and (board[2][2] == t):
            return True
    return False

def check_board_diagonal(t):
    if (board[0][0] == t) and (board[1][1] == t) and (board[2][2] == t):
        return True
    return False

def check_board_inverse_diagonal(t):
    if (board[0][2] == t) and (board[1][1] == t) and (board[2][2] == t):
        return True
    return False

# 手番 t の勝ち判定
def is_win_simple(t):
    if check_board_horizontal(t):
        return True
    if check_board_vertical(t):
        return True
    if check_board_diagonal(t):
        return True
    if check_board_inverse_diagonal(t):
        return True
    return False

def is_win_actual(t):
    if not is_win_simple(t):
        return False
    if t==FIRST:
        if is_win_simple(SECOND):
            return False
    else:
        if is_win_simple(FIRST):
            return False
    return True

# 盤面埋まりの判定
def is_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == OPEN:
                return False
    return True

# 引き分けの判定
def is_draw():
    if is_win_simple(FIRST):
        return False
    if is_win_simple(SECOND):
        return False
    if not is_full():
        return False
    return True

# ログのリプレイ
def replat_log(log):
    init_board()
    init_turn()
    print(show_board())
    for m in log:
        if len(m) == 2:
            print(show_turn(),"の番です")
            print(set_board(m[0], m[1], turn))
            print(show_board())
            print("IS WIN", turn, ":", is_win_actual(turn))
            change_turn()
        else:
            print("RESULT IN LOG: ",m[0])
    print("IS WIN FIRST: ", is_win_actual(FIRST))
    print("IS WIN SECONF: ", is_win_actual(SECOND))
    print("IS DRAW: ", is_draw())
    
# プレイ
def play():
    init_turn()
    init_board()
    print(show_board())
    
    log = []
    while True:
        print(show_turn(),"の番です")
        while(True):
            row = int(input("行を入力"))
            column = int(input("列を入力"))
            result = set_board(row, column, turn)
            print(result)
            if result == "OK":
                break
            print("不適切な入力。再度、入力")
        print(show_board())
        if is_draw():
            print("引き分け")
            break
        if is_win_actual(turn):
            print(show_turn(), "の勝ち")
            break
        change_turn()
    if len(log)>0:
        replat_log(log)
    else:
        print("棋譜は作成されていません")
if __name__ == '__main__':
    print('三目並べ')