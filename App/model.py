"""
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


from App.controller import obrasmasantiguas
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.Algorithms.Sorting import mergesort as me
from datetime import datetime
from time import process_time



"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

def newCatalog():
    catalog = {'artists':None,
               'artworks':None,
               'Medium':None,
               'Nationality':None,
               'Begin_Date':None,
               'Department':None
    }
    catalog['artists'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artworks'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['Medium'] = mp.newMap(800,
                                   maptype='PROBING',
                                   loadfactor=0.50)
    catalog['Nationality'] = mp.newMap(69,
                                   maptype='PROBING',
                                   loadfactor=0.50)

    catalog['Begin_Date'] = mp.newMap(290, 
                                    maptype='CHAINING',
                                    loadfactor=4.0)
    
    catalog['Department'] = mp.newMap(11,
                                    maptype='CHAINING',
                                    loadfactor=4.0)

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

def comparacionDate(a1, a2):

    return a1['Date']<a2['Date']

def obrasantiguas(catalog, numero, medio):
    Lista = lt.newList(datastructure='ARRAY_LIST')
    obras = mp.get(catalog['Medium'], medio)
    lt.addLast(Lista, obras)
    
    sub_list = lt.subList(Lista, 1, numero)
    sorted_list = me.sort(sub_list, comparacionDate) 
    
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
#Req 1
def catalg_r1_begin(catalog):
    diccionario={}
    for i in range(1, lt.size(catalog['artists'])+1):
        artista = lt.getElement(catalog['artists'], i)
        artista['BeginDate'] =int(artista['BeginDate']) 
        if int(artista["BeginDate"]) in diccionario:
           diccionario[int(artista["BeginDate"])].append(artista)
        else:
           diccionario[int(artista["BeginDate"])]=[artista]
    
    for j in diccionario.keys():

        mp.put( catalog['Begin_Date'], j, diccionario[j])
    
    return(catalog["Begin_Date"])

def r1(catalog, añoini, añofini):

    Lista_años = lt.newList(datastructure='ARRAY_LIST')
    catalogo_begin = catalg_r1_begin(catalog)
    Años = mp.keySet(catalogo_begin)
    lista = []
    for i in range(1, lt.size(Años)+1):
        A= lt.getElement(Años, i)
        lista.append(A)
    lista.sort()
    if añofini+1 not in lista:
        lista = lista[lista.index(añoini):lista.index(añofini)]
    else:
        lista = lista[lista.index(añoini):lista.index(añofini+1)]
    for j in lista:
        Artista = mp.get(catalogo_begin, j)
        lt.addLast(Lista_años, Artista)
    contador = 0
    for h in (Lista_años['elements']):
        for j in h['value']:
            contador+=1
    print()
    print("Existen "+str(contador)+" artistas que nacieron entre "+str(añoini)+ " y "+str(añofini)+".")
    print()
    print("Los primeros y ultimos 3 artistas en el rango son...")
    print()
    value_=0
    lista_final = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(lista_final, ((mp.get(catalogo_begin, añoini))['value'][0:3]))
    if len((mp.get(catalogo_begin, añofini)['value'][-3:]))<3:
        lt.addLast(lista_final, (((mp.get(catalogo_begin, añofini-1))['value'][-1:])))
        lt.addLast(lista_final, (((mp.get(catalogo_begin, añofini))['value'][-3:])))
    print(lista_final)
    print(process_time())
    

# Req2

def req2(catalog,fecha_inicial, fecha_final):

    artworks = catalog["artworks"]
    fecha_inicial=datetime.strptime(fecha_inicial, '%Y-%m-%d') 
    fecha_final= datetime.strptime(fecha_final, '%Y-%m-%d')
    lista = lt.newList(datastructure='ARRAY_LIST')

    for i in range(1, lt.size(artworks)+1):

        obra = lt.getElement(artworks, i)

        if len(obra['DateAcquired']) > 0:

            fecha=datetime.strptime(obra['DateAcquired'], '%Y-%m-%d')
            if fecha >= fecha_inicial and fecha <= fecha_final:

              lt.addLast(lista, obra)

    if lt.size(lista)< 1:

      return("No se encontraron obras dentro del rango dado" )

    lista_sort = sa.sort(lista, comparacionDateAcquired)  
    lista_final = lt.subList(lista_sort, 1, 3)
    lista_ultimos = lt.subList(lista_sort, -3, 3)

    for i in range(1, lt.size(lista_ultimos)+1):
        lt.addLast(lista_final, lt.getElement(lista_ultimos, i))

    mapcl = creditlinemap(lista)
    compra = cantidad_purchase(mapcl)

    print ("Existen: " + str(lt.size(lista)) + " obras en el rango de los años dados.")
    print ("Existen " + str(compra) + " obras adquiridas por compra")

    return resultado_final_con_id(lista_final, catalog["artists"]), process_time()

def comparacionDateAcquired(e1, e2): 

    e1 = e1['DateAcquired']
    e2 = e2['DateAcquired']
    p1 = False
    p2 = False

    if len(e1) > 0 :
        e1 = datetime.strptime(e1, '%Y-%m-%d') 
        p1 = True
        
    if len(e2) > 0:
        e2 = datetime.strptime(e2, '%Y-%m-%d') 
        p2= True

    if p1==True and p2==True:
    
     if e1 < e2:
        
        resultado = True

     else:

        resultado= False   

    else:

       resultado = False  

    return resultado 

def resultado_final_con_id(lista, artists):
    
    resultado=lt.newList(datastructure='ARRAY_LIST')  
    iterador = 0
    diccionario={}
    artistas= ""

    for i in range(1, lt.size(lista)+1):

        diccionario={}
        obra = lt.getElement(lista,i)
        lista_obra = id_a_lista(obra["ConstituentID"])
        artistas= ""

        for n in lista_obra:
       
          iterador = 0  
          encontrado = False 
          
          while iterador <= lt.size(artists) and encontrado != True:

           artista = lt.getElement(artists,iterador)

           if int(n) == int(artista["ConstituentID"]):

            artistas += artista["DisplayName"]
            encontrado = True 

           else: 

            iterador += 1 
     
        diccionario["ObjectID"] = obra["ObjectID"]
        diccionario["Title"] = obra["Title"]
        diccionario["ArtistsName"] = artistas
        diccionario ["Medium"] = obra["Medium"]
        diccionario["Dimensions"] = obra["Dimensions"]
        diccionario["Date"] = obra["Date"] 
        diccionario["DateAcquired"] = obra["DateAcquired"]
        diccionario["URL"] = obra["URL"]

        lt.addLast(resultado, diccionario)    
      
    return resultado

def id_a_lista(string):

    un_digito=True

    if "," in string:
      un_digito=False

    valores = string[1:len(string)-1]  

    if un_digito == False:

        resultado = valores.split(",")

    else:

        resultado = [valores]

    return resultado 


def creditlinemap(lista):

    creditline = mp.newMap(300,
                            maptype='PROBING',
                            loadfactor=0.50)

    diccionario={}
    for i in range(1, lt.size(lista)+1):
        obra = lt.getElement(lista, i)
        if obra["CreditLine"] in diccionario:
           diccionario[obra["CreditLine"]].append(obra)
        else:
           diccionario[obra["CreditLine"]]=[obra]

    for i in diccionario.keys():

        mp.put( creditline, i, diccionario[i])

    return(creditline)

def cantidad_purchase(map):

    total = 0

    if mp.get(map, "Purchase") != None: 

      total += len(mp.get(map, "Purchase")["value"])

    if mp.get(map, "Purchase Fund") != None: 

      total += len(mp.get(map, "Purchase Fund")["value"])

    if mp.get(map, "Purchased with funds provided by the Friends of Contemporary Drawing") != None: 

      total += len(mp.get(map, "Purchased with funds provided by the Friends of Contemporary Drawing")["value"])

    if mp.get(map, "Purchase and gift of Barbara Schwartz in memory of Eugene M. Schwartz") != None: 

      total += len(mp.get(map, "Purchase and gift of Barbara Schwartz in memory of Eugene M. Schwartz")["value"])
    
    if mp.get(map, "Purchase from Cinema Arts") != None: 

      total += len(mp.get(map, "Purchase from Cinema Arts")["value"])
    
    if mp.get(map, "Purchased with funds given by Patricia and Morris Orden") != None: 

      total += len(mp.get(map, "Purchased with funds given by Patricia and Morris Orden")["value"])
    
    if mp.get(map, "Purchased with funds given by Richard E. Salomon and purchase through the Vincent D'Aquila and Harry Soviak Bequest Fund") != None: 

      total += len(mp.get(map, "Purchased with funds given by Richard E. Salomon and purchase through the Vincent D'Aquila and Harry Soviak Bequest Fund")["value"])

    if mp.get(map, "Purchased with funds given by Susan G. Jacoby in honor of her mother Marjorie L. Goldberger") != None: 

      total += len(mp.get(map, "Purchased with funds given by Susan G. Jacoby in honor of her mother Marjorie L. Goldberger")["value"])

    if mp.get(map, "Purchased with funds provided by Maja Oeri and Hans Bodenmann") != None: 

      total += len(mp.get(map, "Purchased with funds provided by Maja Oeri and Hans Bodenmann")["value"])

    if mp.get(map, "Purchased with funds provided by the International Council of The Museum of Modern Art in honor of H.R.H. Duke Franz of Bavaria, and Committee on Drawings Funds") != None: 

      total += len(mp.get(map, "Purchased with funds provided by the International Council of The Museum of Modern Art in honor of H.R.H. Duke Franz of Bavaria, and Committee on Drawings Funds")["value"])

    if mp.get(map, "Purchased with funds provided by the Friends of Contemporary Drawing") != None: 

      total += len(mp.get(map, "Purchased with funds provided by the Friends of Contemporary Drawing")["value"])
      
    return total

# Req3

def req3(catalog, nombre):
    
    obras= catalog["artworks"]
    artistas= catalog["artists"]
    id = obtener_id(artistas, nombre.lower())
    obras_por_artista = lt.newList(datastructure="ARRAY_LIST")
    contar_obras = 0
    resultado = None

    if id == None:

       resultado = "El artista no fue encontrado dentro de nuestro catalogo"

    else: 

        for i in range(1, lt.size(obras)+1):

          obra = lt.getElement(obras, i)
          lista = id_a_lista(obra["ConstituentID"])
          diccionario = {}

          for s in lista: 

           if id == int(s):
            
            diccionario["Title"] = obra["Title"]
            diccionario["Date"]= obra["Date"]
            diccionario["Medium"] = obra["Medium"]
            diccionario["Dimensions"] = obra["Dimensions"]

            lt.addLast(obras_por_artista, diccionario)
            contar_obras += 1
            break

        print("Existen " + str(lt.size(obras_por_artista)) + " obras en el museo con su nombre\n")
        medium = medium_map(obras_por_artista)
        
        if len(medium) > 6:

            resultado = [medium[:3],medium[-3:]]

        else:

            resultado = medium

    return resultado, process_time()

def medium_map(lista):

    medium = mp.newMap(100,
                            maptype='PROBING',
                            loadfactor=0.50)
    cuenta = {}
    diccionario={}

    for i in range(1, lt.size(lista)+1):
        obra = lt.getElement(lista, i)
        if obra["Medium"] in diccionario:
           diccionario[obra["Medium"]].append(obra)
           cuenta[obra["Medium"]] += 1
        else:
           diccionario[obra["Medium"]]=[obra]
           cuenta[obra["Medium"]] = 1

    for i in diccionario.keys():

        mp.put(medium, i, diccionario[i])

    print("Existen " + str(mp.size(medium)) + " diferentes tecnicas en sus obras de trabajo.\n")
    organizado = sorted(cuenta.items(), key=lambda x: x[1], reverse=True)
    print("su Top 5 de medios utilizados es: ")
    print(organizado[:5])
    print ("Su tecnica mas utilizada fue " + str(organizado[0][0]) + " con " + str(organizado[0][1]) + " obras." )

    return (mp.get(medium, str(organizado[0][0])))["value"]

def obtener_id(artistas, nombre):
    id = None 

    for i in range(1, lt.size(artistas)+1):

        artista=lt.getElement(artistas, i)
        if nombre in artista["DisplayName"].lower() or nombre == artista["DisplayName"]:

           id= int(artista["ConstituentID"])
           break 
        
        else:

            pass

    return id

#Req 4 
def r4(catalog):
    mapa = catalog['Nationality']
    
    diccionario = {}
    nacionalidades = ((mp.keySet(mapa)))
    lista = []
    for i in range( 1, lt.size(nacionalidades)+1):
        H = lt.getElement(nacionalidades, i)
        lista.append(H)
    for j in lista:
        contador = 0
        for h in mp.get(mapa, j)['value']:
            contador+=1
            diccionario[j] = contador
    if '' in diccionario.keys():
        del(diccionario[''])
    dicci_list = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
    print("El TOP 10 de nacionalidades en el MoMA son...")

    print(dicci_list[:10])

    Constituent = (((mp.get(mapa, 'American'))['value'][0:3]))
    Constituent_1 = (((mp.get(mapa, 'American'))['value'][-4:]))
    lista_codigos = []
    Lista_final = lt.newList(datastructure='ARRAY_LIST')
    for i in range(len(Constituent)):
       lista_codigos.append(str(Constituent[i]['ConstituentID']))

    for k in range(len(Constituent_1)):
       lista_codigos.append(str(Constituent_1[i]['ConstituentID']))
    if str(Constituent_1[i]['ConstituentID']) in lista_codigos:
           lista_codigos.append(str(Constituent_1[i-1]['ConstituentID']))
    
    for i in range(1, lt.size(catalog['artworks'])+1):
        obra = lt.getElement(catalog['artworks'], i)
        
        for j in range(len(lista_codigos)):
            if (obra['ConstituentID'][1:-1]) in lista_codigos[j]:
                lt.addLast(Lista_final, obra)
                
    print()
    print("La primeras y ultimas 3 obras de la nacionalidad American son...")
    print()
    print(Lista_final)
    print(process_time())
#Req5

def catalg_r5_department(catalog):
    diccionario={}
    for i in range(1, lt.size(catalog['artworks'])+1):
        obra = lt.getElement(catalog['artworks'], i)
        obra['Department'] =obra['Department']
        if obra["Department"] in diccionario:
           diccionario[obra["Department"]].append(obra)
        else:
           diccionario[obra["Department"]]=[obra]
    
    for j in diccionario.keys():

        mp.put( catalog['Department'], j, diccionario[j])
    
    return(catalog["Department"])


def req5(catalog, departamento):
    catalogo_dept = catalg_r5_department(catalog)
    #Constantes
    
    costo_defecto = 48.00
    Costo_total_sin_info = 0
    Costo_total_con_info = 0
    costo_total_translado = 0
    #Listas segun info
    Lista_sin_info = lt.newList(datastructure='ARRAY_LIST')
    Lista_con_info = lt.newList(datastructure='ARRAY_LIST')
    
    for i in mp.get(catalogo_dept, departamento)['value']:
        #Caso no obras con info suficiente
         if i['Dimensions'] == '':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Variable':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'various': 
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Various composition and sheet dimensions.':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Various dimensions':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Y': 
            lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'dimensions vary':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Dimensions: various':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Duration variable':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'N':
             lt.addLast(Lista_sin_info,  i)
         elif i['Dimensions'] == 'Dimensions and duration variable':
             lt.addLast(Lista_sin_info,  i)
         elif "min." in i['Dimensions'] :
             lt.addLast(Lista_sin_info,  i)
         else: 
             lt.addLast(Lista_con_info,  i)
        
    Costo_total_sin_info = (lt.size(Lista_sin_info)*costo_defecto)
    for i in range(1, lt.size(Lista_sin_info)):
        obra = lt.getElement(Lista_sin_info,i)
        obra["Cost_USD"] = costo_defecto

        lt.changeInfo(Lista_sin_info, i, obra)


    for i in range( 1, lt.size(Lista_con_info)+1):

        obra = lt.getElement(Lista_con_info, i)

        depth = obra["Depth (cm)"]
        diameter = obra["Diameter (cm)"]
        height = obra["Height (cm)"]
        Width = obra["Width (cm)"]
        length = obra[ "Length (cm)"]

        if len(depth) == 0:

           depth = 1

        
        elif float(depth) == 0.0:

           depth = 1

        else: 

           depth = float(depth)/100

        if len(diameter) == 0:

          diameter = 1

        elif float(diameter) == 0.0:

          diameter = 1

        else: 

           diameter= float(diameter)/100

        if len(height) == 0:

          height = 1

        elif float(height) == 0.0:

          height = 1

        else: 

           height = float(height)/100

        if len(Width) == 0:

           Width = 1

        elif float(Width) == 0.0:

          Width = 1

        else: 

           Width = float(Width)/100

        if len(length) == 0:

          length = 1 

        elif float(length) == 0.0:

          length = 1 

        else: 

           length = float(length)/100

        costo = (((depth * diameter * height * Width * length)/0.0001)/72.00)/2 
        Costo_total_con_info += costo
        obra["Cost_USD"] = costo

        lt.changeInfo(Lista_con_info, i, obra)
        costo_total_translado = Costo_total_con_info + Costo_total_sin_info


    for i in range(1, lt.size(Lista_sin_info)):
       obra = lt.getElement(Lista_con_info, i)
       lt.addLast(Lista_con_info, obra)

    organizado_fechas= sa.sort(Lista_con_info, comparacionDatecosto)  
    organizado_costo = sa.sort(Lista_con_info, comparacioncosto)  
    lista_final = lt.subList(organizado_fechas, 1, 5)
    lista_ultimos =lt.subList(organizado_costo, 1, 5)

    for i in range(1, lt.size(lista_ultimos)+1):
       lt.addLast(lista_final, lt.getElement(lista_ultimos, i))

    print("La carga estimada de es: 0 kg")
    print()
    print("El total de obras a transportar es " + str(lt.size(Lista_con_info))) 
    print()
    print("El costo estimado en USD es de " + str(costo_total_translado))
    print()
    print(process_time())
    resultado = resultado_final_id(lista_final, catalog["artists"])

    return print(resultado)

def comparacioncosto(e1, e2): 

    return e1["Cost_USD"] > e2["Cost_USD"]

def comparacionDatecosto(e1, e2): 

    e1 = e1['Date']
    e2 = e2['Date']
    p1 = False
    p2 = False

    if len(e1) > 0 :
        p1 = True
        
    if len(e2) > 0:

        p2= True

    if p1==True and p2==True:
    
     if e1 < e2:
        
        resultado = True

     else:

        resultado= False   

    else:

       resultado = False  

    return resultado 

def resultado_final_id(lista, artists):
    
    resultado=lt.newList(datastructure='ARRAY_LIST')  
    iterador = 0
    diccionario={}
    artistas= ""

    for i in range(1, lt.size(lista)+1):

        diccionario={}
        obra = lt.getElement(lista,i)
        lista_obra = id_a_lista(obra["ConstituentID"])
        artistas= ""

        for n in lista_obra:
       
          iterador = 0  
          encontrado = False 
          
          while iterador <= lt.size(artists) and encontrado != True:

           artista = lt.getElement(artists,iterador)

           if int(n) == int(artista["ConstituentID"]):

            artistas += artista["DisplayName"]
            encontrado = True 

           else: 

            iterador += 1 
     
        diccionario["ObjectID"] = obra["ObjectID"]
        diccionario["Title"] = obra["Title"]
        diccionario["ArtistsName"] = artistas
        diccionario["Classification"] = obra["Classification"]
        diccionario["Date"] = obra["Date"] 
        diccionario ["Medium"] = obra["Medium"]
        diccionario["Dimensions"] = obra["Dimensions"]
        diccionario["Cost_USD"] = obra["Cost_USD"]

        lt.addLast(resultado, diccionario)    
      
    return resultado

        

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
