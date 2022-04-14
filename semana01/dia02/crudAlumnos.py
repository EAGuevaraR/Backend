import tabulate
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
print("-" * 50)
print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "* 8 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES     " + " "* 18 + "|")
print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " "* 18 + "|")
print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " "* 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " "* 18 + "|")
print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " "* 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " "* 18 + "|")
print("-" * 50)
opcion = 0
alumnos = [{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'232323'}]
while(opcion != 5):
    opcion = int(input("INGRESE OPCIÓN DEL MENU :"))
    
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        nombre  = input("NOMBRE  : ")
        email   = input("EMAIL   : ")
        celular = input("CELULAR : ")
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)
        print("ALUMNO REGISTRADO CON EXITO!!!")
   
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras))
    
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        #Paso 1 buscar el alumno a editar
        valorBusqueda=input("Ingrese el email del alumno a actualizar : ")
        indexAlumno = -1
        for i in range(len(alumnos)):
          dicAlumnoBusqueda = alumnos[i]
          for clave,valor in dicAlumnoBusqueda.items():
            if(valor == valorBusqueda and clave == 'email'):
              indexAlumno=i
              break
        #print("el alumno esta en el indice : " + str(indexAlumno))
        #print("datos del alumno : " + str(alumnos[indexAlumno]))
        #paso 2 ingresar los nuevos valores para el alumnos a editar
        if (indexAlumno == -1):
          print("No se encontró el email del alumno")
        else:
          nombre  = input("NOMBRE  : ")
          email   = input("EMAIL   : ")
          celular = input("CELULAR : ")
          dictAlumnoEditar = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        #paso 3 actualizatr los datos del alumno a editar
        alumnos[indexAlumno] = dictAlumnoEditar
        print("ALUMNO ACTUALIZADO!!")
   
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        #paso1 buscar el alumno a eliminar
        valorEliminar = input ("Ingrese el email del alumno a eliminar : ")
        indexAlumno = -1
        for i in range(len(alumnos)):
          dicAlumnoBusqueda = alumnos[i]
          for clave,valor in dicAlumnoBusqueda.items():
            if(valor == valorBusqueda and clave == 'email'):
              indexAlumno=i
              break
        
        if (indexAlumno == -1):
          print("No se encontró el email del alumno")
        else:
          #ELIMINAR EL ALUMNO
          alumnos.pop(indexAlumno)
          print("ALUMNO ELIMINADO!!")

    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
   
    else:
        print("OPCION INCORRECTA")