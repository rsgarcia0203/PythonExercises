# Escriba un programa que permita ingresar al usuario un día, mes y un año
# El programa deberá de imprimir la fecha con el formato año-mes-día

# Primero creamos las variables que contendrán los datos ingresados por el usuario,
# junto con sus respectivos inputs
dia = int(input("Ingrese el día: "))
mes = input("Ingrese el mes: ")
anio = int(input("Ingrese el año: "))

# Luego creamos una lista de meses, debido a que el usuario deberá ingresar el nombre del mes y no el número
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Finalmente buscamos donde se encuentra ubicado nuestro mes en nuestra lista de meses (la cual está ordenada)
i = meses.index(mes.capitalize())

# Imprimimos el resultado
print("20{}-{}-{}".format(anio,i,dia))


# Escriba un programa que pida la siguiente información sobre un viaje al usuario: 
# salida(Ciudad o País), destino(Ciudad o País), tiempo estimado de viaje, velocidad (Tren, auto o tren) y número de pasajeros
# Toda está información debera de ingresarla el usuario separada por comas

# Con la finalidad de que el programa sea mas intuitivo para el usuario, vamos a imprimir el formato y los datos que debe ingresar el mismo
print("CALCULO DEL TIEMPO DE VIAJE\n")
print("Formato de ingreso de datos:")
print("Salida(Ciudad o País), destino(Ciudad o País), tiempo estimado de viaje, velocidad (Tren, auto o tren) y número de pasajeros \n")

# Luego solicitamos el ingreso por teclado de los datos
datos = input("Ingrese la información del viaje separado por comas: ")

# Separamos los datos que fueron ingresados por la "," y los almacenamos en sus respectivas variables
salida, destino, tiempo_estimado, velocidad, pasajeros = datos.split(",")

# La velocidad calculada va a disminuir dependiendo a la cantidad total de pasajeros dentro del vehículo
velocidad_calculada = float (velocidad) - int(pasajeros)

# El tiempo de viaje será igual a la velocidad dividida para el tiempo estimado de viaje
tiempo_viaje = velocidad/ float(tiempo_estimado)

# Finalmente imprimimos de manera ordenada toda la información ingresada y calculada
print("Salida: {}".format(salida.capitalize()))
print("Destino: {}".format(destino.capitalize()))
print("Pasajeros: {}".format(pasajeros))
print("Velocidad calculada: {} km/h".format(velocidad_calculada))
print("Tiempo de viaje: {} horas".format(tiempo_viaje))
