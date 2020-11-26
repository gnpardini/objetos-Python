class NumeroComplejo:
  
  def __init__(self,valorY,valorX):
    self.valorY = valorY
    self.valorX = valorX

  def getNumeroComplejo(self):
    numeroComplejo = self.valorY + self.valorX
    return numeroComplejo



numeroComplejo1 = NumeroComplejo(5,6)
numeroComplejo1.getNumeroComplejo()
print(numeroComplejo1.getNumeroComplejo())