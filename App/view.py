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
    print("1- Cargar información en el catálogo: ")
    print("2- Crear indices (MAPS) por medio: ")
    print("3- Mostrar obras por medio: ")
    print("4- Crear indices (MAPS) por nacionalidad: ")
    print("5- Saber numero de obras por nacionalidad: ")


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

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Autores cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        
    elif int(inputs[0]) == 2:
        print(controller.pruebauno(catalog))
        print(process_time())
    elif int(inputs[0]) == 3:
        Medio = str(input("Digite el medio: "))
        controller.medio(catalog, Medio)

    elif int(inputs[0]) == 4:
        print(controller.nacionalidad_(catalog))
        print(process_time())
    elif int(inputs[0]) == 5:
        nacionalidad = str(input("Digite la nacionalidad: "))
        controller.buscar_por_nacio(catalog, nacionalidad)
    else:
        sys.exit(0)
sys.exit(0)
