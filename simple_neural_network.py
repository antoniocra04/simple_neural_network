# importing numpy
import numpy as np 

#variable for decrease learning
alpha = 0.1

#training data for learning 
training_inputs = np.array([[0,0,1],
							[0,1,1],
							[1,0,1],
							[1,1,1],])

#set random seed
np.random.seed(1)

#random weights
weights = 2 * np.random.random((3)) - 1

#true answers on training data
training_goals = np.array([0,1,0,1])

#variabel for final result
final_results = ""

#lerning
for i in range(40):
	for x in range(len(training_inputs)):
		#neural network
		prediction = training_inputs[x].dot(weights) #calculating prediction

		delta = prediction - training_goals[x] #calculating delta for weights

		weights = weights - alpha * (training_inputs[x] * delta) #learning weights

		#final results
		if(i == 39):
			final_results = final_results + " " + str(abs(round(prediction)))

print(final_results)



