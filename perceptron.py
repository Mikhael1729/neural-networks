class Axon:
  def __init__(self, id, weight, start, end):
    self.id = id
    self.weight = weight
    self.start = start
    self.end = end

class Perceptron:
  def __init__(self, id, threshold, adjacents={}):
    self.id = id
    self.threshold = threshold
    self.adjacents = adjacents

class PerceptronsNeuralNetwork:
  def __init__(self, default_threshold=3, default_weight=2):
    self.perceptrons = {}
    self.axons = []
    self.default_threshold = default_threshold
    self.default_weight = default_weight

  def generate_axon_id(self):
    last = self.axons[-1] if self.axons else 0
    new_id = last + 1

    return new_id

  def add_perceptron(self, treshold):
    new_id = len(self.perceptrons) + 1

    new_perceptron = Perceptron(
      new_id = new_id,
      threshold = self.default_threshold,
      weight = self.default_weight
    )

    # TODO: self.perceptrons = 



    
