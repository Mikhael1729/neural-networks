from axon import Axon
from perceptron import Perceptron, PerceptronInput

"""
Holds the set of neurons and connections between them via
a graph representation.
"""
class PerceptronsNeuralNetwork:
  def __init__(self, default_threshold=3, default_weight=-2):
    self.__perceptrons = {} # The nodes.
    self.__axons = [] # The edges.
    self.__default_threshold = default_threshold
    self.__default_weight = default_weight

  def add(self, threshold=None, weight=None, is_input=False):
    new_id = self.__generate_next_perceptron_id() 
    threshold_value = threshold if threshold else self.__default_threshold

    new_perceptron = Perceptron(id = new_id, threshold = threshold_value)

    self.__insert_perceptron(new_perceptron)

    return new_perceptron

  def add_input(self, value=0):
    new_id = self.__generate_next_perceptron_id()
    new_input = PerceptronInput(id=new_id, value=value)

    self.__insert_perceptron(new_input)

    return new_input

  def __insert_perceptron(self, perceptron):
    self.__perceptrons[perceptron.id] = perceptron

  def connect(self, source, destination, weight=None):
    axon = Axon(
      id=self.__generate_next_axon_id(),
      source=self.get_perceptron(source),
      destination=self.get_perceptron(destination),
      weight=self.__default_weight if not weight else weight
    )

    # Register axon.
    self.__axons.append(axon)
    
    # Register adjacents. TODO: Do parameters validations.
    self.__perceptrons[source].adjacents.append(axon)

  def get_perceptron(self, id):
    if not isinstance(id, int):
      return None

    last_axon_id = self.__get_last_axon_id()
    id_exists = id > 0 and id <= last_axon_id

    return self.__perceptrons[id] if id_exists else None

  def __generate_next_axon_id(self):
    last = self.__get_last_axon_id()
    new_id = last + 1

    return new_id

  def __get_last_axon_id(self):
    last = self.__axons[-1].id if self.__axons else 0
    return last

  def __generate_next_perceptron_id(self):
    last = self.__get_last_perceptron_id()
    new_id = last + 1

    return new_id

  def __get_last_perceptron_id(self):
    last = len(self.__perceptrons)

    return last
