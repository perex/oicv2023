#Ejercicio de preparación - Hola OICV
#Este es un ejercicio muy sencillo, para que pruebes el funcionamiento del juez de la olimpiada.
#Debes escribir un programa que lea de la entrada estándar y que escriba varios saludos.
#La primera línea de la entrada que debes leer tiene dos números n y k. El primer número indica la cantidad de saludos y el segundo indica si hay que leer o no nombres para saludar.
#En el caso en que sea 0, significa que no hay que leer nada más de la entrada y que hay que saludar n veces diciendo Hola OICV.

#ejemplo 4 0
linea = input()

try:   
    
    #El primer número indica la cantidad de saludos
    n = int(linea[0]) 
    #el segundo indica si hay que leer o no nombres para saludar
    k = int(linea[2])
    
    #print(n)
    #print(k)

    if k == 0: #no hay que leer nombres
        #imprimimos tantos Hola OICV como contenga n
        for x in range(n):
            print("Hola OICV")
    elif k == 1:
        #leer nombres por línea estándar
        listaNombres = []
        for x in range(n):
            nombre = input()
            listaNombres.append(nombre)
        for x in listaNombres:
            #Imprimir "Hola " + x ("Nombre Actual de la lista")
            print("Hola "+x)
    else:
        print("Entrada incorrecta")
except:
        print("Entrada incorrecta")   
    
   
