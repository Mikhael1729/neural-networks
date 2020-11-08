from perceptrons_network import PerceptronsNetwork
from layer import Layer

network = PerceptronsNetwork()

# Create neurons
p1 = network.add(value=1, layer_side=Layer.INPUT)
p2 = network.add(value=1, layer_side=Layer.INPUT)
p3 = network.add()
p4 = network.add()
p5 = network.add()
p6 = network.add(layer_side=Layer.OUTPUT)
p7 = network.add(layer_side=Layer.OUTPUT)

# Connect them.
network.connect(p1.id, p3.id)
network.connect(p1.id, p4.id)
network.connect(p2.id, p3.id)
network.connect(p2.id, p5.id)
network.connect(p3.id, p4.id)
network.connect(p3.id, p5.id)
network.connect(p3.id, p6.id, weight=-4)
network.connect(p4.id, p7.id)
network.connect(p5.id, p7.id)

# Print result
network.fire()

print("After fire \n---\n")
print(f"carry: {p6}")
print(f"sum: {p7}")
