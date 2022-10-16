def cut(H, W, new, T_F):
    a = 0
    for i in range(W-1):
        for j in range(H-1):
            if new[i][j] == new[i][j+1] == new[i+1][j] == new[i+1][j+1] and new[i][j] != '':
                T_F[i][j], T_F[i][j+1], T_F[i+1][j], T_F[i+1][j+1] = False,False,False,False
                a += 1
    if a == 0: return 0
    return T_F

def solution(H, W, board):
    new = [[] for i in range(W)]
    T_F = [[True for i in range(H)] for i in range(W)]
    answer = 0
    for i in board:
        for j in range(W):
            new[j] = [i[j]] + new[j]
    while True:
        if cut(H, W, new, T_F) == 0: break
        for i in range(W):
            for j in range(-1,-H-1,-1):
                if T_F[i][j] == False:
                    del new[i][j]
                    new[i].append('')
                    del T_F[i][j]
                    T_F[i].append(False)
  
    return (H*W)- sum([sum(i) for i in T_F])