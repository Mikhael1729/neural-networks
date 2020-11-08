from axon import Axon
from enum import Enum
from perceptron import Perceptron

class Layer(Enum):
  INPUT = 1
  HIDDEN = 2
  OUTPUT = 3

"""
Holds the set of neurons and connections between them via
a graph representation.
"""
class PerceptronsNetwork:
  def __init__(self, default_threshold=3, default_weight=-2):
    self.__perceptrons = {} # The nodes.
    self.__axons = [] # The edges.
    self.__perceptrons_inputs = {} # Register the input axons for each perceptron.

    self.__default_threshold = default_threshold
    self.__default_weight = default_weight

    # Locate the index of each perceptron for each layer.
    self.__inputs = []
    self.__outputs = []
    self.__hiddens = []

  @property
  def perceptrons(self):
    return self.__perceptrons

  @property
  def input_layer(self):
    inputs = []
    for id in self.__inputs:
      inputs.append(self.__perceptrons[id])

    return inputs

  @property
  def input_layer(self):
    hiddens = []
    for id in self.__hiddens:
      hiddens.append(self.__perceptrons[id])

    return hiddens

  @property
  def output_layer(self):
    outputs = []
    for id in self.__outputs:
      outputs.append(self.__perceptrons[id])

    return outputs

  def add_input(self, value=0):
    new_id = self.__generate_next_perceptron_id() 
    new_perceptron = Perceptron(
      id=new_id,
      value=value,
      threshold=self.__default_threshold,
      layer_side=Layer.INPUT
    )

    self.__perceptrons[new_id] = new_perceptron
    self.__inputs.append(new_id)

    return new_perceptron

  def add(self, threshold=None, value=None):
    new_id = self.__generate_next_perceptron_id() 
    threshold_value = threshold if threshold else self.__default_threshold

    new_perceptron = Perceptron(id=new_id, threshold=threshold_value)

    self.__perceptrons[new_id] = new_perceptron
    self.__perceptrons_inputs[new_id] = []

    self.__hiddens.append(new_id)

    return new_perceptron

  def add_output(self):
    new_id = self.__generate_next_perceptron_id() 
    new_perceptron = Perceptron(
      id=new_id,
      threshold=self.__default_threshold,
      layer_side=Layer.OUTPUT
    )

    self.__perceptrons[new_id] = new_perceptron
    self.__perceptrons_inputs[new_id] = []

    self.__outputs.append(new_id)

    return new_perceptron

  def connect(self, source, destination, weight=None):
    # Create axon.
    destination_perceptron = self.get_perceptron(destination)

    if destination_perceptron.layer_side == Layer.INPUT:
      raise Exception("Inputs can't have destination axons")

    source_perceptron = self.get_perceptron(source)

    new_axon = Axon(
      id=self.__generate_next_axon_id(),
      source= source_perceptron,
      destination=destination_perceptron,
      weight=self.__default_weight if not weight else weight
    )

    # Register axon.
    self.__axons.append(new_axon)
    
    # Register adjacents. TODO: Do parameters validations and evaluate the use of the axon in the array or the object.
    self.__perceptrons[source].adjacents.append(new_axon)

    # Register in perceptron_inputs
    if  self.__perceptrons_inputs:
      self.__perceptrons_inputs[destination].append(new_axon)
    else:
      self.__perceptrons_inputs[destination] = [new_axon]

    return new_axon

  def get_perceptron(self, id):
    if not isinstance(id, int):
      raise Exception(f"The indicated perceptron ({id}) does not exists")

    last_perceptron_id = self.__get_last_perceptron_id()
    id_exists = id > 0 and id <= last_perceptron_id

    if id_exists:
      return self.__perceptrons[id]
    else:
      raise Exception(f"The indicated perceptron ({id}) does not exists")

  # Start the network computation.
  def fire(self):
    # The order of execution is guided by the order of perceptrons registration.
    for id in self.__perceptrons_inputs:
      input_axons = self.__perceptrons_inputs[id]
      perceptron = self.__perceptrons[id]

      perceptron.update_value(input_axons)

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
