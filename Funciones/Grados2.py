"""Para este ejercicio usaremos la misma temática que el anterior
   Es decir, escribiremos un programa que nos permita convertir los grados
   Sin embargo, esta vez haremos que permita elegir al usuario el tipo de conversión que desea realizar
   Y que el usuario pueda salir al ingresar una opcion, para ello deberemos mostrar un menú"""

# Primero definimos la función 'convertirFaC', la cual convertirá de grados Fahrenheit a Celsius
def Fahrenheit_Celsius(F):
    C = (F - 32) / (9/5)
    return C

def Fahrenheit_Kelvin(F):
    K = ((F - 32) * (5/9)) + 273
    return K

def Celsius_Fahrenheit(C):
    F = (C * (9/5)) + 32
    return F

def Celsius_Kelvin(C):
    K = C + 273
    return K

def Kelvin_Celsius(K):
    C = K - 273
    return K

def Kelvin_Fahrenheit(K):
    F = ((K - 273) * (9-5)) + 32
    return F

def Menu():
    print("  ==========================")
    print("||     MENU PRINCIPAL       ||")
    print("  ==========================\n\n")
    print("\t1.- Convertir de Fahrenheit a Celsius.")
    print("\t2.- Convertir de Fahrenheit a Kelvin.")
    print("\t3.- Convertir de Celsius a Fahrenheit.")
    print("\t4.- Convertir de Celsius a Kelvin.")
    print("\t5.- Convertir de Kelvin a Celsius.")
    print("\t6.- Convertir de Kelvin a Fahrenheit.")
    print("\t7.- Salir\n\n\n")

    op = input("Ingrese una opción: ")
    return op

op = ""
while op == "7":
    
    op = Menu()

    if op == "1":
        print("****************************")
        print("*  Convertidor de °F a °C  *")
        print("****************************\n")

        # Le pedimos al usuario que ingrese los grados
        F = input("Ingrese los grados: ")

        # Verificamos que haya ingresado un número y no una letra o palabra
        if F.isnumeric() == True:
            C = Fahrenheit_Celsius(float(F))
            print("{}°F es igual a {}°C".format(float(F),C))
        else: 
            print("Debe ingresar un valor numérico.")

    elif op == "2":
        print("****************************")
        print("*  Convertidor de °F a °K  *")
        print("****************************\n")

        # Le pedimos al usuario que ingrese los grados
        F = input("Ingrese los grados: ")

        # Verificamos que haya ingresado un número y no una letra o palabra
        if F.isnumeric() == True:
            K = Fahrenheit_Kelvin(float(F))
            print("{}°F es igual a {}°K".format(float(F),K))
        else: 
            print("Debe ingresar un valor numérico.")

    elif op == "3":
        print("****************************")
        print("*  Convertidor de °C a °F  *")
        print("****************************\n")

        # Le pedimos al usuario que ingrese los grados
        C = input("Ingrese los grados: ")

        # Verificamos que haya ingresado un número y no una letra o palabra
        if C.isnumeric() == True:
            F = Celsius_Fahrenheit(float(C))
            print("{}°C es igual a {}°F".format(float(C),F))
        else: 
            print("Debe ingresar un valor numérico.")

    elif op == "4":
        print("****************************")
        print("*  Convertidor de °C a °K  *")
        print("****************************\n")

        # Le pedimos al usuario que ingrese los grados
        C = input("Ingrese los grados: ")

        # Verificamos que haya ingresado un número y no una letra o palabra
        if C.isnumeric() == True:
            K = Celsius_Kelvin(float(C))
            print("{}°C es igual a {}°K".format(float(C),F))
        else: 
            print("Debe ingresar un valor numérico.")

    elif op == "5":
        print("****************************")
        print("*  Convertidor de °K a °C  *")
        print("****************************\n")

        # Le pedimos al usuario que ingrese los grados
        K = input("Ingrese los grados: ")

        # Verificamos que haya ingresado un número y no una letra o palabra
        if K.isnumeric() == True:
            C = Kelvin_Celsius(float(K))
            print("{}°C es igual a {}°K".format(float(K),C))
        else: 
            print("Debe ingresar un valor numérico.")

    elif op == "6":
        print("****************************")
        print("*  Convertidor de °K a °F  *")
        print("****************************\n")

        # Le pedimos al usuario que ingrese los grados
        K = input("Ingrese los grados: ")

        # Verificamos que haya ingresado un número y no una letra o palabra
        if K.isnumeric() == True:
            F = Kelvin_Fahrenheit(float(K))
            print("{}°C es igual a {}°K".format(float(K),F))
        else: 
            print("Debe ingresar un valor numérico.")

    elif op == "7":
        print("***********  ***********    *******     *******   *****   *******   *******")
        print("*            *          *  *       *   *       *    *    *       *  *      ")
        print("*            *          *  *       *  *        *    *    *       *  *      ")
        print("*            *          *  *       *  *             *    *       *  ****** ")
        print("*   *******  ***********   *********  *             *    *********        *")
        print("*         *  *       *     *       *  *        *    *    *       *        *")
        print("*         *  *        *    *       *   *       *    *    *       *        *")
        print("***********  *         *   *       *    *******   *****  *       *  ****** ")

    else:
        print("Ingrese una opción valida.")