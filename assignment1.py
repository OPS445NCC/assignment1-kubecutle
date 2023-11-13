#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2023
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: <Student Name>
Description: <fill this in>
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap yea
    return leap_flag

def day_count(year_start:str, year_end:str, day:str) -> int:
  
   count=0
   today=year_start
   while today != year_end:
       if day_of_week(today).lower() == day.lower():
          count=count+1
       today=after(today)
   return count


   return count

def mon_max(mon:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap_flag=leap_year(year)
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    return mon_max

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    leap_flag=leap_year(year)
    max=mon_max(mon,year)
 
    if day > max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    ...

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY   DD/MM/YYYY NN   Day")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    parts=date.split('/')
    if len(parts) != 3:
         return False
    
    day=int(parts[0])
    if day<1 or day > 31:
        return False
    month=int(parts[1])
    if month<1 or month > 12:
        return False
    year=int(parts[2])
    if year<1000 or year > 2100:
        return False

    max=mon_max(month,year)
    if max < day:
        return False
    return True


def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    ...

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        exit(0)
    valid = valid_date(sys.argv[1])
    if not valid :
        usage()
    valid = valid_date(sys.argv[2])
    if not valid :
        usage()
    # check length of arguments
    # check first arg is a valid date
    # check that second arg is a valid number (+/-)
    # call day_iter function to get end date, save to x
    # print(f'The end date is {day_of_week(x)}, {x}.')
    pass