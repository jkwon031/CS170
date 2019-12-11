import os
import math
import random
import copy
def normalize(data, num_features):
	mean = []
	stand_dev = []

	for i in range(1, num_features + 1):
		totsum = 0
		for j in range(len(data)):
			totsum = totsum + data[j][i]
		totsum = totsum / len(data)
		mean.append(totsum)
	#print(mean)

	for i in range(1, num_features + 1):
		square = 0
		for j in range(len(data)):
			square = square + (pow(data[j][i] - mean[i - 1], 2))
			#print(square)
		variance = square / len(data)
		#print(len(data))
		#print(variance)
		stand_dev.append(math.sqrt(variance))
	#print(stand_dev)

	for i in range(len(data)):
		for j in range(1, num_features + 1):
			data[i][j] = ((data[i][j] - mean[j-1]) / stand_dev[j-1])
	return data
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
	best_accuracy = 0
	best_set_of_features = []
	current_set_of_features = []
	tempacc = 0
	for i in range(num_features):
		print("On the", str(i + 1), "th level of the search tree")
		feature_to_add_at_this_level = 0
		best_so_far_accuracy = 0
		best_so_far_features = []
		for k in range(num_features):
			if (k + 1) not in current_set_of_features:
				print("--Considering adding the", str(k + 1), "feature")
				#print(current_set_of_features)
				accuracy = leave_one_out(data, current_set_of_features, k + 1, flag)
				print("accuracy: " + str(accuracy))
				if accuracy > best_so_far_accuracy:
					best_so_far_accuracy = accuracy
					best_so_far_features = current_set_of_features.copy()
					#print(best_so_far_features)
					tempacc = accuracy
					feature_to_add_at_this_level = k + 1
				if best_so_far_accuracy > best_accuracy:
					#print("TESTING:", best_so_far_accuracy, best_accuracy)
					#print("TESTING FEATURES:", best_so_far_features, best_set_of_features)
					best_accuracy = best_so_far_accuracy
					best_set_of_features = best_so_far_features
					#print("Before Removal:", best_set_of_features)
					#print(k + 1)
					best_set_of_features.append(k + 1)
					#print("After Removal:", best_set_of_features)
		current_set_of_features.append(feature_to_add_at_this_level)
		print("On level", str(i + 1), ", I added feature", str(feature_to_add_at_this_level), "to current set")
		#print(current_set_of_features)
		print(best_accuracy, best_set_of_features)		
		#print(feature_to_add_at_this_level + 1)
	return(tempacc, current_set_of_features, best_accuracy, best_set_of_features)	

def backward_elimination(data, num_features):
	flag = 1
	best_accuracy = 0
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
					best_so_far_features = current_set_of_features.copy()
					#print(best_so_far_features)
					feature_to_remove_at_this_level = k + 1
				if best_so_far_accuracy > best_accuracy:
					#print("TESTING:", best_so_far_accuracy, best_accuracy)
					#print("TESTING FEATURES:", best_so_far_features, best_set_of_features)
					best_accuracy = best_so_far_accuracy
					best_set_of_features = best_so_far_features
					#print("Before Removal:", best_set_of_features)
					#print(k + 1)
					best_set_of_features.remove(k + 1)
					#print("After Removal:", best_set_of_features)
		current_set_of_features.remove(feature_to_remove_at_this_level)

		#best_set_of_features = current_set_of_features.copy()
		print("On level", str(i + 1), ", I removed feature", str(feature_to_remove_at_this_level), "from current set")
		print(best_accuracy, best_set_of_features)

def special_algorithm(data, num_features):
	flag = 0
	best_accuracy = 0
	best_set_of_features = []
	current_set_of_features = []
	for i in range(num_features):
		print("On the", str(i + 1), "th level of the search tree")
		feature_to_add_at_this_level = 0
		best_so_far_accuracy = 0
		best_so_far_features = []
		temp = best_accuracy
		for k in range(num_features):
			if (k + 1) not in current_set_of_features:
				print("--Considering adding the", str(k + 1), "feature")
				#print(current_set_of_features)
				accuracy = leave_one_out(data, current_set_of_features, k + 1, flag)
				print("accuracy: " + str(accuracy))
				if accuracy > best_so_far_accuracy:
					best_so_far_accuracy = accuracy
					best_so_far_features = current_set_of_features.copy()
					#print(best_so_far_features)
					feature_to_add_at_this_level = k + 1
				if best_so_far_accuracy > best_accuracy:
					#print("TESTING:", best_so_far_accuracy, best_accuracy)
					#print("TESTING FEATURES:", best_so_far_features, best_set_of_features)
					best_accuracy = best_so_far_accuracy
					best_set_of_features = best_so_far_features
					#print("Before Removal:", best_set_of_features)
					#print(k + 1)
					best_set_of_features.append(k + 1)
					#print("After Removal:", best_set_of_features)
		if temp == best_accuracy:
			break
		current_set_of_features.append(feature_to_add_at_this_level)
		print("On level", str(i + 1), ", I added feature", str(feature_to_add_at_this_level), "to current set")
		#print(current_set_of_features)
		print(best_accuracy, best_set_of_features)		
		#print(feature_to_add_at_this_level + 1)



if __name__ == "__main__":

	data = []
	#norm_data = []
	#features = []
	num_features = 0
	num_instances = 0
	acc = 0
	#mean = []
	#stand_dev = []
	tot = []


	filename = input("Please enter the name of the file to test: ")

	try:
		f = open(filename, "r")

	except:
		print("The file " + filename + " doesn't exist")


	algorithm = input("Type the number of algorithm you want to run:\n" +
		"1) Forward Selection\n" + 
		"2) Backward Elimination\n" +
		"3) Special Algorithm\n")
	#filename = "./CS170_SMALLtestdata__15.txt"
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

	data = normalize(data, num_features)
	
	#acc = leave_one_out(data, num_instances, num_features)
	#print("Running nearest neighbor with all", num_features, "features, using \"leaving-one-out\" evaluation, I get an accuracy of", acc)

	if algorithm == "1":
		tot = forward_selection(data, num_features)
	elif algorithm == "2":
		backward_elimination(data, num_features)
	elif algorithm == "3":
		special_algorithm(data, num_features)
	else:
		print("Invalid Option")

#print("Running nearest neighbor with all", num_features, "features, using \"leaving-one-out\" evaluation, I get an accuracy of", tot[0])	

	#forward_selection(data, num_features)
	#backward_elimination(data, num_features)
'''
	for i in range(1, num_features + 1):
		features = []
		for row in data:
			features.append(row[i])
			print(features)
'''