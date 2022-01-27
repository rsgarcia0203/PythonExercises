# Escribiremos un programa que nos permita convertir los grados
# En este caso vamos a convertir de grados Fahrenheit a Celsius
# Y pediremos la información al usuario separata por comas


# Primero definimos la función 'convertir', la cual llamaremos para realizar la conversión
def convertir(gradoF):
    # Al ser un ejercicio introductorio, haremos que si los grados F son menores a -460, devuelva que en celsius es -1000000
    if gradoF < -460:
        return -1000000
    else:
        gradoC = (gradoF - 31) * (5 / 9)
        return gradoC

# Definimos la función 'mostrarDatos', la cual mostrara por consola los datos de los grados que hemos convertido de manera ordenada
def mostrarDatos(lst1, lst2, lst3):
    for i in range(len(lst1)):
        # Usamos el format para poder imprimir de manera ordenada los datos
        print("{}F son {}C ({})".format(lst1[i],lst2[i], lst3[i]))
    return ""

# Definimos la función 'condiciones', la cual nos permitirá saber bajo que condiciones nos encontramos al estar en esa temperatura
# Es decir, si hace Frío, Calor o esta Temperado
def condiciones(lstgradosC):
    lst_condiciones = []
    condicion = ""
    for grado in lstgradosC:
        if grado < 15:
            condicion = "frio"
            lst_condiciones.append(condicion)
        elif grado > 30:
            condicion = "caliente"
            lst_condiciones.append(condicion)
        else:
            condicion = "temperado"
            lst_condiciones.append(condicion)
    return lst_condiciones

# Pedimos al usuario que ingrese la información
datos = input("Temperaturas: ")
lst_gradosF = datos.split(",") # Usamos el split para separar el string de datos ingresados por la coma
lst_gradosC = []

# Recorremos la listas de grados Fahrenheit para realizar la converción a grados Celsius
for gradoF in lst_gradosF:
    gradoC = convertir(gradoF)
    lst_gradosC.append(gradoC)

# Generamos la lista de condiciones para esas temperaturas
lst_condiciones = condiciones(lst_gradosC)

# Mostramos los datos ingresados, con su respectiva conversión y su condición
mostrarDatos(lst_gradosF,lst_gradosC,lst_condiciones)