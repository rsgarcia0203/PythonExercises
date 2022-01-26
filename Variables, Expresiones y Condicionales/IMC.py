"""Escriba un programa que le pida al usuario su nombre, peso, altura y edad.
   Ud debe calcular el indice de masa corporal (IMC = peso / altura^2).
   Luego, basado en la edad y el IMC, muestre los siguientes mensajes:
   - Si el IMC es menor a 18.50, tiene desnutrición
   - Si el IMC esta entre 18.50 y 25, tiene un peso normal
   - Si el IMC esta entre 25 y 30, tiene sobrepeso
   - Si el IMC esta entre 30 y 35, tiene Obesidad de clase I
   - Si el IMC esta entre 35 y 40, tiene Obesidad de clase II
   - Si el IMC es mayor a 40, tiene obesidad de clase III
   NOTA: Solo se puede calcular el IMC si el usuario tiene 18 o más años"""
   
# Primero pedimos al usuario que ingrese su nombre
usuario= input("Escriba su nombre de usuario:")

# Le pedimos que ingrese su peso
peso= int(input("Escriba su peso:"))

# Le pedimos que ingrese su altura
altura= int(input("Escriba su altura:"))

# Y finalmente su edad
edad= int(input("Escriba su edad:"))

# Calculamos el IMC con la formula proporcionada
IMC = peso/altura**2

# Si la edad es menor a 18 años, entonces no podremos realizar y mostrar el calculo
if edad < 18:
    print("No hacemos calculos para menores de 18 años")

# Si tiene 18 años o mas, entonces procedemos a realizar y mostrar el calculo
else:

    # Escribimos las condiciones antes menciondas con su respectivo mensaje
    # En este caso serán mensajes personalizados
    if IMC < 18.50:
        print("Tiene desnutricion, necesita comer mas")
    elif IMC >= 18.50 and IMC < 25:
        print("Tienes peso normal")
    elif IMC >= 25 and IMC < 30:
        print("Tiene sobrepeso, debería de realizar un poco de actividad física")
    elif IMC >= 30 and IMC < 35:
        print("Tiene obesidad de clase I, necesita comer menos y realizar ejercicio")
    elif IMC >= 35 and IMC < 40:
        print("Tiene obesidad de clase II, necesita comer menos y realizar más ejercicio")
    elif IMC >= 40:
        print("Tiene obesidad de clase III, se le recomienda agendar cita con un nutriologo para que lo ayude")