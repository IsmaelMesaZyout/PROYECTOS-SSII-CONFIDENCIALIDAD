##SUMA BASE DE DATOS
from multiprocessing.resource_sharer import stop
import FuncionHash
import AperturaBaseDatos
import time

def run_query(query=''):    
    cursor = AperturaBaseDatos.connection.cursor()
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else:               # Hacer efectiva la escritura de datos 
        data = None
    return data

def comprobacion(user_input):
    try:
        if(int(user_input)):
            return True
    except ValueError:
        return False

suma = 0
suma1 = 0

v = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/new.csv")
p = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/horario_provisional.png")
x = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/ssii.txt")
val =[
    ("new",v),
    ("horario_provisional",p),
    ("ssii", x)
]

cont = 0
for i in val:
    if(cont == len(val)):
        sql1 = "UPDATE terceratabla SET NumeroHash ='"+ i[1] + "'"
        AperturaBaseDatos.cursor.execute(sql1)
        AperturaBaseDatos.connection.commit()
    else:          
        AperturaBaseDatos.cursor.execute("INSERT INTO terceratabla(Nombre,NumeroHash) VALUES (%s, %s)",(i[0], i[1]))
        AperturaBaseDatos.connection.commit()
        cont += 1

while(True):                
    user_input1 = input("¿Qué fichero quieres comprobar? Introduce el codigo de validacion del archivo: ")
    comprobacion(user_input1)
    val3 = "SELECT SumaHashNumero, Nombre FROM terceratabla"
    val3 = run_query(val3)
    print(val3)
    for t in val3:
        if(str(user_input1) == str(t[0])):
            val1 = "SELECT NumeroHash FROM terceratabla WHERE SumaHashNumero='" + str(user_input1) + "'"
            val1 = run_query(val1)
            print(val1)
            val2 = "SELECT NumeroHash FROM segundatabla WHERE Nombre='" + str(t[1]) + "'"
            val2 = run_query(val2)
            print(val2)
            if(comprobacion(user_input1)==True):
                suma = str(t[0]) + str(val2[0][0]) #Servidor
                suma1 = str(user_input1) + str(val1[0][0]) #Cliente
                if(suma1 == suma):
                    print("OK")
                    exit()    
                else:
                    print("NO OK")
                    exit()       