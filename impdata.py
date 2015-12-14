import os
import numpy as np
from collections import defaultdict
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

all_arrays = defaultdict(list)
for dirname in os.listdir("."):
	if not os.path.isdir(dirname): continue
	for filename in os.listdir(dirname):
		if filename.startswith("."): continue  # Edit added 12/7
		#print "Loading in: ", dirname + os.sep + filename
		array = np.loadtxt(dirname + os.sep + filename)
 		all_arrays[dirname].append(array)

all_the_z = list() #initialize another list to hold all the zbarprimes (step 4 in your notes)
k = 1
for arraylist in all_arrays.values():  # Each "value" in the dictionary is a list of arrays
	for array in arraylist:
		flattened = array.flatten()
		for i in xrange(0, len(flattened), 3*k):  
			subarray = flattened[i:(i + 3*k)]
			if len(subarray) != (3*k): 
				break
			all_the_z.append(subarray)


#Z, y = make_classification(n_samples=1000, n_features=6, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)

km = KMeans(n_clusters = 10)
km.fit(all_the_z)

file_zs = Z[10:15]

print("Flattened chunks of interest: ")
print(file_zs)

cluster_ids = km.predict(file_zs)
explicit_clusters = km.cluster_centers_[cluster_ids]
assert explicit_clusters.shape == (5,6)	   #5 centers, each of length 6

time_list = list()
x_list = list()

flattened_points = explicit_clusters.flatten()

for i in xrange(0, len(flattened_points), 3):
	x_val = flattened_points[i]
	time_list.append(i)
	x_list.append(x_val)

print("hello")
#plot signals
plt.plot(time_list, x_list)
plt.xlabel("time")
plt.ylabel("$x$ acceleration")
plt.show()
