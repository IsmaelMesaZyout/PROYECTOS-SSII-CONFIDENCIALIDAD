from mysql.connector import Error
import mysql.connector
import FuncionHash
import time 
try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3307,
        user='root',
        password='ismael',
        db='ssii_pruebas'
    )

    if connection.is_connected():
        print("Conexión exitosa.")
        infoServer = connection.get_server_info()
        print("Info del servidor: {}".format(infoServer))
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("Conectado a la base de datos: {}".format(row))
except Error as ex:
    print("Error durante la conexión: {}".format(ex))


cursor = connection.cursor()
sql = "INSERT INTO segundatabla(Nombre,NumeroHash) VALUES (%s, %s)"
#sql1 = "INSERT INTO segundatabla(Nombre,NumeroHash, ID) VALUES (%s, %s, %s)"
p = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/horario_provisional.png")
v = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/new.csv")

lista = []
c = True
val =[
        ("horario_provisional",p),
        ("new",v)
    ]
cursor.executemany(sql,val)
connection.commit()

def run_query(query=''): 
   
    cursor = connection.cursor()
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else:               # Hacer efectiva la escritura de datos 
        data = None
    return data


while(c):
    time.sleep(5) 
    val1 = "SELECT * FROM segundatabla" #se saca la lista del sql
    val1 = run_query(val1)
    v = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/new.csv")
    p = FuncionHash.getmd5file("C:/Users/Ismael/Desktop/horario_provisional.png")
    val =[
        ("new",v),
        ("horario_provisional",p)
    ]
    if (val != val1):
        print("Se ha modificado el hash de un archivo")
    else:
        print("nothing")