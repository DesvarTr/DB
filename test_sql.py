# Realizado por Gonzalo Montezuma
import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# Configurar la conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="asistencias"
)

# Función para ejecutar el comando SQL y mostrar los resultados
def ver(tabla):
    if tabla == "estudiantes":
        columns = ("ID", "Nombre", "Grado")
        Stringyiyi = "SELECT * FROM estudiantes"
    elif tabla == "registro":
        columns = ("Registro ID", "Estudiante ID", "Asistente", "Fecha", "Hora")
        Stringyiyi = "SELECT * FROM registro"
    else:
        return

    mycursor = mydb.cursor()
    mycursor.execute(Stringyiyi)
    myresult = mycursor.fetchall()

    # Crear una nueva ventana para mostrar los resultados
    results_window = tk.Toplevel()
    results_window.title(f"Resultados - {tabla}")

    # Crear un Treeview para mostrar los resultados en formato de tabla
    tree = ttk.Treeview(results_window, columns=columns, show='headings')

    # Configurar los encabezados del Treeview
    for col in columns:
        tree.heading(col, text=col)

    # Insertar los datos en el Treeview
    for row in myresult:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill='both')

# Función para abrir la ventana con opciones de tablas
def open_table_options():
    table_window = tk.Toplevel()
    table_window.title("Seleccionar Tabla")

    estudiantes_button = tk.Button(table_window, text="Estudiantes", command=lambda: ver("estudiantes"))
    estudiantes_button.pack(pady=10)

    registro_button = tk.Button(table_window, text="Registro", command=lambda: ver("registro"))
    registro_button.pack(pady=10)
   
# Función para crear un estudiante
def crear_estudiante(nombre_entry, grado_entry, window, status_label):
    nombre = nombre_entry.get()
    grado = grado_entry.get()
    
    if not nombre or not grado:
        messagebox.showerror("Error", "Ambos campos deben estar llenos.")
        return

    if len(nombre) > 100:
        messagebox.showerror("Error", "El nombre supera los 100 caracteres, escriba una cadena más corta")
        return
    if len(grado) > 100:
        messagebox.showerror("Error", "El grado supera los 100 caracteres, escriba una cadena más corta")
        return

    mycursor = mydb.cursor()
    sql = "INSERT INTO estudiantes (nombre, grado) VALUES (%s, %s)"
    val = (nombre, grado)
    mycursor.execute(sql, val)
    mydb.commit()

    status_label.config(text="Estudiante creado exitosamente")
    window.after(3000, lambda: status_label.config(text=""))
    
    # Limpiar las cajas de texto después de crear el estudiante
    nombre_entry.delete(0, tk.END)
    grado_entry.delete(0, tk.END)

    # Establecer el foco en la caja de texto del nombre
    nombre_entry.focus_set()

# Función para abrir la ventana para crear un estudiante
def open_create_student():
    create_window = tk.Toplevel()
    create_window.title("Crear Estudiante")

    tk.Label(create_window, text="Ingrese el nombre del estudiante:").pack(pady=5)
    nombre_entry = tk.Entry(create_window)
    nombre_entry.pack(pady=5)

    tk.Label(create_window, text="Ingrese el grado del estudiante:").pack(pady=5)
    grado_entry = tk.Entry(create_window)
    grado_entry.pack(pady=5)

    status_label = tk.Label(create_window, text="")
    status_label.pack(pady=5)

    create_button = tk.Button(create_window, text="Crear", 
                              command=lambda: crear_estudiante(nombre_entry, grado_entry, create_window, status_label))
    create_button.pack(pady=20)

    # Establecer el foco inicial en la caja de texto del nombre
    nombre_entry.focus_set()

# Función para abrir las opciones de creación
def open_create_options():
    create_options_window = tk.Toplevel()
    create_options_window.title("Seleccionar Tipo de Registro")

    estudiantes_button = tk.Button(create_options_window, text="Estudiantes", command=open_create_student)
    estudiantes_button.pack(pady=10)

    # Aquí puedes agregar una función similar para `registro`
    # registro_button = tk.Button(create_options_window, text="Registro", command=open_create_record)
    # registro_button.pack(pady=10)

# Configurar la ventana principal
root = tk.Tk()
root.title("Base de Datos Asistencias")

ver_button = tk.Button(root, text="Ver", command=open_table_options)
ver_button.pack(pady=20)

crear_button = tk.Button(root, text="Crear", command=open_create_options)
crear_button.pack(pady=20)

root.mainloop()