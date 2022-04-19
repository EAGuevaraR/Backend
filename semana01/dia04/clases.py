#crear clase
class Automovil:
  #crear atributos
  def __init__(self,aa,pl,col,mar):
    self.año = aa
    self.placa = pl
    self.color = col
    self.marca = mar

  #crear metodos
  def encender(self):
    print('encender ' + self.marca)
  def avanzar(self):
    print('avanzar ' + self.marca)
  def acelerar(self):
    print('acelerar ' + self.placa)
  def frenar(self):
    print('frenar ' + self.color) 

#crear objetos
vw = Automovil(1970, 'CH-1234', 'Amarillo', 'Volkswagen')
print("se creó el objeto vw con los datos:")
print("año : " + str(vw.año))
print("placa : " + vw.placa)
print("marca : " + vw.marca)
print("color : " + vw.color)


tico = Automovil(1998 , 'AB-132', 'Verde', 'Daewoo')
lamborghini = Automovil(2018,'gjh-1321', 'Azul', 'Lamborghini')

#utilizar objetos
vw.encender()
tico.encender()
tico.frenar()
lamborghini.frenar()


 