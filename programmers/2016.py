import calendar as cal
def solution(a, b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[cal.weekday(2016,a,b)]