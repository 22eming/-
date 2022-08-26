import numpy as np

def change_res(res,yy,xx,prevnum,min_num):
    nownum = res[yy][xx]
    min_num = min(min_num,nownum)
    res[yy][xx] = prevnum
    prevnum = nownum
    return res, prevnum, min_num

def solution(rows, columns, queries):
    answer = []
    result = np.arange(rows*columns).reshape(rows,columns)+1
    res = []
    for i in result:
        res.append([ int(j) for j in i])

    for querie in queries:
        [y1,x1,y2,x2] = np.array(querie)-1
        prevnum = res[y1][x1]
        min_num = prevnum
        for xx in range(x1+1,x2+1):
            yy = y1
            res, prevnum, min_num = change_res(res,yy,xx,prevnum,min_num)

        for yy in range(y1+1, y2+1):
            res, prevnum, min_num = change_res(res,yy,xx,prevnum,min_num)

        for xx in range(x2-1,x1-1,-1):
            res, prevnum, min_num = change_res(res,yy,xx,prevnum,min_num)
        
        for yy in range(y2-1,y1-1,-1):
            res, prevnum, min_num = change_res(res,yy,xx,prevnum,min_num)
        answer.append(min_num)
    
    return answer
    

print(solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))