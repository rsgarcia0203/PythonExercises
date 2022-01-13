import numpy as np
# Compañía propietaria de una tarjeta de crédito
# tipo de articulo comprado
tipo = {"V": "Vestimenta",
        "A": "Alimentación",
        "E": "Educación",
        "N": "Entretenimiento",
        "S": "Salud"}

# barrios de la ciudad; un mismo barrio no se puede repetir en dos sectores
barrios = {"Tarqui": ["Alborada", "Sauces III", "Sauces IV"],
           "Ximena": ["La Floresta", "Guangala"]}

# Asuma que tiene una lista de transacciones
# Formato: Barrio:Fecha,Local,Tipo_articulo,Valor
transacciones = ["Alborada:21-12-2019,Veris,S,$35.40", ...]

def cargar_datos(transacciones, dic_tipos, dic_barrios):
    # Primero: creamos una lista vacia, la cual contendrá todos los barrios de manera ordenada
    lst_barrios = []

    # Segundo: recorremos el diccionario de barrios para agregarlos a nuestra lista de barrios
    for parroquia in barrios.keys():
        for barrio in dic_barrios[parroquia]:
            lst_barrios.append(barrio)

    # Tercero: creamos una matriz de ceros, de tamaño mxn
    #          donde las filas serán los barrios
    #          y las columnas serán los tipos de articulo por cada año
    #          En este caso solo tendremos 2 años (2019 y 2020)
    M = np.zeros((len(lst_barrios), 2 * len(dic_tipos.keys())))

    # Cuarto: recorremos las transacciones para poder indexarlas en nuestra matriz M
    for transaccion in transacciones:
        barrio, datos = transaccion.split(":")
        fecha, local, tipo_articulo, monto = datos.split(",")
        anio = (fecha.split("-"))[-1]
        monto = float(monto[1:])

        # Buscamos el indice de la fila en la que está el barrio
        i = lst_barrios.index(barrio)

        # Buscamos el indice de la columna en la que está el tipo de articulo
        lst_tipos = dic_tipos.keys()
        j = lst_tipos.index(tipo_articulo)

        # si el año es 2020, le sumamos la longitud de los tipos de articulos
        if anio == "2020":
            j = j + len(dic_tipos.keys()) - 1

        # ahora indexamos el monto en las coordenadas encontradas
        M[i,j] = monto

    return M
    
    
# Asuma que tiene una martiz M con datos de ventas anuales en galones
# de las gasolineras de todo el país
"""
          Primax    PS Los Ríos   Mobil     ...   Lutexsa CIA   PS Remigio
          Alborada               Cumbayá          Ltda          Crespo
Regular    239034     678493      896321    ...      32438        554213
Extra     4568321     6745634    9754008    ...     3242342       3456123
Súper      234773      56743      123678    ...       4783         90874
...          ...        ...        ...      ...       ....          ...
Premium     45672      45212       90781    ...       3904         10431
"""
M = [[...],
     [...],
     [...],
      ...,
     [...]]
# También tiene los siguientes datos como vectores de Numpy:

tipoGasolina = np.array(["Regular", "Extra", "Súper", "Premium", ...])
gasolineras = np.array(["Primax Alborada", "PS Los Ríos", "Mobil Cumbayá", "Lutexsa CIA Ltda", "PS Remigio Crespo", ...])
distrito = np.array(["distrito1", "distrito2", "distrito1", "distrito2", "distrito4", ...])
ciudades = np.array(["Guayaquil", "Babahoyo", "Quito", "Guayaquil", "Cuenca", ...])

# a. Pida un tipo de gasolina por teclado y muestre por pantalla los nombres
# de todas las gasolineras que han vendido en el año más del promedio de venta
# en galones para ese tipo
tipo_gasolina = input("Ingrese el tipo de gasolina: ")
promedio_de_venta = np.mean(M)

# Obtenemos un arreglo que contenga solo la fila donde está ubicado el tipo de gasolina ingresado
arr_galones_totales = M[tipoGasolina == tipo_gasolina]
arr_galones_totales = arr_galones_totales[arr_galones_totales > promedio_de_venta]
print(arr_galones_totales)


# b. Pida una ciudad por teclado y calcule cuántas de sus gasolineras han vendido más
# de 15 millones de galones en total en el año, considerando todas las ventas de
# todos los tipos de gasolinas
ciudad = input("Ingrese el nombre de la ciudad: ")

# Obtenemos las ventas totales de cada gasolinera
# sumamos las ventas de las gasolineras por todo tipo de gasolina
arr_gasolineras = np.sum(M, axis=0)

# Ahora obtenemos cuantas gasolineras han vendido mas de 15 millones de galones en total en el año
arr_gasolineras = arr_gasolineras[arr_gasolineras > 15000000]
print("La cantidad de gasolineras que han vendido mas de 15 millones de galones en el año son :", len(arr_gasolineras))