import FuncionHash
import time
import os
import AperturaBaseDatos
from datetime import datetime

sql = "INSERT INTO segundatabla(Nombre,NumeroHash) VALUES (%s, %s)"
#sql1 = "INSERT INTO segundatabla(Nombre,NumeroHash, ID) VALUES (%s, %s, %s)"
p = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/horario_provisional.png")
v = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/new.csv")
x = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/ssii.txt")

lista = []
val =[  
        ("new",v),
        ("horario_provisional",p),
        ("ssii",x)
    ]
AperturaBaseDatos.cursor.executemany(sql,val)
AperturaBaseDatos.connection.commit()
 
def run_query(query=''): 
   
    cursor = AperturaBaseDatos.connection.cursor()
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else:               # Hacer efectiva la escritura de datos 
        data = None
    return data

file = open("./registro.txt", "w")
file.close()
while(True):
    c = 0
    val1 = "SELECT * FROM segundatabla" #se saca la lista del sql
    val1 = run_query(val1)
    print(val1)
    while(c<30):
        
        v = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/new.csv")
        p = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/horario_provisional.png")
        x = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/ssii.txt")

        val =[
            ("new",v),
            ("horario_provisional",p),
            ("ssii",x)
        ]
        
        archivo = "./log/" + str(datetime.now().strftime('%Y_%m'))
        
        file = open(archivo + ".txt", "a")
        
        tf = False
        cambios=[]
        for x,y in zip(val,val1):
            if x != y:
                tf = True
                cambios.append(x[0])
        
        if (tf):
            print("Se ha modificado el hash de un archivo")
            file.write("Día " + str(datetime.now().strftime('%d')) + " a las " + str(datetime.now().strftime('%H:%M')) + ":  FALLO - El/Los archivo/s " + str(cambios) + " ha/n sido modificado/s" + os.linesep)
        else:
            print("No se ha modificado el hash de ningún archivo")
            file.write("Día " + str(datetime.now().strftime('%d')) + " a las " + str(datetime.now().strftime('%H:%M')) + ":  ACIERTO - El arhivo no ha sido alterado" + os.linesep)        
        file.close()
        c=c+1
        
        time.sleep(10) 
        despues = "./log/" + str(datetime.now().strftime('%Y_%m'))
        if despues != archivo:
            file = open(archivo + ".txt", "r")
            cont = 0
            print(despues)
            print(archivo)
            for line in file: 
                line = line.strip() 
                words = line.split(" ")     
                for word in words: 
                    if word == 'FALLO':
                        cont = cont + 1
            file = open(archivo + ".txt", "a")
            file.write(os.linesep + "Han ocurrido un total de " + str(cont) + " fallos")
            file.close()

