from random import *
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
lista = []
sueldos = []

def inicio():
    menus=True
    while menus:
        menu=('1. Asignar sueldos aleatorios','2. Clasificar sueldos','3. Ver estadísticas.','4. Reporte de sueldos','5. Salir del programa')
        try:
            for i in menu:
                print(i)
            op = int(input("**Ingrese una opcion**"))
            if op == 1:
                asignar(trabajadores)
            elif op == 2:
                    clasificar(lista)
            elif op == 3:
                    estadisticas(lista)
            elif op == 4:
                    reporte(lista)
            elif op == 5:
                    salir()
                    menus = False
            else:
                print("**Debes ingresar un  numero entre el 1-5")
        except ValueError:
                print("**Debes ingresar un numero**")

def asignar(trabajador):
    for i in trabajador:
        sueldo = randint(300000,2500000)
        lista.append({"Nombre empleado":i,
                      "Sueldo":sueldo
                      })
    print("Sueldos asignados con exito**")
    return lista

def  clasificar(lista):
    menoresA800 =[]
    entre800Y2M = []
    mayor2M = []
    
    for i in lista:
        if i['Sueldo'] <= 800000:
            menoresA800.append(i)
        elif i['Sueldo'] >= 800000 and i['Sueldo'] <= 2000000: 
            entre800Y2M.append(i)
        elif i['Sueldo']> 2000000: 
            mayor2M.append(i)

    print(f"**Sueldos menores a $800.000 TOTAL {len(menoresA800)} **\n")
    print("Nombre Empleado", "   Sueldo" )
    for i in menoresA800:
        print( i["Nombre empleado"],    "$",i['Sueldo'])

    print(f"**Sueldos entre  $800.000 y $2.000.000 TOTAL {len(entre800Y2M)} ** \n")
    print("Nombre Empleado" ,  "   Sueldo" )
    for i in entre800Y2M:
        print( i["Nombre empleado"],    "$",i['Sueldo'])
    
    print(f"**Sueldos superiores a $2.000.000 TOTAL {len(mayor2M)} ** \n")
    print("Nombre Empleado" ,  "   Sueldo " )

    for i in mayor2M:
        print( i["Nombre empleado"],    "$",i['Sueldo'])

def estadisticas(lista):
    contador = 0
    # prueba=1
    # media = 0
    for i in lista:
        sueldos.append(i['Sueldo'])
        contador+=i['Sueldo']
        # media += i['Sueldo'] ** prueba
    sueldoMaximo = max(sueldos)
    sueldoBajo = min(sueldos)
    sueldoPromedio = contador / len(lista)
    print("*** El sueldo mas ALTO es: " ,sueldoMaximo, "***")
    print("*** El sueldo mas BAJO es: " ,sueldoBajo, "***")
    print("*** El sueldo PROMEDIO es: " ,sueldoPromedio, "***")
    # print("*** La MEDIA GEOMETRICA es: " ,media, "***")

def reporte(lista):
    todo= []
    nombre=[]
    sueldo=[]
    descSalud=[]
    descAfp=[]
    sueldoLiquido=[]
   
    for i  in lista:
        nombre.append(i["Nombre empleado"])
        sueldo.append(i['Sueldo'])
    print("nombre empleado")
    for i in sueldo:
        salud = i * 0.07
        afp= i * 0.12
        descSalud.append(salud)
        descAfp.append(afp)
        liquido = i -salud - afp
        sueldoLiquido.append(liquido)
    with open("archivo.csv","a", newline='') as archivo:
        datos = csv.writer(archivo)
        datos.writerow(["Nombre empleado","Sueldo base","Descuento salud","Descuento AFP", "Sueldo Liquido"])
        print("Nombre Empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido")
   
        todo.append({"Nombre empleado":nombre,
                      "Sueldo":sueldo,
                       "Descuento Salud":descSalud,
                       "Descuento AFP":descAfp,
                       "Sueldo Liquido":sueldoLiquido})
        datos.writerow([todo])
    
    for i in todo:
        print(i["Nombre empleado"],i["Sueldo"],i["Descuento Salud"],i["Descuento AFP"],i["Sueldo Liquido"])

def salir():
    print("Finalizando Programa")
    print("Desarrollado por Geraldine Becerra")
    print("RUT 18.795.772-9")
  
inicio()

