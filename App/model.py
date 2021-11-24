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

import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

#=======================================================================
# Construccion de modelos
#=======================================================================

def newAnalyzer():
    """ Inicializa el analizador
    airports: tabla de hash para guardar los vertices del grafo
    red: grafo para representar los vuelos entre aeropuertos
    """
    
    analyzer = {
                'red': None,
                'aeropuertos': None,
                }

    analyzer['red'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=None)
    analyzer['aeropuertos'] = mp.newMap()
    analyzer['ciudades'] = mp.newMap()
    return analyzer

#======================================================================
# Agregar info al catalogo
#======================================================================

def addAirport(analyzer,airport):
    """
    Adiciona un aeropuerto al map aeropuertos como vertice del grafo red  
    """
    id = airport['IATA']
    mp.put(analyzer['aeropuertos'],id,airport)
    if not gr.containsVertex(analyzer['red'], id):
            gr.insertVertex(analyzer['red'], id)
    return analyzer

def addRoute(analyzer, route):
    """
    Adiciona una ruta como arco entre dos aeropuertos en el grafo red
    """
    origin = route['Departure']
    destination = route['Destination']
    distance = route['distance_km']
    edge = gr.getEdge(analyzer['red'], origin, destination)
    if edge is None:
        gr.addEdge(analyzer['red'], origin, destination, distance)
    return analyzer

def addCity(analyzer, city):
    """
    Adiciona una ciudad al map ciudades
    """
    name = city['city']
    mp.put(analyzer['ciudades'],name,city)
    return analyzer
#======================================================================
# Funciones de comparacion
#======================================================================

def ordenAscendenteD(a,b):
    if (a > b):
        return 0
    return -1

#======================================================================
# Requerimientos
#======================================================================

def Requerimiento1(analyzer):
    grafo = analyzer['red']
    aeropuertos = gr.vertices(grafo)
    conexiones = lt.newList()
    for aeropuerto in lt.iterator(aeropuertos):
        num = gr.degree(grafo,aeropuerto)
        lt.addLast(conexiones,num)
    ms.sort(conexiones,ordenAscendenteD)
    c = lt.lastElement(conexiones)

    mas_conectados = lt.newList()
    for aeropuerto in lt.iterator(aeropuertos):
        n = gr.degree(grafo,aeropuerto)
        if int(n) == int(c):
            lt.addLast(mas_conectados,aeropuerto)
    mapa = analyzer['aeropuertos']
    resultado = lt.newList('ARRAY_LIST')
    for ide in lt.iterator(mas_conectados):
        pareja = mp.get(mapa,ide)
        valor = me.getValue(pareja)
        lt.addLast(resultado,valor)
    lt.addLast(resultado,c)
    return resultado
