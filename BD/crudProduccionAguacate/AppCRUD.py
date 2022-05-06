#Librerías
import sqlite3
from sqlite3 import Error

#Conexión a la base de datos
def crearConexion(rutaBD):    
    try:
        conn = sqlite3.connect(rutaBD)
        print("Conexión exitosa!!!")
        print("Versión de sqlite: ",sqlite3.version)
    except Error as e:
        print(e)            
    #Retornamos la instancia del conector
    return conn

#Read
def consultarTodosTrabajadores(conn):
    sql = "SELECT * FROM Trabajador"
    cur = conn.cursor()
    cur.execute(sql)
    registros = cur.fetchall()
    return registros    

#Create
def crearTrabajador(conn, tuplaTrabajador):
    #('NuevoTRABAJADOR','asdasd','asdasd','aasd',ggg')
    sql = f"INSERT INTO Trabajador (Nombre,CC,Telefono,EPS,ARL) VALUES (?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql,tuplaTrabajador)
    conn.commit()

#Sección principal
#----------------
rutaBD = 'BD_Finca.db'
conn = crearConexion(rutaBD)
#Mientras está abierta la conexión
with conn:
    print("Espacio conectado a la BD")
    
    #Obtener y mostrar todos los trabajadores antes de la modificación
    registrosTrabajadores = consultarTodosTrabajadores(conn)
    for trabajador in registrosTrabajadores:
        print(trabajador)
    
    crearTrabajador(conn,('NuevoTRABAJADOR','105678','312312312','Sanitas','SURA'))    
    
    #Obtener y mostrar todos los trabajadores después de la modificación
    registrosTrabajadores = consultarTodosTrabajadores(conn)
    for trabajador in registrosTrabajadores:
        print(trabajador)
    
    
    

