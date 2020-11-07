"""
Perceptron neuron representation
"""
class Perceptron:
  def __init__(self, id, threshold, adjacents=[], is_input=False):
    self.id = id
    self.threshold = threshold
    self.adjacents = adjacents # Holds the list of connected perceptrons (Axon)
    self.is_input = is_input

