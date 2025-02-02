from enum import Enum
from abc import ABC
from layer import Layer

"""
Perceptron representation
"""
class Perceptron:
  def __init__(self, id, threshold=None, value=None, layer_side=Layer.HIDDEN):
    self.id = id
    self.threshold = threshold if not(layer_side == Layer.INPUT) else None
    self.value = value 
    self.layer_side = layer_side

  def __str__(self):
    return f"Perceptron(id: {self.id}, value: {self.value})"
  
  # Update the value of the perceptron depending on its inputs (edges). It can be used in a network firing.
  def update_value(self, input_edges):
    if self.layer_side == Layer.INPUT:
      return self.value

    result = 0
    for edge in input_edges:
      weight = edge.weight
      input_value = edge.source

      result = result + (weight * edge.source.value)

    # Add the bias.
    bias = self.threshold
    result = result + bias

    # Set value
    self.value = 0 if result <= 0 else 1

    return self.value
