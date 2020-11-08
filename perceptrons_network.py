from axon import Axon
from perceptron import Perceptron
from layer import Layer

class PerceptronsNetwork:
  def __init__(self, default_threshold=3, default_weight=-2):
    self.__perceptrons = {}
    self.__perceptrons_inputs = {} # Stores all input axons for each perceptron.

    self.__last_axon_id = 0

    self.__default_threshold = default_threshold
    self.__default_weight = default_weight

    # Each of one of the following lists allows to locate the key of each perceptron 
    # in the corresponding layer side. 
    self.__inputs = []
    self.__outputs = []
    self.__hiddens = []

  def add(self, threshold=None, value=None, layer_side=Layer.HIDDEN):
    new_id = self.__generate_next_perceptron_id() 
    threshold_value = threshold if threshold else self.__default_threshold

    new_perceptron = Perceptron(
      id=new_id,
      threshold=threshold_value,
      value=value,
      layer_side=layer_side
    )

    # Store the perceptron.
    self.__perceptrons[new_id] = new_perceptron

    # Register the key the perceptron depending on its layer type.
    if layer_side == Layer.INPUT:
      self.__inputs.append(new_id)
    else:
      self.__perceptrons_inputs[new_id] = []

      if layer_side == Layer.OUTPUT:
        self.__outputs.append(new_id)
      else:
        self.__hiddens.append(new_id)

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

    # Save connection.
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

  # Starts the network computation. The order of execution is guided by the order of perceptrons registration.
  def fire(self):
    for id in self.__perceptrons_inputs:
      input_axons = self.__perceptrons_inputs[id]
      perceptron = self.__perceptrons[id]

      perceptron.update_value(input_axons)

  def __generate_next_axon_id(self):
    new_id = self.__last_axon_id + 1
    return new_id

  def __generate_next_perceptron_id(self):
    last = self.__get_last_perceptron_id()
    new_id = last + 1

    return new_id

  def __get_last_perceptron_id(self):
    return len(self.__perceptrons)
