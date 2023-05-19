import tkinter as tk
import sqlite3
import subprocess

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    raza = entry_raza.get()
    peso = entry_peso.get()

    conn = sqlite3.connect("mascota.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos_personales (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            edad TEXT,
            raza TEXT,
            peso TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO datos_personales (nombre, edad, raza, peso)
        VALUES (?, ?, ?, ?)
    """, (nombre, edad, raza, peso))

    conn.commit()
    conn.close()

    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_raza.delete(0, tk.END)
    entry_peso.delete(0, tk.END)

root = tk.Tk()
root.title("Registro de Mascotas")
ancho_ventana = 620
alto_ventana = 480
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root['bg'] = "#383838"

def limitar_entry(entrada, limit):
    def limitar(event):
        texto = entrada.get()
        if len(texto)>=limit and not event.keysym=='BackSpace':
            return "break"
    entrada.bind("<Key>", limitar)

label_titulo = tk.Label(root, text="- REGISTRO DE MASCOTAS -", font="Times 20", fg="white")
label_titulo.pack(pady=20)
label_titulo['bg']="#383838"
label_nombre = tk.Label(root, text="Nombre:", font="Times", fg="white", )
label_nombre['bg']="#383838"
label_nombre.pack()
def letra(char):
    return char in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ"
validatecommand = root.register(letra)
entry_nombre = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_nombre,10)
entry_nombre.pack()

label_edad = tk.Label(root, text="Edad:", font="Times", fg='white')
label_edad['bg']="#383838"
label_edad.pack()
def numero(char):
    return char in "0123456789"
validatecommand = root.register(numero)
entry_edad = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_edad,2)
entry_edad.pack()

label_raza = tk.Label(root, text="Raza:", font="Times", fg='white')
label_raza['bg']="#383838"
label_raza.pack()
def letra(char):
    return char in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ "
validatecommand = root.register(letra)
entry_raza = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_raza,10)
entry_raza.pack()

label_peso = tk.Label(root, text="Peso (kg):", font="Times", fg= 'white')
label_peso['bg']="#383838"
label_peso.pack()
def numero(char):
    return char in "0123456789"
validatecommand = root.register(numero)
entry_peso = tk.Entry(root, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(entry_peso,2)
entry_peso.pack()

button_guardar = tk.Button(root, text="Guardar", command=guardar_datos, font="Times", bg="#585858", fg="white")
button_guardar.pack(pady=30)

def menú():
    root.destroy()
    subprocess.call(["python", "Proyecto_menú.py"]) 

button_guardar = tk.Button(root, text="Regresar", command=menú, font="Times", bg="#585858", fg="white")
button_guardar.pack(pady=20)

root.resizable(width=0, height=0)
root.mainloop()