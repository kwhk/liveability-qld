def algorithm(distance):
	# distance is in the form of 2-tuple, with its weight and value where the value is the ratio of the commute time from destination to suburb over the max commute time out of all the suburbs in QLD

	value = 0

	for i in range(len(distance)):
		value += distance[i][0] * distance[i][1]

	return value