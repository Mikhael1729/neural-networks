"""
It's the edge between two neurons.
"""
class Axon:
  def __init__(self, id, weight, source, destination):
    self.id = id
    self.weight = weight
    self.source = source
    self.destination = destination
