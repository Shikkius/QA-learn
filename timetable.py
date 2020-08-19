import datetime as DT

year = int(input('Введите год в формате ГГГГ: '))
month = int(input('Введите месяц в формате ММ: '))
day = int(input('Введите день в формате ДД: '))
count = 30

date = DT.date(year, month, day)
dateEnd = date + DT.timedelta(days=count)
cntDay = 0
cntDelta = 0
wkd = 0
print(f'Дата начала: {date}')

for i in range(20):
    i = date + DT.timedelta(days=cntDelta)
    wkd = i.weekday()
    cntDay = i
    if cntDay <= dateEnd and wkd < 6:
        cntDelta += 2
        cntDay = DT.datetime.strftime(cntDay, '%d %m %Y %A')      
        i = cntDay
        print(i)
    elif cntDay <= dateEnd and wkd == 6:
        cntDelta += 1
        continue
    else:
        break
print(f'Дата конца: {dateEnd}')