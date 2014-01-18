month_to_days = {
	1:31,
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31
}
year = 1900
day = 0 #Monday; Sunday=6

no_sundays_on_first = 0
while year < 2001:
	leapyear = (year % 400 == 0 or (year % 4 == 0 and not (year % 100 == 0)))
	for month in range(1,12+1):
		if day == 6 and year >= 1901:
			no_sundays_on_first += 1

		if month == 2 and leapyear:
			no_days = 29
		else:
			no_days = month_to_days[month]
		day = (day + no_days) % 7
	year += 1
print no_sundays_on_first