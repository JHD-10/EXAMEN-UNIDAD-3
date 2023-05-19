import tkinter as tktk
import subprocess

class MenuScreen(tktk.Frame):   

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Ejemplo de pantalla con menú")

        def usuario():
            root.destroy()
            subprocess.call(["python", "usuario.py",])  
        
        def mascota():
            root.destroy()
            subprocess.call(["python", "mascota.py"])

        def agendar():
            root.destroy()
            subprocess.call(["python", "agendar.py"])

        def administrador():
            root.destroy()
            subprocess.call(["python", "administrador.py"])
            
        
        # Agregamos algunos widgets a la pantalla
        self.label = tktk.Label(self, text="¡Bienvenido a Veterinaria Animalandia!", font="Times 20", fg="white")
        self.label['bg'] = '#383838'
        self.label.pack(pady=40)

        self.button = tktk.Button(self, text="Si eres nuevo, registrate aquí!!", font="Times 10", command=usuario, fg="white")
        self.button['bg'] = '#585858'
        self.button.pack(padx=5 , pady=20)
    
        self.button = tktk.Button(self, text="Registra a tu mascota con nosotros!!", font="Times 10", command=mascota, fg="white")
        self.button.pack(padx=5 , pady=20)
        self.button['bg'] = '#585858'

        self.button = tktk.Button(self, text="Agenda una cita para tu mascota!!", font="Times 10", command=agendar, fg="white")
        self.button.pack(padx=5 , pady=20)
        self.button['bg'] = '#585858'

        self.button = tktk.Button(self, text="Si eres administrador, inicia sesión aquí", font="Times 10", command=administrador, fg="white")
        self.button.pack(padx=5 , pady=20)
        self.button['bg'] = '#585858'

        self.button = tktk.Button(self, text="Cerrar", font="Times 10", command=root.quit, fg="white")
        self.button['bg'] = '#585858'
        self.button.pack(padx=5 , pady=20)
    
        self.pack()
        

root = tktk.Tk()
root.resizable(width=0, height=0)
ancho_ventana = 620
alto_ventana = 480
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root['bg'] = '#383838'
app = MenuScreen(root)
app['bg'] = '#383838'
app.mainloop()