def customer(a,b):
    cus_list = []
    n = 2
    pre_list = []
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
    while n < len(cus_list):
        # print(n,'번째')
        if cus_list[n][2] == 'booked' and cus_list[n-1][2] == 'unbooked':
            for i in range(0, n):
                if cus_list[i][2] == 'booked':
                    pre_list.append(i)
                if len(pre_list) >= 1:
                    pre_booked = cus_list[max(pre_list)]
                else:
                    pre_booked = cus_list[0]
            # print(n,'번째일때',cus_list[n],'의 차례이고 최근예약자는', pre_booked)
        if cus_list[n][2] == 'booked' and cus_list[n-1][2] == 'unbooked' and cus_list[n][1] - pre_booked[1] <= 10:
            cus_list[n-1], cus_list[n] = cus_list[n], cus_list[n-1]
            n = n - 1
        else:
            n = n + 1
        # print(cus_list)

    print(cus_list)

customer([['양권', '09:05']],[['성규', '09:00'], ['현주', '09:10']])
customer([['양권', '09:05'], ['헌', '12:55']], [['성규', '13:00'], ['성동', '12:50']])
customer([['이각', '09:17'],['화웅', '09:21'],['장료','09:30']],[['동탁','09:20'],['유선','09:30'],['마장','09:19']])

#결과값

[['성규', 540, 'unbooked'], ['양권', 545, 'booked'], ['현주', 550, 'unbooked']]
[['양권', 545, 'booked'], ['성동', 770, 'unbooked'], ['헌', 775, 'booked'], ['성규', 780, 'unbooked']]
[['이각', 557, 'booked'], ['화웅', 561, 'booked'], ['장료', 570, 'booked'], ['마장', 559, 'unbooked'], ['동탁', 560, 'unbooked'], ['유선', 570, 'unbooked']]
