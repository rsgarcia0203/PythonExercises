# FUNCIONES, ARCHIVOS, ARREGLOS

# En esté ejercicio desarrollaremos un programa que tendrá que:
# 1.- Cargar datos desde un archivo csv y generar una matriz y dos listas
# 2.- Calcular los promedios


import numpy as np

def cargar_datos(archivo,dic_tipos,dic_barrios):
    lst_barrios = []
    for sector in dic_barrios:
        for barrio in sector:
            lst_barrios.append(barrio)
    arr_barrios = np.unique(lst_barrios)
    M = np.zeros((len(arr_barrios)*2,len(dic_tipos)))
    lst_tipos = dic_tipos.keys()
    file = open(archivo,"r")
    file.readline()
    for linea in file.readlines():
        barriox,local,tipo,valor = linea.strip().split(",")
        barrio,fecha = barriox.split(":")
        i = arr_barrios.index(barrio)
        j = lst_tipos.index(tipo)
        if fecha.endswith("2019")==True:
            M[i][j] += float(valor[1:])

        elif fecha.endswith("2020")==True:
            M[i][j+len(lst_tipos)] += float(valor[1:])

    file.close()
    return M, list(arr_barrios),lst_tipos

def promedios(M,año,l_tipos,l_barrios):
    if año == 2019:
        M2 = M[:][len(l_tipos):]
        tot = M2.sum(axis=1)
        prom_anual = np.mean(tot)
        arr_barrios = np.array(l_barrios)
        n_arr_barrios = arr_barrios[tot > prom_anual]
        return list(n_arr_barrios)

    elif año == 2020:
        M2 = M[:][:len(l_tipos)]
        tot = M2.sum(axis=1)
        prom_anual = np.mean(tot)
        arr_barrios = np.array(l_barrios)
        n_arr_barrios = arr_barrios[tot > prom_anual]
        return list(n_arr_barrios)

#3
M, lst_barrios, lst_tipos = cargar_datos("transactions.csv",dic_tipos,dic_barrios)
lst_barrios_prom = promedios(M,2020,lst_tipos,lst_barrios)
print("Barrios que consumieron mas que el promedio para el 2020:",lst_barrios_prom)

#4
r = ""
while r == "correcta":
    sector = input("Ingrese el sector de la ciudad: ")
    if sector.capitalize() == "Red" or sector.capitalize() == "Blue" or sector.capitalize() == "Magneta":
        barrios = dic_barrios [sector.capitalize()]
        M2019 = M[:][len(lst_tipos):]
        M2020 = M[:][:len(lst_tipos)]
        M2019_tot = M2019.sum(axis=1)
        M2020_tot = M2020.sum(axis=1)
        lst_val_barrios_2019 = []
        lst_val_barrios_2020 = []

        for barrio in barrios:
            i = lst_barrios.index(barrio)
            valor_2019 = M2019_tot[i]
            valor_2020 = M2020_tot[i]
            lst_val_barrios_2019.append(valor_2019)
            lst_val_barrios_2020.append(valor_2020)
        arr_val_barrios_2019 = np.array(lst_val_barrios_2019)
        arr_val_barrios_2020 = np.array(lst_val_barrios_2020)
        arr_barrios = np.array(barrios)
        count = 5
        while count != 0:
            max2019 = np.max(arr_val_barrios_2019)
            max2020 = np.max(arr_val_barrios_2020)
            if max2019 > max2020:
                M2019_tot [M2019_tot == max2019] = 0
                M2020_tot [M2020_tot == max2020] = 0
                count = count-1
        n_arr_barrios = arr_barrios [M2020_tot == 0]
        print(list(n_arr_barrios))
        r = "correcta"

    else:
        print("Nombre del sector incorrecto, intente de nuevo")
        r = "incorrecto"

