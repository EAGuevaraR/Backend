#clase para administrar los usuarios de un sistema
class Usuario:
  def __init__(self,nom,pwd):
    self.nombre = nom
    self.password = pwd

  def iniciarSesion(self):
    if (self.nombre == 'admin' and self.password == '12345'):
      print("Bienvenido " + self.nombre)
    else:
      print("Datos de acceso incorrectos")

#Usando mi clase Usuario
usuario1 = Usuario('admin', 'admin')
usuario1.iniciarSesion()

usuario2 = Usuario('admin', '12345')
usuario2.iniciarSesion()