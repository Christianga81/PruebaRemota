import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hola Mundo")
ventana.geometry("300x200")

# Crear una etiqueta con el mensaje
etiqueta = tk.Label(ventana, text="¡Hola Mundo!", font=("Arial", 16))
etiqueta.pack(pady=50) 

# Crear un botón para mostrar un mensaje
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Hola desde la ventana!")

boton = tk.Button(ventana, text="Hacer clic aquí", command=mostrar_mensaje)
boton.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()