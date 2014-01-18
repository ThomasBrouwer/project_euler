# Same code as problem_18.py
def higher_val(a,b):
	return a if a > b else b

def find_max_path(layers):
	# We go bottom up, adding the highest of each two values next
	# to each other to the parent, until we reach the top
	for i in reversed(range(0,len(layers)-1)):
		layer = layers[i]
		layer_below = layers[i+1]
		for j in range(0,len(layer)):
			layer[j] += higher_val(layer_below[j],layer_below[j+1]) 
	return layers[0][0]

triangle = open("triangle.txt",'r').read()
layers = triangle.split("\n")
layers = [values.split() for values in layers]
layers = [
	[int(val) for val in layer]
	for layer in layers
]
layers = layers[:-1]
print find_max_path(layers)