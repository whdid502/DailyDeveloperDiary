def solution(n, m):
    answer = []
    n_list = []
    m_list = []
    answer_list= []
    for i in range(1,n+1):
        if n%i == 0:
            n_list.append(i)
    for i in range(1,m+1):
        if m%i == 0:
            m_list.append(i)
    for i in range(1,len(n_list)+1):
        for j in range(1,len(m_list)+1):
            if n_list[i] == m_list[j]:
                answer_list.append(n_list[i])
    if len(answer_list) == 1:
        max_v = 1
    else:
        max_v = answer_list[1]
    min_v = n_list[-2]*m_list[-2]
    answer.append(max_v)
    answer.append(min_v)
