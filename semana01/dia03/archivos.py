f = open ('alumnos.txt', 'w')
f.write('ernesto Guevara, eaguevarar@hotmail.com, 22222\n')
f.write('jose,jose@gmail.com,2222\n')
f.write('maria, maria@ttt.com,2222\n')

f= open ('alumnos.txt','r')
alumnos = f.read()
print(alumnos)

listaAlumnos = alumnos.splitlines()
print(listaAlumnos)

listaResultado = []

for dictAlumno in listaAlumnos:
  listaDiccionarioAlumnos = dictAlumno.split(',')
  print(listaDiccionarioAlumnos)
  dictAlumno = {
    'nombre' : listaDiccionarioAlumnos[0],
    'email' : listaDiccionarioAlumnos[1],
    'celular' : listaDiccionarioAlumnos[2]
  }
  listaResultado.append(dictAlumno)

print(listaResultado)
f.close 