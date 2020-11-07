"""
Perceptron neuron representation
"""
class Perceptron:
  def __init__(self, id, threshold, adjacents=[]):
    self.id = id
    self.threshold = threshold
    self.adjacents = adjacents # Holds the list of connected perceptrons (Axon)

class PerceptronInput:
  def __init__(self, id, adjacents=[], value=0):
    self.id = id
    self.adjacents = []
    self.value = value

