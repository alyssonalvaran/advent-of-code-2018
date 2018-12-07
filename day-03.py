"""
Reference: https://adventofcode.com/2018/day/3
"""

# save data-day-03.txt content as string variable data
with open ("data-day-03.txt", "r") as file:
    data = file.readlines()

# convert string variable data to a list of strings
data = [d.replace("\n", "") for d in data]

coordinates = []
coordinates_with_id = {}
for d in data:
	coordinates_per_id = []
	
	# parse data into a list of integers
	"""
	0 - id
	1 - border width
	2 - border length
	3 - width
	4 - length
	"""
	d = d.replace("#", "").replace(" @ ", ",").replace(": ", ",").replace("x", ",").split(",")
	d = [int(i) for i in d]
	
	# append data coordinates to coordinates list (format: [x, y] starting from index 0 of Q4)
	for l in range(d[4]):
		for w in range(d[3]):
			coordinates.append(str(d[1] + w) + ", " + str(d[2] + l))
			coordinates_per_id.append(str(d[1] + w) + ", " + str(d[2] + l))
	
	# append coordinates with id as key-value pair
	coordinates_with_id[d[0]] = coordinates_per_id

overlap_count = len(set([c for c in coordinates if coordinates.count(c) > 1]))
print("Part 1: " + str(overlap_count))

unique_id = None
for c_key in coordinates_with_id:
	#check each coordinate if has a duplicate in the coordinates list
	has_duplicates = False
	for coordinate in coordinates_with_id[c_key]:		
		if coordinates.count(coordinate) > 1:
			has_duplicates = True
	
	# if it doesn't have a duplicate, set it as the value of unique_id
	# (only works because there's exactly only one id with no duplicates)
	if not has_duplicates:
		unique_id = c_key
	
print("Part 2: " + str(unique_id))