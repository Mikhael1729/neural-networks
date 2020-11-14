from perceptrons_network import PerceptronsNetwork
from layer import Layer
from notes_numbers import notes_numbers
from chord_modes import chord_modes

# Assign weight automatically.
network = PerceptronsNetwork(default_threshold=0, default_weight=1)

note1 = notes_numbers["Do"]
note2 = notes_numbers["Mib"]
note3 = notes_numbers["Sol"]

# Create neurons
input_perceptrons = {
  network.add(value=1, layer_side=Layer.INPUT): note1,
  network.add(value=1, layer_side=Layer.INPUT): note2,
  network.add(value=1, layer_side=Layer.INPUT): note3,
}

output_perceptrons = [
  network.add(layer_side=Layer.OUTPUT, threshold=14),
  network.add(layer_side=Layer.OUTPUT, threshold=15),
  network.add(layer_side=Layer.OUTPUT, threshold=16),
  network.add(layer_side=Layer.OUTPUT, threshold=17)
]

# Connect them.
for key, value in input_perceptrons.items():
  for operceptron in output_perceptrons:
    network.connect(key.id, operceptron.id, weight=value)

# Compute the network.
network.fire()

# Print the result.
for perceptron in output_perceptrons:
  if perceptron.value == 1:
    print(chord_modes[perceptron.threshold])
    break
