""""
given the booked schedule of two individuals, their preference of holding a meeting within a time frame and duration of
meeting, give the list of time brackets for when the two individuals can have a meeting

[['9:00','10:30'],['12:00', '13:00'], ['16:00', '18:00']]
['9:00', '20:00']

[['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
['10:00', '18:30']

30
"""


def calavail(p1s, p1b, p2s, p2b, time):
    booked = []
    avail = []
    pb = []
    p1 = 0
    p2 = 0
    if comptime(p1b[0], p2b[0]) == -1:
        pb.append(p2b[0])
    elif comptime(p1b[0], p2b[0]) == 1 or comptime(p1b[0], p2b[0]) == 0:
        pb.append(p1b[0])
    if comptime(p1b[1], p2b[1]) == -1:
        pb.append(p1b[1])
    elif comptime(p1b[1], p2b[1]) == 1 or comptime(p1b[0], p2b[0]) == 0:
        pb.append(p2b[1])
    while p1 < len(p1s) and p2 < len(p2s):
        if comptime(p1s[p1][0], p2s[p2][0]) == -1:  # p1 is less than p2
            booked.append(p1s[p1])
            p1 += 1
        else:
            booked.append(p2s[p2])
            p2 += 1
    while p1 < len(p1s):
        booked.append(p1s[p1])
        p1 += 1
    while p2 < len(p2s):
        booked.append(p2s[p2])
        p2 += 2
    i = 0
    while i < len(booked) - 1:
        end1 = booked[i][1]
        start2 = booked[i + 1][0]
        if comptime(end1, start2) == 1:
            end2 = booked[i + 1][1]
            if comptime(end2, end1) == -1:
                booked.pop(i + 1)
                i -= 1
            else:
                booked[i][1] = end2
        i += 1
    for i in range(len(booked) - 1):
        end1 = booked[i][1]
        start2 = booked[i + 1][0]
        if difbw(end1, start2) >= int(time):
            avail.append([end1, start2])
    for i in range(len(avail) - 1):
        if avail[i][0] == avail[i][1]:
            avail.pop(i)
    if comptime(avail[0][0], pb[0]) == -1:
        avail[0][0] = pb[0]
    if comptime(avail[-1][1], pb[1]) == -1:
        avail.append([avail[-1][1], pb[1]])
    if comptime(avail[-1][1], pb[1]) == 1:
        avail[-1][1] = pb[1]
    return avail


def comptime(t1, t2):
    hour1, min1 = t1.split(":")
    hour2, min2 = t2.split(":")
    t1 = int(hour1) * 100 + int(min1)
    t2 = int(hour2) * 100 + int(min2)
    if t1 > t2:
        return 1  # greater than
    elif t1 < t2:
        return -1  # less than
    elif t1 == t2:
        return 0  # equal


def difbw(x, y):
    hx, mx = x.split(":")
    hy, my = y.split(":")
    return int((int(hy) * 100 + int(my)) - int((int(hx) * 100 + int(mx))))


sch1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
tb1 = ['9:00', '20:00']
sch2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
tb2 = ['10:00', '18:30']
dur = 30
print(calavail(sch1, tb1, sch2, tb2, int(dur)))
