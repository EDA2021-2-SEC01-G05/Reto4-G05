﻿"""
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
from DISClib.ADT import graph as gr
from DISClib.ADT import map as mp
from DISClib.ADT import stack as st
from DISClib.DataStructures import mapentry as me
assert cf
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#=================================================================================
# Funciones Iniciales
#=================================================================================

def printMenu():
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de transporte aereo")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("0- Salir")
    print("*******************************************")

def loadData(analyzer):
    """
    Carga los datos en la estructura de datos
    """
    return controller.loadData(analyzer)

analyzer = None

#=================================================================================
# Especificaciones de la impresion de datos
#=================================================================================

def printDataReq1(datos):
    size = lt.size(datos)
    if size>0:
        for dato in lt.iterator(datos):
            if dato is not None:
                print('IATA: ' + dato['IATA'] + ', Nombre: ' + dato['Name']
                     + ', Ciudad: ' + dato['City'] + ', Pais: ' + dato['Country']) 
    else:   
        print ("No se encontraron datos")

def printAeropuerto(dato):
    if dato is not None:
                print('IATA: ' + dato['IATA'] + ', Nombre: ' + dato['Name']
                     + ', Ciudad: ' + dato['City'] + ', Pais: ' + dato['Country'])

def printFirst(analyzer, indice):
    llaves = mp.keySet(analyzer[indice])
    p = lt.firstElement(llaves)
    primero = mp.get(analyzer[indice], p)
    valor = me.getValue(primero)
    if indice == "aeropuertos":
        print("Nombre: " + valor["Name"] + " Ciudad: " + valor["City"] + " País: " + valor["Country"] 
                            + " Latitud: " + valor["Latitude"] + " Longitud: " + valor["Longitude"])
    elif indice == "ciudades":
        valor = lt.removeLast(valor)
        print("Nombre: " + valor["city_ascii"] + " Latitud: " + valor["lat"] + " Longitud: " + valor["lng"] 
                                                                    + " Población: " + valor["population"])
def PrintCargaDatos(analyzer):
    print("-" * 50)
    print("Información Grafo Dirigido")
    print("-" * 50)
    print("Total de aeropuertos: " + str(gr.numVertices(analyzer['red'])))
    print("Total de rutas: " + str(gr.numEdges(analyzer['red'])))
    print("-" * 50)
    print("Información Grafo No Dirigido")
    print("-" * 50)
    print("Total de aeropuertos: " + str(gr.numVertices(analyzer['blue'])))
    print("Total de rutas: " + str(gr.numEdges(analyzer['blue'])))
    print("-" * 50)
    print("Total de ciudades: "+  str(mp.size(analyzer["ciudades"])))
    print("-" * 50)
    print("Primer Aeropuerto Cargado: ")
    printFirst(analyzer, "aeropuertos")
    print("-" * 50)
    print("Primera Ciudad Cargado: ")
    printFirst(analyzer, "ciudades")
    print("-" * 50 +"\n")

#=================================================================================
# Requerimientos
#=================================================================================

def cargaDatos(analyzer):
    return controller.loadData(analyzer)

def Requerimiento1(analyzer):
    aeropuertos = controller.Requerimiento1(analyzer)
    interconexiones = lt.removeLast(aeropuertos)
    printDataReq1(aeropuertos)
    print('Número de aeropuertos interconectados: ' + str(interconexiones))
    print("-" * 50)
    return None

def Requerimiento2(analyzer):
    return None

def Requerimiento3(analyzer,origen,destino):
    resultado = controller.Requerimiento3(analyzer,origen,destino)
    aero_o = lt.removeFirst(resultado)
    aero_d = lt.removeFirst(resultado)
    camino = lt.removeFirst(resultado)
    dt_o = lt.removeFirst(resultado)
    dt_d = lt.removeFirst(resultado)
    d_aerea = lt.newList()
    print("-" * 50)
    print('Aeropuerto de origen: ')
    printAeropuerto(aero_o)
    print('Aeropuerto de destino: ')
    printAeropuerto(aero_d)
    print("-" * 50)
    print('Ruta Aérea por segmentos: ')
    tamano = st.size(camino)
    i = 0
    while i < tamano:
        path = st.pop(camino)
        print(str(path))
        lt.addLast(d_aerea,float(path['weight']))
        i += 1
    total_a = 0
    for distance in lt.iterator(d_aerea):
        total_a += distance
    print("-" * 50)
    print('Distancia total ruta: ' + str(int(dt_o+dt_d+total_a)))
    print('Distancia total aereo: ' + str(int(total_a)))
    print('Distancia ciudad-aeropuerto origen: ' + str(int(dt_o)))
    print('Distancia ciudad-aeropuerto destino: ' + str(int(dt_d)))
    return None

def Requerimiento4(analyzer):
    return None

def Requerimiento5(analyzer):
    return None

#================================================================================
# Menu principal
#================================================================================

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        analyzer = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("\nCargando información de transporte aereo ....")
        start_time = time.process_time()
        cargaDatos(analyzer)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de ejecución: " + str(elapsed_time_mseg))
        PrintCargaDatos(analyzer)

    elif int(inputs[0]) == 3:
        start_time = time.process_time()
        Requerimiento1(analyzer)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de ejecución: " + str(elapsed_time_mseg))

    elif int(inputs[0]) == 4:
        start_time = time.process_time()
        Requerimiento2(analyzer)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de ejecución: " + str(elapsed_time_mseg))
    
    elif int(inputs[0]) == 5:
        origen = input('Ciudad de origen: ')
        destino = input('Ciudad de destino: ' )
        start_time = time.process_time()
        Requerimiento3(analyzer,origen,destino)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de ejecución: " + str(elapsed_time_mseg))
    
    elif int(inputs[0]) == 6:
        start_time = time.process_time()
        Requerimiento4(analyzer)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de ejecución: " + str(elapsed_time_mseg))

    elif int(inputs[0]) == 7:
        start_time = time.process_time()
        Requerimiento5(analyzer)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de ejecución: " + str(elapsed_time_mseg))
        
    else:
        sys.exit(0)
sys.exit(0)