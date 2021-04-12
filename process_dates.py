from datetime import datetime
import json
import ast

month_index = {
    'Jan':0,
    'Feb':1,
    'Mar':2,
    'Apr':3,
    'May':4,
    'Jun':5,
    'Jul':6,
    'Aug':7,
    'Sep':8,
    'Oct':9,
    'Nov':10,
    'Dec':11
}

months_leap = [
    ('Jan',31),
    ('Feb',29),
    ('Mar',31),
    ('Apr',30),
    ('May',31),
    ('Jun',30),
    ('Jul',31),
    ('Aug',31),
    ('Sep',30),
    ('Oct',31),
    ('Nov',30),
    ('Dec',31)]

months = [
    ('Jan',31),
    ('Feb',28),
    ('Mar',31),
    ('Apr',30),
    ('May',31),
    ('Jun',30),
    ('Jul',31),
    ('Aug',31),
    ('Sep',30),
    ('Oct',31),
    ('Nov',30),
    ('Dec',31)]

def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

with open('dates.txt', 'r') as f:
        
    contents = f.read()


dates = ast.literal_eval(contents)
i_list = []
end_month = -1
end_day = -1
end_year = -1
curr_month = -1
curr_day = 0
curr_year = 0
i = 1
curr_max = 1
streak_store = {}
for elem in dates:
    parse = elem.split(',')
    year = int(parse[1])
    parse2 = parse[0].split(' ')
    month = parse2[0]
    day = int(parse2[1])
    if curr_month == -1:
        curr_day = day
        curr_month = month_index[month]
        curr_year = year
        end_day = day
        end_month = month_index[month]
        end_year = year
    if curr_day - 1 == day:
        i += 1
        curr_day = day
    elif curr_month - 1 == month_index[month]:
        if leap_year(year):
            last_day_of_month = months_leap[curr_month - 1][1]
        else:
            last_day_of_month = months[curr_month - 1][1]
        if last_day_of_month == day:
            curr_day = day
            curr_month = month_index[month]
            i += 1
        else:
            print(last_day_of_month, curr_day, curr_month, curr_year, day, month, year)
    elif curr_year - 1 == year and month == 'Dec' and day == 31:
        curr_day = day
        curr_month = month_index[month]
        curr_year = year
        i += 1
    else:
        if i > curr_max:
            curr_max = i
            streak_store[i] = {
                'start': {
                    'start_day':day,
                    'start_month':month,
                    'start_year':year,
                    },
                'end':  {
                    'end_day':end_day,
                    'end_month':months[end_month][0],
                    'end_year':end_year
                    }
            }
        i_list.append(i)
        i = 1
        curr_day = day
        curr_month = month_index[month]
        curr_year = year
        end_day = day
        end_month = month_index[month]
        end_year = year
    start_day = curr_day
    start_month = curr_month
    start_year = curr_year
print(elem)
print(streak_store[curr_max])
print(f'Longest consecutive streak: [{curr_max}]')
start = f'{streak_store[curr_max]["start"]["start_day"]} {streak_store[curr_max]["start"]["start_month"]} {streak_store[curr_max]["start"]["start_year"]}'
end = f'{streak_store[curr_max]["end"]["end_day"]} {streak_store[curr_max]["end"]["end_month"]} {streak_store[curr_max]["end"]["end_year"]}'
print(f'Start date: [{start}]   End date: [{end}]')

print('******************************************')
for i in i_list:
    print(i)
print('******************************************')

    

