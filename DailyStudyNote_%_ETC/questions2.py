# type a
# booked = ['양권', '09:05']
# unbooked = ['성규', '09:00'], ['현주', '09:10']
# 예상답안 > ['성규', '양권', '현주']
#
# type b
# booked = [['양권', '09:05'], ['헌','13":00']]
# unbooked = [['성규', '12:55'], ['성동', '13:05']]
# 예상답안 > ['양권', '성동', '헌', '성규']
#
# 조건 : 예약시간이 먼저지만 예약자 우선순위, 진료시간은 10분

# import Datetime
from operator import itemgetter
def customer(a,b):
    answer = []
    cus_list = []
    # print(len(a))
    for i in range(len(a)):
        cus_list.append([a[i][0], a[i][1], 'booked'])
    for i in range(len(b)):
        cus_list.append([b[i][0], b[i][1], 'unbooked'])
    for i in range(len(cus_list)):
        hour = int(cus_list[i][1][:2])*60
        minutie = int(cus_list[i][1][-2:])
        tm = hour + minutie
        cus_list[i][1] = tm
    cus_list.sort(key=lambda x: x[1])
    print(cus_list)
    # for i in range(1,len(cus_list)):
    #     if cus_list[i][2] == 'booked' and cus_list[i][1] - cus_list[i-1][1] <= 10 and cus_list[i-1][2] == 'unbooked':
    #         cus_list[i-1], cus_list[i] = cus_list[i], cus_list[i-1]
    #         print(i)
    #         i -= i
    #         print(i)
    #         continue
    while


    print(cus_list)

customer([['양권', '09:05']],[['성규', '09:00'], ['현주', '09:10']])
customer([['양권', '09:05'], ['헌', '12:55']], [['성규', '13:00'], ['성동', '12:50']])
customer([['이각', '09:17'],['화웅', '09:21'],['장료','09:31']],[['동탁','09:20'],['유선','09:30'],['마장','09:19']])
