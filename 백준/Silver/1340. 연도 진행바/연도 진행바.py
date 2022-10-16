month, day, year, t = input().split()
year = int(year)
day = int(day[:-1])
h, m = map(int, t.split(":"))
month_name = ["January" , "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"]
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if not year % 400 or (not year%4 and year%100):
    month_day[1] += 1
total_time = sum(month_day) * 24 * 60
now_time = (sum(month_day[:month_name.index(month)]) + day-1) * 24 * 60 + h*60 + m
print(now_time / total_time * 100)