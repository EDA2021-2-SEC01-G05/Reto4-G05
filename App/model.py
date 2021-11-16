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
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
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
                }

    analyzer['red'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=None)
    return analyzer

#======================================================================
# Agregar info al catalogo
#======================================================================

def addAirport(analyzer,airport):
    """
    Adiciona un aeropuerto como vertice del grafo
    """
    id = airport['IATA']
    if not gr.containsVertex(analyzer['red'], id):
            gr.insertVertex(analyzer['red'], id)
    return analyzer

def addRoute(analyzer, route):
    """
    Adiciona una ruta como arco entre dos aeropuertos
    """
    origin = route['Departure']
    destination = route['Destination']
    distance = route['distance_km']
    edge = gr.getEdge(analyzer['red'], origin, destination)
    if edge is None:
        gr.addEdge(analyzer['red'], origin, destination, distance)
    return analyzer

#======================================================================
# Funciones de comparacion
#======================================================================