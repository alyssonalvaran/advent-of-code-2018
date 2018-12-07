"""
Reference: https://adventofcode.com/2018/day/4
"""

import re

# save data-day-03.txt content as string variable data
with open ("data-day-04.txt", "r") as file:
    data = file.readlines()

# convert string variable data to a list of strings
data = [d.replace("\n", "") for d in data]

# sort data chronologically
data = sorted(data)

"""
{
	10: [
		[05, 24],
		[30, 54],
		[24, 28]
	],
	99: [
		[40, 49],
		[36, 45],
		[45, 54]
	]
}
"""

parsed_data = {}
guard_id = None
for i in range(len(data)):
	# get guard id
	has_guard_id = re.search('Guard #(.*) begins shift', data[i])
	if has_guard_id is not None:
		guard_id = int(has_guard_id.group(1))
	
	# get time
	else:
		has_woken_up = re.search(':(.*)] wakes up', data[i])
		if has_woken_up is not None:
			has_slept = re.search(':(.*)] falls asleep', data[i-1])
			
			if guard_id not in parsed_data:
				parsed_data[guard_id] = []
			parsed_data[guard_id].append([int(has_slept.group(1)), int(has_woken_up.group(1))-1])

# get guard_id with the most time asleep
guard_with_most_sleep = None
total_time_asleep = 0
for guard_id in parsed_data:
	time_asleep = 0
	for time in parsed_data[guard_id]:
		time_asleep = time_asleep + (time[1] - time[0])
	
	if guard_with_most_sleep is None or time_asleep > total_time_asleep:
		guard_with_most_sleep = guard_id
		total_time_asleep = time_asleep

# get minute where the guard slept the most
most_frequent_minute = None
max_minute_counter = 0
for minute in range(60):
	minute_counter = 0
	for time in parsed_data[guard_with_most_sleep]:
		if time[0] <= minute <= time[1]:
			minute_counter = minute_counter + 1
	if most_frequent_minute is None or max_minute_counter < minute_counter:
		most_frequent_minute = minute
		max_minute_counter = minute_counter

print(guard_with_most_sleep * most_frequent_minute)
	