import tkinter as tk
from tkinter import messagebox

# Nombre del autor (debes agregar más nombres antes de entregar)
autor = "Miguel Ángel Rivillas"

# Función 1: Mostrar autor del trabajo
def mostrar_autor():
    mensaje = f"Trabajo realizado por:\n- {autor}"
    messagebox.showinfo("Autor del trabajo", mensaje)

# Función 2: Formulario para calcular el cuadrado de un número
def formulario_cuadrado():
    def calcular():
        try:
            numero = float(entrada.get())
            resultado = numero ** 2
            messagebox.showinfo("Resultado", f"El cuadrado de {numero} es {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    ventana_formulario = tk.Toplevel()
    ventana_formulario.title("Formulario: Calcular cuadrado")
    ventana_formulario.geometry("300x150")

    etiqueta = tk.Label(ventana_formulario, text="Ingrese un número:")
    etiqueta.pack(pady=5)

    entrada = tk.Entry(ventana_formulario)
    entrada.pack(pady=5)

    boton_calcular = tk.Button(ventana_formulario, text="Calcular", command=calcular)
    boton_calcular.pack(pady=10)

# Función 3: Interacción con el puntero del mouse
def cambiar_puntero():
    def saludo():
        messagebox.showinfo("¡Hola!", "¡Gracias por pasar el mouse!")

    ventana_puntero = tk.Toplevel()
    ventana_puntero.title("Interacción con el puntero")
    ventana_puntero.geometry("300x150")

    boton = tk.Button(ventana_puntero, text="Pasa el mouse por aquí", command=saludo)
    boton.pack(pady=40)

    # Cambia el cursor al pasar el mouse
    boton.bind("<Enter>", lambda e: boton.config(cursor="hand2"))
    boton.bind("<Leave>", lambda e: boton.config(cursor="arrow"))

# Ventana principal
def ventana_principal():
    root = tk.Tk()
    root.title("Proyecto GUI - Lógica de Programación")
    root.geometry("400x300")

    etiqueta = tk.Label(root, text="Seleccione una opción:", font=("Arial", 14))
    etiqueta.pack(pady=20)

    boton1 = tk.Button(root, text="Mostrar autor", width=25, command=mostrar_autor)
    boton1.pack(pady=10)

    boton2 = tk.Button(root, text="Formulario: Calcular cuadrado", width=25, command=formulario_cuadrado)
    boton2.pack(pady=10)

    boton3 = tk.Button(root, text="Interacción con puntero", width=25, command=cambiar_puntero)
    boton3.pack(pady=10)

    boton_salir = tk.Button(root, text="Salir", width=25, command=root.destroy)
    boton_salir.pack(pady=20)

    root.mainloop()

# Ejecutar el programa
ventana_principal()