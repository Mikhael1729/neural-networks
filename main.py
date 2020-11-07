from perceptrons_neural_network import PerceptronsNeuralNetwork

network = PerceptronsNeuralNetwork()

# Create neurons
p1 = network.add_input(0)
p2 = network.add_input(1)
p3 = network.add()
p4 = network.add()
p5 = network.add()
p6 = network.add()
p7 = network.add()

# Connect them.
network.connect(p1.id, p3.id)
network.connect(p2.id, p3.id)
network.connect(p3.id, p4.id)
network.connect(p3.id, p5.id)
network.connect(p3.id, p6.id, weight=-4)
network.connect(p4.id, p7.id)
network.connect(p5.id, p7.id)

