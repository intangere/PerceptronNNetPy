from random import random, choice

inputs = [([.1, 0], .1),\
		  ([.1, .2], .3),\
		  ([.3, .2], .5),\
		  ([.4, .3], .7)]

weights = [float(str(random())),\
		   float(str(random()))]

threshold = .5
learning_rate = .2
epochs = 0
errors = []

def step(x):
	#Let's just return the weight
	return x

def dot(x, w):
	return sum([x[i] * w[i] for i in range(len(x))])

def multiply_all(x, w):
	return [x[i] * w[i] for i in range(len(x))]

def update_weights(i, error):
	for idx, weight in enumerate(weights):
		weights[idx] += i[idx] * error * learning_rate	

while True:
	i, expected = choice(inputs)
	delta_wji = dot(weights, i)
	error = expected - step(delta_wji)
	update_weights(i, error)
	epochs += 1
	if epochs % 200000 == 0:
		for q, expected in inputs:
			print "%s -> %s" % (q, step(dot(q, weights)))
		print weights
		break


#happy, petting -> happy
#happy, leash -> sad
#sad, leash -> sad
#mad, leash -> super mad