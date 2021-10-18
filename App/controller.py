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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""



# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog) 
    
def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """

    artistsfile = cf.data_dir + '/MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
 
    for artist in input_file:

        model.addArtist(catalog, artist)
    

def loadArtworks(catalog):
    artworksfile = cf.data_dir + '/MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artworks in input_file:
        model.addArtworks(catalog, artworks)

def pruebauno(catalog):
    return model.prueba(catalog)

def medio(catalog, Medio):
    return model.buscarporMedio(catalog,Medio)

def obrasmasantiguas(catalog, numero, medio):
    return model.obrasantiguas(catalog, numero, medio)

def nacionalidad_(catalog):
    return model.nacionlidad(catalog)

def buscar_por_nacio(catalog, nacionalidad):
    return model.buscarporNacionalidad(catalog,nacionalidad)

def req2(catalog, fecha_inicial, fecha_final):
    return model.req2(catalog, fecha_inicial, fecha_final)

def req3(catalog, nombre):
    return model.req3(catalog, nombre)

def req5(catalog, departamento):
    return model.req5(catalog, departamento)
    