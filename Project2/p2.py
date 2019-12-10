import os
import math

def feature_search(data, num_features):
	current_set_of_features = []
	for i in range(num_features):
		print("On the", str(i + 1), "th level of the search tree")
		for k in range(num_features):
			print("--Considering adding the", str(k + 1), "feature")
			accuracy = leave_one_out(data, current_set_of_features, k + 2)

def leave_one_out(data, num_instances, num_features):
	accuracy = 0
	num_correct = 0
	for i in range(num_instances):
		best_so_far = float("inf")
		best_so_far_loc = float("nan")
		#print("Looping over rows", str(i + 1))
		for j in range(num_instances):
			sum_dist = 0
			if(i != j):
				#print("for examplar", str(i + 1), "comparing it to", str(j + 1))
				for k in range(1, num_features + 1):
					distance = pow(data[i][k] - data[j][k] , 2)
					sum_dist = sum_dist + distance
				sum_dist = math.sqrt(sum_dist)
				if sum_dist < best_so_far:
					best_so_far = sum_dist
					best_so_far_loc = j
				#print("sum_dist = ", sum_dist)
		#print("for exemplar", str(i + 1), "I think its nearest neighbor is", str(best_so_far_loc + 1))

		if data[i][0] == data[best_so_far_loc][0]:
			print("I got exemplar", str(i + 1), "correct")
			num_correct = num_correct + 1
	accuracy = num_correct / num_instances
	#print(accuracy)

	return accuracy

if __name__ == "__main__":

	data = []
	#features = []
	num_features = 0
	num_instances = 0
	acc = 0
	mean = []
	stand_dev = []
	filename = "./test2.txt"

	f=open(filename, "r")
	fline = f.readline()



	#print(line.split())

	num_features = len(fline.split()) - 1
	#print(num_features)

	f.seek(0)

	for line in f:
		num_instances = num_instances + 1

	#print(num_lines)

	f.seek(0)

	for i in range(num_instances):
		data.append([])
		for j in f.readline().split():
			data[i].append(float(j))
	print(data)
	print("This dataset has", num_features, "features with", num_instances, "instances")

	
	acc = leave_one_out(data, num_instances, num_features)
	print("Running nearest neighbor with all", num_features, "features, using \"leaving-one-out\" evaluation, I get an accuracy of", acc)

	feature_search(data, num_features)

'''
	for i in range(1, num_features + 1):
		features = []
		for row in data:
			features.append(row[i])
			print(features)
'''