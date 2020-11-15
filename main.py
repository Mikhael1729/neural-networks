from perceptrons_network import PerceptronsNetwork
from layer import Layer
from notes_numbers import notes_numbers
from chord_modes import chord_modes, Chord

chord = Chord("Si", "Re", "Fa#")
print(chord)

"""
- ¿Cómo conocer el nombre de un acorde?:

  - Resta de semitonos:
    
    - Si la Tercera o la Quinta es menor que la última nota (12) sumar esta a la pertinente
    - Realizar este cálculo: |Fundamental + Tercera| - |Fundamental + Quinta|
    - Identificar el nombre del acorde usando esta regla:

      (Resta de semitonos, posición)
      
      Aplicándola, sería así:

      (3, 1), (7, 3), (4, 2)

  - A general form:

    Ignore the semitonestj

  - Mode of a chord:
    
    - Know the fundamental note `first_position`
    - Get the normalized positions of each note by substracting `m - 1` where `m` is the position of the
      first note of the chord
    - The sum of the positions encode the mode of the chord. The following are the founded rules:

	self.chord_modes = {
	  15: "Aumentado",
	  14: "Mayor",
	  13: "Menor",
	  12: "Disminuido"
	}


"""



