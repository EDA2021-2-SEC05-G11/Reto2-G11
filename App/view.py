"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from time import process_time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("A- Cargar información en el catálogo: ")
    print("B- Crear indices (MAPS) por medio: ")
    print("C- Mostrar obras por medio: ")
    print("D- Crear indices (MAPS) por nacionalidad: ")
    print("E- Saber numero de obras por nacionalidad: ")
    print("1- REQ. 1: listar cronológicamente los artistas: ")
    print("2- REQ. 2: listar cronológicamente las adquisiciones")
    print("3- REQ. 3: clasificar las obras de un artista por técnica ")
    print("4- REQ. 4: clasificar las obras por la nacionalidad de sus creadores: ")
    print("5- REQ. 5: transportar obras según un departamento del museo ")


catalog = None

"""
Menu principal
"""
def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)
while True:

    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if  str(inputs[0]).lower() == "a":
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Autores cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        
    elif str(inputs[0]).lower() == "b":
        print(controller.pruebauno(catalog))
        print(process_time())
    elif str(inputs[0]).lower() == "c":
        Medio = str(input("Digite el medio: "))
        controller.medio(catalog, Medio)

    elif str(inputs[0]).lower() == "d":
        print(controller.nacionalidad_(catalog))
        print(process_time())
    elif str(inputs[0]).lower() == "e":
        nacionalidad = str(input("Digite la nacionalidad: "))
        controller.buscar_por_nacio(catalog, nacionalidad)

    elif int(inputs[0]) == 1:
        añoini =int(input("Digite el año inicial: ")) 
        añofini = int(input("Digite el año final: "))
        controller.r1(catalog, añoini, añofini)

    elif int(inputs[0]) == 2:

        print("Para ingresar la fecha siga las siguientes indicaciones\n")
        anio_inicial = str(int(input("Digite el año inicial del rango cronologico: ")))
        mes_inicial = str(int(input("Digite el mes inicial del rango cronologico : ")))
        dia_inicial = str(int(input("Digite el dia inicial del rango cronologico: ")))

        fecha_inicial= anio_inicial + "-" + mes_inicial + "-" + dia_inicial

        anio_final = str(int(input("Digite el año final del rango cronologico: ")))
        mes_final = str(int(input("Digite el mes final del rango cronologico: ")))
        dia_final = str(int(input("Digite el dia final del rango cronologico: ")))

        fecha_final= anio_final + "-" + mes_final + "-" + dia_final

        print (controller.req2(catalog, fecha_inicial, fecha_final))

    elif int(inputs[0]) == 3:
        
        nombre=str(input("Ingrese el nombre del artista: \n"))
        print(controller.req3(catalog, nombre))
    
    elif int(inputs[0]) == 4:
        controller.req4(catalog)

    elif int(inputs[0]) == 5:
        
        departamento=str(input("Ingrese el nombre del departamento del museo: \n"))
        controller.req5(catalog, departamento)

    else:
        sys.exit(0)
sys.exit(0)
