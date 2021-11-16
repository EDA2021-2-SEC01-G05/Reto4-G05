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

#======================================
# Inicialización del Catálogo
#======================================

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer

#==================================
# Funciones para la carga de datos
#==================================

def loadData(analyzer):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadAirports(analyzer)
    loadRoutes(analyzer)
    return analyzer

def loadAirports(catalog):
    """
    Carga los aeropuertos.
    """
    booksfile = cf.data_dir + 'Skylines/airports_full.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for airport in input_file:
        model.addAirport(catalog, airport)
    
def loadRoutes(catalog):
    """
    Carga las rutas.
    """
    booksfile = cf.data_dir + 'Skylines/routes_full.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for route in input_file:
        model.addRoute(catalog, route)