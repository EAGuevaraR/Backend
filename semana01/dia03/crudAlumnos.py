import tabulate
from libAlumnos import buscarAlumno
from libAlumnos import menu
from libAlumnos import insertarAlumno
from libAlumnos import actualizarAlumno
from libAlumnos import eliminarAlumno
from libAlumnos import cargarAlumnos
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D

menu ()
opcion = 0
#alumnos = [{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'232323'}]

f = open('alumnos.txt','r')
strAlumnos = f.read()
alumnos = cargarAlumnos(strAlumnos)
f.close

while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        insertarAlumno(alumnos)
   
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        #Paso 1 buscar el alumno a editar
        valorBusqueda=input("Ingrese el email del alumno a actualizar : ")
        indexAlumno = buscarAlumno(valorBusqueda,alumnos)

        #paso 2 ingresar los nuevos valores para el alumnos a editar
        if (indexAlumno == -1):
            print("No se encontró el email del alumno")
        else:
           actualizarAlumno(indexAlumno,alumnos)
   
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        #paso1 buscar el alumno a eliminar
        valorEliminar = input ("Ingrese el email del alumno a eliminar : ")
        indexAlumno = buscarAlumno(valorBusqueda,alumnos)
        
        if (indexAlumno == -1):
          print("No se encontró el email del alumno")
        else:
          #ELIMINAR EL ALUMNO
          eliminarAlumno(indexAlumno,alumnos)
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
   
    else:
        print("OPCION INCORRECTA")