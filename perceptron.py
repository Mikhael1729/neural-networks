from enum import Enum
from abc import ABC

class Layer(Enum):
  INPUT = 1
  HIDDEN = 2
  OUTPUT = 3

"""
Perceptron representation
"""
class Perceptron:
  def __init__(self, id, threshold=None, adjacents=[], value=None, layer_side=Layer.HIDDEN):
    self.id = id
    self.threshold = threshold
    self.adjacents = adjacents # Holds the list of connected perceptrons (Axon)
    self.value = value
    self.layer_side = layer_side

  def __str__(self):
    return f"Perceptron(id: {self.id}, value: {self.value})"
  
  # Update the value of the perceptron depending on its inputs (axons)
  def update_value(self, input_axons):
    if self.layer_side == Layer.INPUT:
      return self.value

    # Sum each weight with each input value
    result = 0
    for axon in input_axons:
      weight = axon.weight # int
      input_value = axon.source # int

      result = result + (weight * axon.source.value)

    # Add the bias.
    bias = self.threshold
    result = result + bias

    # Set value
    self.value = 0 if result <= 0 else 1

    return self.value
