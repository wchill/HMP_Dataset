import numpy as np 
from collections import defaultdict

all_the_z = list() #initialize another list to hold all the zbarprimes (step 4 in your notes)
k = 1
for arraylist in all_the_z.values():  # Each "value" in the dictionary is a list of arrays
	for array in arraylist:
		flattened = array.flatten()
		for i in xrange(0, len(flattened), 3*k):  # TODO: Init k somewhere
			subarray = flattened[i:(i + 3*k)]
			if len(subarray) != (3*k): 
				break
			all_the_z.append(subarray)