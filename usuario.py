import tkinter as tk
import sqlite3
import subprocess

# Función para guardar los datos ingresados por el usuario en la base de datos
def guardar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    domicilio = entry_domicilio.get()
    telefono = entry_telefono.get()

    # Conectar a la base de datos
    conn = sqlite3.connect("datos_personales.db")
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos_personales (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            domicilio TEXT,
            telefono TEXT
        )
    """)

    # Insertar los datos en la tabla
    cursor.execute("""
        INSERT INTO datos_personales (nombre, apellido, domicilio, telefono)
        VALUES (?, ?, ?, ?)
    """, (nombre, apellido, domicilio, telefono))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    # Limpiar los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_domicilio.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Datos Personales")
ancho_ventana = 620
alto_ventana = 480
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root['bg'] = "#383838"

# Crear los campos de entrada para los datos
label_titulo = tk.Label(root, text="- REGISTRO DE DATOS -", font="Times 20", fg="white")
label_titulo.pack(pady=20)
label_titulo['bg']="#383838"
label_nombre = tk.Label(root, text="Nombre:", font="Times", fg="white", )
label_nombre['bg']="#383838"
label_nombre.pack()

def limitar_entry(entrada, limit):
    def limitar(event):
        texto = entrada.get()
        if len(texto)>=limit and not event.keysym=='BackSpace':
            return "break"
    entrada.bind("<Key>", limitar)

def letra(char):
    return char in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ"
validatecommand = root.register(letra)
entry_nombre = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_nombre,20)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:", font="Times", fg='white')
label_apellido['bg']="#383838"
label_apellido.pack()
entry_apellido = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_apellido, 20)
entry_apellido.pack()

def domicilio(char):
    return char in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ0123456789 "
validatecommand = root.register(domicilio)
label_domicilio = tk.Label(root, text="Domicilio:", font="Times", fg='white')
label_domicilio['bg']="#383838"
label_domicilio.pack()
entry_domicilio = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_domicilio, 25)
entry_domicilio.pack()

def telefono(char):
    return char in "0123456789"
validatecommand = root.register(telefono)
label_telefono = tk.Label(root, text="Teléfono:", font="Times", fg= 'white')
label_telefono['bg']="#383838"
label_telefono.pack()
entry_telefono = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_telefono, 10)
entry_telefono.pack()

def menú():
    root.destroy()
    subprocess.call(["python", "Proyecto_menú.py"]) 

# Crear un botón para guardar los datos
button_guardar = tk.Button(root, text="Guardar", command=guardar_datos, font="Times", bg="#585858", fg="white")
button_guardar.pack(pady=20)

button_guardar = tk.Button(root, text="Regresar", command=menú, font="Times", bg="#585858", fg="white")
button_guardar.pack(pady=20)
# Iniciar el bucle de eventos de la ventana
root.resizable(width=0, height=0)
root.mainloop()