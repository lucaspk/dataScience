from random import random

#Already consider the bias as one of the neuron's weight
#For convention, we inialize each neuron with a small random weight value (i.e. between 0 and 1)
#Each neuron is a dictionary: "weights" = key; an array with total_of_weights numbers(the weights) = value.
def gen_neurons(total_of_weights, total_of_neurons):
  bias = 1
  neuron_weights = [random() for each_weight in range(total_of_weights + bias)]
  neurons = [{"weights": neuron_weights} for each_neuron in range(total_of_neurons)]
  return neurons

def inialize_network(total_of_inputs, total_neurons_hidden_layer, total_neurons_output_layer):
  layers = []
  hidden_layer = gen_neurons(total_of_inputs, total_neurons_hidden_layer)
  layers.append(hidden_layer)
  output_layer = gen_neurons(total_neurons_hidden_layer, total_neurons_output_layer)
  layers.append(output_layer)
  return layers
