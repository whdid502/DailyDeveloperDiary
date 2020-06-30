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

#-------------
#최대공약수
def gcd(x,y):
    #y가 0이될때까지 반복
    while y:
        #y를 x에 대입
        #x를 y로 나눈 나머지에 y를 대입
        x,y = y, x%y
    return x

#내장함수
from math import gcd

print(gcd(1071,1029))

#21

#---------
#최소공배수
from math import gcd

def lcm(x,y):
    return x*y // gcd(x,y)
