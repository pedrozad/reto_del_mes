import Bloque
import datetime 

class Cadena:
  def __init__(self, data):
    """Variables de inicialización necesarios para por lo menos identificar el primer bloque y/o el último bloque. Otras variables también podrán ser agregadas"""
    timestamp = datetime.datetime.utcnow()
    # A chain cannot contain empty blocks 
    # First Bloque
    try:
      first_bloque = Bloque.Bloque(timestamp,data,"0")
    except TypeError:
      raise TypeError("Data cannot be neither None nor an empty string")
    # A chain like a list
    self.chain = [first_bloque]
    

  def agregar_bloque(self, data):
    """Agrega un bloque a la cadena. Tomar en consideración que el primer bloque es especial porque no tiene previous_hash. Retorna True si la operación es exitosa, False de lo contrario. Considerar retornar con Error si se trata de algun caso especial"""
    try:
      aux_block = self.chain[-1]
      timestamp = datetime.datetime.utcnow()
      new_block = Bloque.Bloque(timestamp,data,aux_block.hash)
      self.chain.append(new_block)
      return True
    except TypeError as identifier:
      raise TypeError("agregar_bloque. The data is invalid")
    else:
      print("Error in memory?")
    return False

  def verificar_integridad(self):
    """Revisa la integridad de la cadena, bloque por bloque, asegurandose previous_hash sea igual al hash del bloque previo. Retorna False si la verificación no es exitosa, True de lo contrario"""
    boolean = True
    chainLength = len(self.chain)
    # Iterated from the begin to the end of the chain
    # auxPrevHash helps to save the hash of the previous block
    auxPrevHash = 0
    for i in range(0,chainLength):
      auxBlock = self.chain[i]
      if str(auxPrevHash) != str(auxBlock.previous_hash) :
        #print(str(auxPrevHash))
        #print(str(auxBlock.previous_hash))
        return False
      auxPrevHash = self.chain[i].hash

    return boolean

  def crear_fork(self):
    """Copia la cadena entera o un segmento de ella desde un punto en adelante. Retorna una Cadena. [OPCIONAL]"""

  def __str__(self):
    """Representación en un string de una cadena. Tambien podrá ser utilizando def __repr__(self) si prefiere [OPCIONAL]"""
    string = ""
    string += "[1] -> data: " + str(self.chain[0].data)
    for counter in range(1,len(self.chain)):
      string +="\n["+ str(counter+1) + "] -> data: " + str(self.chain[counter].data)
    return string
