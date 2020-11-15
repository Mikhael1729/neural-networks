from notes_numbers import notes_numbers, s

chord_modes = {
  15: "Aumentado",
  14: "Mayor",
  13: "Menor",
  12: "Disminuido"
}

"""
The logic behind this is based on the chromatic scale
"""
class Chord:
  def __init__(self, first, second, third):
    self.__first_position = Chord.compute_position(first)
    self.__second_position = Chord.normalize_position(first, second)
    self.__third_position = Chord.normalize_position(first, third)

    self.__first = first
    self.__second = second
    self.__third = third

    self.__chord_names_rule = {
      1: 1, # Fundamental.
      5: 3, # First inversion.
      8: 2, # Second inversion.
    };

    self.chord_modes = {
      15: "Aumentado",
      14: "Mayor",
      13: "Menor",
      12: "Disminuido"
    }

  def __str__(self):
    return self.full_name

  @property
  def first(self):
    return self.__first

  @property
  def second(self):
    return self.__second

  @property
  def third(self):
    return self.__third

  @property
  def full_name(self):
    full_name = f"{self.name} {self.mode}"
    return full_name

  @staticmethod
  def normalize_position(first, next_note):
    position_first = Chord.compute_position(first)
    position_next = Chord.compute_position(next_note)
    # print(':: position_next', position_next)


    if position_next < position_first:
      last_position = Chord.get_last_position()
      normalized = last_position + position_next
      return normalized
    else:
      return position_next


  @property
  def name(self):
    #second_position = self.__second_position 
    subtrahend = self.__first_position - 1
    first = self.__first_position - subtrahend

    name_place = self.__chord_names_rule[first]

    if name_place == 1:
      return self.first
    elif name_place == 2:
      return self.second
    else:
      return self.third

  @property
  def mode(self):
    subtrahend = self.__first_position - 1
    normalized_position1 = self.__first_position - subtrahend
    normalized_position2 = self.__second_position - subtrahend
    normalized_position3 = self.__third_position - subtrahend

    mode_number = normalized_position1 + normalized_position2 + normalized_position3
    mode_name = self.chord_modes[mode_number]

    return mode_name

  @staticmethod
  def compute_position(note):
    position =  notes_numbers[note]
    return position

  @staticmethod
  def get_last_position():
    last_position =  s[len(s) - 1]
    return last_position
