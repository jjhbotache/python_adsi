""" 
Continúe con el ejercicio anterior, y añada a la clase 4 propiedades que calculen el
número total de cada una de las bases presentes en la secuencia.
""" 
from ejer_cap6_r1 import adn_sequence

class adn_sequence_2(adn_sequence):
  """_summary_
      This is a class that inherit from an adn_sequence created in a 
      ejer_cap6_r1 file and it's imported to be inheritanced
    Args:
      sequence (str): an ADN sequence in a string as "AGCTAGCTAGCTAGCT"
    """
  def __init__(self,sequence):
    super().__init__()
    sequence=sequence.upper()
    for i in sequence:
      if i == 'A':
        self.A += 1
      elif i == 'C':
        self.C += 1
      elif i == 'G':
        self.G += 1
      elif i == 'T':
        self.T += 1
             