#Realizado por Gonzalo Montezuma
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "asistencias"
)

def ver():

  tabla = input("Ingrese la tabla que quiere revisar: ")
  Stringyiyi = f"SELECT * FROM  {tabla}"

  mycursor = mydb.cursor()

  mycursor.execute(Stringyiyi)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

def crear():  

  tabla = input("Ingrese la tabla a la que le quiere insertar datos: ")

  mycursor = mydb.cursor()

  if tabla == "estudiantes":
    nombre = input("Ingrese el nombre del estudiante: ")
    grado = input("Ingrese el grado del estudiante: ")

    sql = f"INSERT INTO estudiantes (nombre, grado) VALUES (%s, %s)"
    val = (nombre, grado)
    
  elif tabla == "registro":
    nombrer = input("Ingrese ID del estudiante: ")
    asistente = input("Ingrese si el estudiante asistio o no (1/0): ")
    fecha =  input("Ingrese la fecha de este registro: ")
    hora = input("Ingrese la hora a la que ingresó al establecimiento: ")

    sql = f"INSERT INTO registro (estudiante_id, asistente, fecha, hora) VALUES  (%s, %s, %s, %s)"
    val = (nombrer, asistente, fecha, hora)

  else:
    print("Ingrese una opción válida")
  
  mycursor.execute(sql,val)
  mydb.commit()

def actualizar():

  mycursor = mydb.cursor()

  tabla = input("Ingrese la tabla a la que le quiere actualizar datos: ")

  if tabla == "estudiantes":

    id_estudiante = input("Ingrese el ID del estudiante a quien quiere actualizarle un dato: ")
    campo = input("Ingres el campo que desea actualizar: ")
    newdato = input("Ingrese el nuevo dato: ")

    sql = f"UPDATE estudiantes SET {campo} = '{newdato}' WHERE estudiante_id = {id_estudiante}"

  elif tabla == "registro":

    id_estudiante = input("Ingrese el ID del estudiante a quien quiere actualizarle un dato: ")
    campo = input("Ingres el campo que desea actualizar: ")
    newdato = input("Ingrese el nuevo dato: ")

    sql = f"UPDATE registro SET {campo} = '{newdato}' WHERE estudiante_id = {id_estudiante}"

  mycursor.execute(sql)
  mydb.commit()

crear()