# Variables, Expresiones y Condicionales

Esta carpeta contiene archivos que explicarán los conceptos básicos de python y como usarlos.


### Corriendo nuestro primer programa en Python
Los programas de Python no se compilan, sino que se interpretan. 
Ahora, pasemos a escribir un código Python y ejecutarlo. 
Asegúrese de que Python esté instalado en el sistema en el que está trabajando. 
Usaremos python 3.7.0. 

### Creando archivos de python
Los archivos de Python se almacenan con la extensión ".py". 
Abra un editor de texto y guarde un archivo con el nombre "hola.py". 
Ábrelo y escribe el siguiente código: 

```python
print("Hola mundo, este es mi primer programa en Python. :D")
```
### Leyendo el contenido del archivo .py 

+ En los sistemas de Linux: Desde la terminal del sistema nos vamos al directorio donde esta almacenado el archivo creado (hola.py), 
  para ello usamos el comando 'cd' y luego escriba lo siguiente en la terminal:
  ```console
  python hola.py
  ```

+ En los sistemas de Windows: Abrimos el símbolo del sistema y nos movemos al directorio donde está almacenado el archivo creado (hola.py)
  para ello usamos el comando 'cd' y luego ejecutamos el archivo escribiendo el nombre del archivo como un comando: 
  ```console
  cd C:<directorio donde se encuentra el archivo>
  hola.py
  ```

## Variables
Las variables no necesitan declararse primero en python, ya que estas se pueden usar directamente. 
Las variables en python distinguen entre mayúsculas y minúsculas como la mayoría de los otros lenguajes de programación. 
Por ejemplo:
```python
a = 1
b = 2
print(a)
print(b)
```

Salida del código anterior:
```console
1
2
```

## Expresiones
Las operaciones aritméticas en python se pueden realizar mediante el uso de operadores aritméticos y 
algunas de las funciones integradas.
Por ejemplo:
```python
a = 10
b = 2

# En la variable 'c' almacenaremos la suma de a y b
c = a + b

# En la variable 'd' almacenaremos la resta entre a y b
d = a - b

# En la variable 'e' almacenaremos la multiplicacion entre a y b
e = a * b

# En la variable 'f' almacenaremos la división entre a y b
f = a / b

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

Salida del código anterior:
```console
10
2
12
8
20
5
```

## Condicionales
La salida condicional en python se puede obtener usando declaraciones if-else y elif (else if). 

Por ejemplo:
```python
a = 10
b = 2

# En la primera condición le diremos que si el residuo de a para b es 0, imprima que a es divisible para 2
if a % b == 0:
  print("a es divisible para 2")

# En la segunda condición le diremos que si b + 6 da como resultado 10, imprima que el incremento en b produce 10
elif b + 6 == 10:
  print("El incremento en a da como resultado 10")

# Finalmente, si no cumple ninguna de las dos condiciones anteriores, imprimiremos que no cumple con ninguna de las dos condiciones anteriores
else:
  print("No cumple ninguna de las dos condiciones anteriores")
```

Salida del código anterior:
```console
a es divisible para 2
```
