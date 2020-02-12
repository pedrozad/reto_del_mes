import hashlib

class Bloque:
  
  def __init__(self, timestamp, data, previous_hash):
    self.timestamp = timestamp
    # Raise a TypeError if the type of the data is None or if data is a
    # Empty String.
    if ((data is None) or  (not data) ):
        raise TypeError("The data is None or it is empty string")
    else:
        self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()

  def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "Bienvenido al reto del mes, Blockchain!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()