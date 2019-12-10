import os
import math


def nearestNeighborAlgorithm(data, curr_point, num_lines, curr_set):
	nn = 0
	shortestdist = float("inf")
	#print("Curr point:", curr_point)

	for i in range(num_lines - 1):
	#	print("hi")
		if curr_point != i:
			dist = 0
			for j in range(1, len(curr_set)):
				dist = math.sqrt(dist + pow((data[curr_point][curr_set[j]] - data[i][curr_set[j]]), 2))
				print(dist)

			if dist < shortestdist:
				nn = i
				shortestdist = dist

	return nn
'''
def search(data):
	current_set_of_features = []
	print(num_features)
	for i in range(num_features):
		print("On the", str(i + 1), "th level of the serach tree")
		feature_adding = []
		best_acc = 0
		for k in range(num_features):
			if k not in current_set_of_features:
				print("Considering adding the", str(k + 1), "feature")
				accuracy = leave_one_out_cross_validation(data, current_set_of_features, k + 2)
				#print(accuracy)

				if accuracy > best_acc:
					best_acc = accuracy
					feature_adding = k

		current_set_of_features.append(feature_adding)
		print("On level", str(i + 1), "added feature", str(feature_adding), "to current set")		
'''
def leave_one_out_cross_validation(data, curr_set, num_lines):
	num_correct = 0
	for i in range(num_lines):
		n = nearestNeighborAlgorithm(data, i, num_lines, curr_set)

		if data[n][0] == data[i][0]:
			num_correct = num_correct + 1

if __name__ == "__main__":

	data = []
	#features = []
	num_features = 0
	num_lines = 0
	mean = []
	stand_dev = []
	filename = "./test.txt"

	f=open(filename, "r")
	fline = f.readline()

	#print(line.split())

	num_features = len(fline.split()) - 1
	#print(num_features)

	f.seek(0)

	for line in f:
		num_lines = num_lines + 1

	#print(num_lines)

	f.seek(0)

	for i in range(num_lines):
		data.append([])
		for j in f.readline().split():
			data[i].append(float(j))
	print(data)

	for i in range(1, num_features + 1):
		features = []
		for row in data:
			features.append(row[i])
			print(features)
			leave_one_out_cross_validation(data, features, num_lines)