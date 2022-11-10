#Ejercicio de preparación - Hola OICV
#Este es un ejercicio muy sencillo, para que pruebes el funcionamiento del juez de la olimpiada.
#Debes escribir un programa que lea de la entrada estándar y que escriba varios saludos.
#La primera línea de la entrada que debes leer tiene dos números n y k. El primer número indica la cantidad de saludos y el segundo indica si hay que leer o no nombres para saludar.
#En el caso en que sea 0, significa que no hay que leer nada más de la entrada y que hay que saludar n veces diciendo Hola OICV.

#El primer número indica la cantidad de saludos
n = int(linea[0]) 
#el segundo indica si hay que leer o no nombres para saludar
k = int(linea[2])
    
while (n > 0):
    if k == 0: #no hay que leer nombres
        salida = "Hola OICV"
    elif k == 1:
        nombre = input()
        salida = "Hola " + nombre
    print(salida)
    n -= 1
    
   
