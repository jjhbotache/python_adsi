""" 
Continúe con el ejercicio anterior, y añada a la clase un método de instancia para sumar
dos secuencias de ADN. La suma se hará base a base y el resultado será el máximo de
cada letra(base).
""" 
from ejer_cap6_r2 import adn_sequence_2

class adn_sequence_3(adn_sequence_2):
  def add_sequences(sequence1,sequence2):
    sequence = {
      A:0,
      C:0,
      G:0,
      T:0
    }
    for i in sequence1:
      if i == 'A':
        sequence[A] += 1
      elif i == 'C':
        sequence[C] += 1
      elif i == 'G':
        sequence[G] += 1
      elif i == 'T':
        sequence[T] += 1
    for i in sequence2:
      if i == 'A':
        A += 1
      elif i == 'C':
        C += 1
      elif i == 'G':
          G += 1
      elif i == 'T':
          T += 1
    return sequence          
          