import tkinter as tk
import sqlite3
import subprocess
import mysql.connector

class crear_cita:
        
    def _init_(self, master):
        self.master = master
        self.master.title("Registro de citas")
        self.master.config(padx=120, pady=130, bg='#383838')
            
        self.crear_espacios()

    def crear_espacios(self):
        def menú():
            cita.destroy()
            subprocess.call(["python", "Proyecto_menú.py"])
        label_titulo= tk.Label(cita, text="- Agendar cita -", font="Times 30", fg="white", bg="#383838").grid(row=0, column=0, pady=10)
        tk.Label(self.master, text= "Nombre y apellidos:", fg="white", bg="#383838", font="Times 12").grid(row=1, column=0)
        tk.Label(self.master, text= "Fecha de la cita (AMD):", fg="white", bg="#383838", font="Times 12").grid(row=2, column=0)
        tk.Label(self.master, text= "Hora (24hrs):", fg="white", bg="#383838", font="Times 12").grid(row=3, column=0)

        def limitar_entry(entrada, limit):
            def limitar(event):
                texto = entrada.get()
                if len(texto)>=limit and not event.keysym=='BackSpace':
                    return "break"
            entrada.bind("<Key>", limitar)  
        def letra(char):
            return char in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ "
        validatecommand = cita.register(letra)
        self.nombre_entry= tk.Entry(self.master, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
        limitar_entry(self.nombre_entry,30)
        self.nombre_entry.grid(row=1, column=1)
        
        def numero(char):
            return char in "0123456789/"
        validatecommand = cita.register(numero)
        self.fecha_entry= tk.Entry(self.master, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
        limitar_entry(self.fecha_entry,10)
        self.fecha_entry.grid(row=2, column=1)

        def numero(char):
            return char in "0123456789:"
        validatecommand = cita.register(numero)
        self.hora_entry= tk.Entry(self.master, bg="#424242", fg="white", validate="key", validatecommand=(validatecommand, "%S"))
        limitar_entry(self.hora_entry,8)
        self.hora_entry.grid(row=3, column=1)

        self.registrar_button= tk.Button(self.master, text="Registrar citas", command=self.registrar_cita, bg="#585858", fg="white")
        self.registrar_button.grid(row=4, column=1)
        
        regresar_button=tk.Button(self.master, text="Regresar", command=menú, fg="white", bg="#585858")
        regresar_button.grid(row=5, column=1)

        self.registro_exitoso_label=tk.Label(self.master, text="", fg="white", bg="#383838")
        self.registro_exitoso_label.grid(row=6, column=1)

    def registrar_cita(self):
        nombre = self.nombre_entry.get()
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()

     
        try:
            connection = mysql.connector.connect(host='localhost', database='veterinario', user='root', password='')

            mySql_insert_query = """INSERT INTO veterinario (nombre_apellido, fecha, hora) VALUES ('"""+nombre+"','"+fecha+"','" + hora + "')" 
         
            print(mySql_insert_query)
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into veterinario table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into veterinario table {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

        self.nombre_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)

        self.registro_exitoso_label.configure(text="!REGISTRO EXITOSO¡")


cita = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = cita.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = cita.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
cita.geometry(posicion)
crear = crear_cita(cita)
cita.resizable(width=0, height=0)
cita.mainloop()
