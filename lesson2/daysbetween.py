# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def isleapyear(year):
    if year%4==0:
        if year%100==0:
           if year%400==0:
              return True
        else:
              return True
    return False


def daysinmonth(year,month):
    if month ==1 or month ==3 or month ==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    else:
        if month==2:
            if isleapyear(year):
                return 29
            return 28
    return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysinmonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysisbefore(year1, month1, day1, year2, month2, day2):
    if year1<year2:
        return True
    if year1==year2:
        if month1<month2:
            return True
        if month1==month2:
            return day1<day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    # YOUR CODE HERE!
    day=0
    while daysisbefore(year1, month1, day1, year2, month2, day2):
        year1,month1,day1=nextDay(year1,month1,day1)
        day=day+1
    return day
        




print daysBetweenDates(2012,02,22,2012,03,01)
print daysBetweenDates(1912,02,2,2012,02,02)
print daysBetweenDates(2013,02,2,2012,02,06)
