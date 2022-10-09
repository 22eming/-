import sys
N = int(input())
for _ in range(N):
    n = int(input())
    candi = sorted( [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)] )
    cnt = 0
    m_min = float('inf')
    for i in range(n):
        m_i = candi[i][1]
        if m_i < m_min:
            cnt += 1
            m_min = m_i

    print(cnt)