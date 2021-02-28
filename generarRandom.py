import random
import csv

for n in range(0,100):
    codigo = ""
    numAleatorio = 0
    operacion = ""
    direccion = ""
    telefono = ""
    monto = "Q. "
    nombre = ""
    instruccion = []
    numAleatorio = random.randint(1,3)
    if (numAleatorio == 1):
        operacion = "caja_abierta"
    elif(numAleatorio == 2):
        operacion = "caja_eliminada"
    elif(numAleatorio == 3):
        operacion = "C_caja"
        
    for i in range(0,4):
        if(random.randint(0,1) == 0):
            codigo += chr(random.randint(48,57))
        else:
            codigo += chr(random.randint(65,90))
    codigo += "-BC52"

    direccion += str(random.randint(1,21))
    if (random.randint(0,1) == 0):
        direccion += " AVENIDA "
    else:
        direccion += " CALLE "
    direccion += "ZONA " + str(random.randint(1,21))

    for i in range(0,8):
        telefono += str(random.randint(0,9))

    monto += str(random.randint(500,50000))

    for i in range(0,9):
        nombre += chr(random.randint(65,90))
    instruccion.append(operacion)
    if (operacion == "C_caja"):
        codigo = codigo + "/" + nombre + "/" + telefono + "/" + direccion + "/" + monto
        instruccion.append(codigo)
    else:
        instruccion.append(codigo)

    with open('PRUEBA JMETER/PRUEBA.csv', 'a', newline='') as writeFile:
        writer = csv.writer(writeFile, delimiter=";",  quotechar=',',quoting=csv.QUOTE_MINIMAL,lineterminator ='')
        writer.writerow('\n')
        writer.writerow(instruccion)