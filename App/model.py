﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.Algorithms.Sorting import mergesort as me



"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():
    catalog = {'artists':None,
               'artworks':None,
               'Medium':None,
               'Nationality':None
    }
    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['Medium'] = mp.newMap(800,
                                   maptype='PROBING',
                                   loadfactor=0.50)
    catalog['Nationality'] = mp.newMap(69,
                                   maptype='PROBING',
                                   loadfactor=0.50)


    return catalog
# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)

def addArtworks(catalog, artworks):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artworks'], artworks)
# Funciones para creacion de datos

# Funciones de labratorios
def prueba(catalog):

    diccionario={}
    for i in range(1, lt.size(catalog['artworks'])+1):
        obra = lt.getElement(catalog['artworks'], i)
        if obra["Medium"] in diccionario:
           diccionario[obra["Medium"]].append(obra)
        else:
           diccionario[obra["Medium"]]=[obra]

    for i in diccionario.keys():

        mp.put( catalog['Medium'], i, diccionario[i])

    return(catalog["Medium"])

def buscarporMedio(catalog, medio):

    obras = mp.get(catalog['Medium'], medio)
    print(obras)

def comparacionDateAcquired(e1, e2): 
    e1 = e1['Date']
    e2 = e2['Date']
    p1 = None
    p2 = None

    if len(e1) > 0 :
        e1 = datetime.strptime(e1, '%Y-%m-%d') 
        p1 = True
    else:
        p1 = False

        
    if len(e2) > 0:
        e2 = datetime.strptime(e2, '%Y-%m-%d') 
        p2= True
    else:
        p2 = False

    if p1==False:
        return (False)
    if p2==False:
        return (False)
    if p1==True and p2==True:
    
     if e1 < e2:
        
        return (True)

     else:

        return(False)     

def obrasantiguas(catalog, numero, medio):
    Lista = lt.newList(datastructure='ARRAY_LIST')
    obras = mp.get(catalog['Medium'], medio)
    lt.addLast(Lista, obras)
    
    sub_list = lt.subList(Lista, 1, numero)
    sorted_list = me.sort(sub_list, comparacionDateAcquired) 
    
    return sorted_list

def nacionlidad(catalog):

    diccionario={}
    for i in range(1, lt.size(catalog['artists'])+1):
        obra = lt.getElement(catalog['artists'], i)
        if obra["Nationality"] in diccionario:
           diccionario[obra["Nationality"]].append(obra)
        else:
           diccionario[obra["Nationality"]]=[obra]

    for i in diccionario.keys():

        mp.put( catalog['Nationality'], i, diccionario[i])

    return(catalog["Nationality"])

def buscarporNacionalidad(catalog, nacionalidad):
    Lista = lt.newList(datastructure='ARRAY_LIST')
    obras = mp.get(catalog['Nationality'], nacionalidad)
    lt.addLast(Lista, obras)
    lista_mini=[]
    contador=0
    for i in lt. iterator(Lista):
        lista_mini.append(i['value'])
    for elem in lista_mini:
        for j in elem:
            contador+=1
    print("Existen "+str(contador)+" obras de la nacionalidad de "+ str(nacionalidad))

# Requerimientos

    




# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
