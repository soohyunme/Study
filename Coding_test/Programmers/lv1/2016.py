from datetime import date
def solution(a, b):
    day_list = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return day_list[date(2016,a,b).weekday()]