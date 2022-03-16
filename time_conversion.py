Time_in_second = int(input())
Hours = int(Time_in_second / 3600)
Minutes = int((Time_in_second / 3600 - Hours) * 60)
Seconds = Time_in_second % 60
print('%d : %d : %d' % (Hours, Minutes, Seconds))
