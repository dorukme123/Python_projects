
def Fun_algoritm(n, e, m, m_x, step, mrk):
    while True:
        m_d = m_x
        for i in range(n):
            if not mrk[i] and step[i] < m_d:
                m_d = step[i]
                m_v = i
        if m_d == m_x:
            break
        i = m_v
        mrk[i] = True
        for j in range(n):
            if step[i] + m[i][j] < step[j] and m[i][j] > 0:
                step[j] = step[i] + m[i][j]
    if step[e - 1] == m_x:
        print(None)
    else:
        print(step[e - 1])


n, beggin, end = map(int, input().split())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

mx = 1000
step = [mx] * n
step[beggin - 1] = 0
mark = [False] * n
global m_v

Fun_algoritm(n, end, m, mx, step, mark)
