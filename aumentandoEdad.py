class Persona:

  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad
  
  def aumentarEn1LaEdad(self):
    edad = self.edad + 1
    print(edad)

  def __str__(self):
    return self.nombre


  
persona1 = Persona ("Gisela",23)
persona1.aumentarEn1LaEdad()
persona1.__str__()
