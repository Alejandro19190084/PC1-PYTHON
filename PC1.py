"""
Problema 1:
Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
usuario haya introducido.
"""

#Solución
nombre=input("Coloque su nombre porfavor: ")
print("Hola, ", nombre, ", me da gusto en conocerte :)")

"""
Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.
"""
#Solución
costo=float(input("Indique el monto de su consumo total porfavor: "))
propina=costo*0.15
print("Usted podría dejar de propina", propina, "$ o más")

"""
Problema 3:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""
#Solución
payasos=float(input("Indique la cantidad de payasos que desea porfavor: "))
muñecas=float(input("Indique la cantidad de muñecas que desea porfavor: "))
pp=112        #Peso de payasos
pm=75         #Peso de muñecas
paquete=payasos*pp + muñecas*pm
print("El peso total de su paquete es", paquete, "g")

"""
Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N.
"""
N=int(input("Coloque el número que desee: "))
suma=N*(N+1)/2
print("La suma de los ",N,"es igual a: ",suma)

"""
Problema 5:
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.
"""
numero_de_shows=int(input("¿A cuántos shows ha asistido?: "))
cantidad_de_shows=numero_de_shows>3
print(cantidad_de_shows)

"""
Problema 6
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.
"""
edad=int(input("Coloque su edad por favor: "))
if edad<4:
    entrada=0
elif 4<=edad<=18:
    entrada=5
else:
    entrada=10

print("El precio de la entrada es ",entrada, " soles para un cliente de ",edad," años de edad") 

"""
Problema 7
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""
print("Ingrese dos números que desee y seleccione '1' para sumar; '2' para restar el primero menos el segundo y; '3' para multiplicar")
numero_1=float(input("Coloque el primer número: "))
numero_2=float(input("Coloque el segundo número: "))
opciones=int(input("¿Qué opción desea?: "))

if opciones==1:
    op=numero_1+numero_2
    print("El resultado de la suma es: ",op)
elif opciones==2:
    op=numero_1-numero_2
    print("El resultado de la resta es: ",op)
elif opciones==3:
    op=numero_1*numero_2
    print("El resultado de la multiplicación es: ",op)
else:
    print("La opción no es válida")

"""
Problema 8:
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar
"""
time = input("Escriba la hora en formato de 24 horas (por ejemplo, 12:12): ")

# Dividir la entrada en horas y minutos
try:
    horas, minutos = map(int, time.split(":"))
except ValueError:
    print("Error: Formato de hora incorrecto. Utiliza el formato HH:MM.")
else:
    # Construir la hora en formato HH:MM
    hora = f"{horas:02d}:{minutos:02d}"

    # Determinar la comida
    if "07:00" <= hora <= "08:00":
        print("Es hora de desayunar.")
    elif "12:00" <= hora <= "13:00":
        print("Es hora de almorzar.")
    elif "18:00" <= hora <= "19:00":
        print("Es hora de cenar.")
    else:
        print("No es hora de comer.")

"""
Problema 9:
Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
'día', 'buen', 'Di'].
"""
lista_original = input("Introduce una lista de elementos separados por comas: ")  #Lista brindada por el usuario
lista_original = lista_original.split(',')

lista_invertida = lista_original[::-1]               #Invertir la lista

print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)

"""
Problema 10:
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']
"""
lista_elm = input("Introduce una lista con 5 o más elementos separados por comas: ")  #Lista brindada por el usuario
lista_elm = lista_elm.split(',')
lista_rem = lista_elm.remove (0,4,5)
print("Lista de elementos:", lista_elm)
print("Lista removida:", lista_rem)
"""
Problema 11:
Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,, 5]
"""
lista_elm = input("Introduce una lista con 5 o más elementos separados por comas: ")
lista_elm = lista_elm.split(',')

lista_copia = lista_elm.copy()  #Creamos una copia para poder usar el comando remove

lista_copia.remove(lista_copia[5])
lista_copia.remove(lista_copia[4])
lista_copia.remove(lista_copia[0])

print("Lista de elementos original:", lista_elm)
print("Lista modificada:", lista_copia)

"""
Problema 12:
La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios,
anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
la web.
Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip
"""
# Diccionario de extensiones de archivo y tipos MIME
extensiones_mimes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo: ")

# Obtener la extensión del archivo
if "." in nombre_archivo:
    _, extension = nombre_archivo.rsplit('.', 1)
    extension = extension.lower()

    # Verificar si la extensión está en el diccionario
    tipo_mime = extensiones_mimes.get(extension, "application/octet-stream")
    print(f"Tipo MIME para {nombre_archivo}: {tipo_mime}")
else:
    print("El nombre del archivo no tiene una extensión válida.")