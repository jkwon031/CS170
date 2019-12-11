import os
import math
import random
import copy

def nearestNeighborForward(current_set_of_features, val, i, j):
	distance = 0
	#print(current_set_of_features)
	temp = copy.deepcopy(current_set_of_features)
	temp.append(val)
	for k in range(len(temp)):
		distance = distance + pow(data[j][temp[k]] - data[i][temp[k]], 2)
	return distance

def nearestNeighborBackward(current_set_of_features, val, i, j):
	distance = 0
	#print(current_set_of_features)
	temp = copy.deepcopy(current_set_of_features)
	temp.remove(val)
	#print(temp)
	for k in range(len(temp)):
		distance = distance + pow(data[j][temp[k]] - data[i][temp[k]], 2)
	return distance

def leave_one_out(data, current_set_of_features, val, flag):
	num_correct = 0
	#print(current_set_of_features)
	for i in range(len(data)):
		best_so_far = float("inf")
		best_so_far_loc = float("nan")
		for j in range(len(data)):
			if i != j:
				if flag == 0:
					distance = nearestNeighborForward(current_set_of_features, val, i, j)
				elif flag == 1:
					#print("hi")
					distance = nearestNeighborBackward(current_set_of_features, val, i, j)
				#print(distance)
				if distance < best_so_far:
					best_so_far = distance
					best_so_far_loc = j
		if data[i][0] == data[best_so_far_loc][0]:
			num_correct = num_correct + 1
	accuracy = num_correct / len(data)
	return accuracy					

def forward_selection(data, num_features):
	flag = 0
	current_set_of_features = []
	for i in range(num_features):
		print("On the", str(i + 1), "th level of the search tree")
		feature_to_add_at_this_level = 0
		best_so_far_accuracy = 0
		for k in range(num_features):
			if (k + 1) not in current_set_of_features:
				print("--Considering adding the", str(k + 1), "feature")
				#print(current_set_of_features)
				accuracy = leave_one_out(data, current_set_of_features, k + 1, flag)
				print("accuracy: " + str(accuracy))
				if accuracy > best_so_far_accuracy:
					best_so_far_accuracy = accuracy
					feature_to_add_at_this_level = k + 1
		current_set_of_features.append(feature_to_add_at_this_level)
		print("On level", str(i + 1), ", I added feature", str(feature_to_add_at_this_level), "to current set")
		print(current_set_of_features)		
		#print(feature_to_add_at_this_level + 1)

def backward_elimination(data, num_features):
	flag = 1
	best_accuracy = 0
	#best_feature = 0
	#best_so_far_features = []
	best_set_of_features = []
	current_set_of_features = []
	for i in range(1, num_features + 1):
		current_set_of_features.append(i)
	print("This set:", current_set_of_features)
	for i in range(len(current_set_of_features)):
		print("On the", str(i + 1), "th level of the search tree")
		feature_to_remove_at_this_level = 0
		best_so_far_accuracy = 0
		best_so_far_features = []
		#best_feature = 0
		for k in range(num_features):
			
			if (k + 1) in current_set_of_features:
				print("--Consdering removing the", str(k + 1), "feature")

				accuracy = leave_one_out(data, current_set_of_features, k + 1, flag)
				print("accuracy: " + str(accuracy))
				if accuracy > best_so_far_accuracy:
					best_so_far_accuracy = accuracy
					best_so_far_features = current_set_of_features
					#print(best_so_far_features)
					feature_to_remove_at_this_level = k + 1
				if best_so_far_accuracy > best_accuracy:
					best_set_of_features = best_so_far_features
					best_accuracy = best_so_far_accuracy
					print("Best so far:", best_so_far_accuracy)
					#print(best_set_of_features)
					#print(best_set_of_features)
		#best_set_of_features.append(best_feature)
		current_set_of_features.remove(feature_to_remove_at_this_level)
		print("On level", str(i + 1), ", I removed feature", str(feature_to_remove_at_this_level), "from current set")
		print(current_set_of_features)
		print(best_accuracy, best_set_of_features)




if __name__ == "__main__":

	data = []
	#features = []
	num_features = 0
	num_instances = 0
	acc = 0
	mean = []
	stand_dev = []
	filename = "./CS170_SMALLtestdata__15.txt"
	#filename = "./test2.txt"

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
	#print(data)
	print("This dataset has", num_features, "features with", num_instances, "instances")

	
	#acc = leave_one_out(data, num_instances, num_features)
	#print("Running nearest neighbor with all", num_features, "features, using \"leaving-one-out\" evaluation, I get an accuracy of", acc)

	#forward_selection(data, num_features)
	backward_elimination(data, num_features)
'''
	for i in range(1, num_features + 1):
		features = []
		for row in data:
			features.append(row[i])
			print(features)
'''