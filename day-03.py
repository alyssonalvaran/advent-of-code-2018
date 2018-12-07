"""
Reference: https://adventofcode.com/2018/day/3
"""

# save data-day-03.txt content as string variable data
with open ("data-day-03.txt", "r") as file:
    data = file.readlines()

# convert string variable data to a list of strings
data = [d.replace("\n", "") for d in data]

# data = ["#3 @ 5,5: 2x2", "#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4"]

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

# count overlapping coordinates
overlap_count = len(set([c for c in coordinates if coordinates.count(c) > 1]))
print("Part 1: " + str(overlap_count))

# get unique coordinates
unique_coordinates = set([c for c in coordinates if coordinates.count(c) == 1])
# get ID of coordinates that did not overlap
for c_key in coordinates_with_id:
	print("c_key: " + str(c_key))
	if set(coordinates_with_id[c_key]).issubset(unique_coordinates):
		print("Part 2: " + str(c_key))
		break