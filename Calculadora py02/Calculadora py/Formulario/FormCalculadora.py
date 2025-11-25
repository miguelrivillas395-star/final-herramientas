import tkinter as tk
from tkinter import font
from Configuracion import Constantes as cons
import Utileria.utilVentana as utilVentana

class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.confingWindow()
        self.ConstruirWidget()
        self.ConstruirWidgetToggle()
        self.mostrar_mensaje("Forma de interacion, con el teclado o dando click en los botones")


    def mostrar_mensaje(self, texto, duracion=2500):
        # Muestra un mensaje emergente temporal sin afectar la app.
        ventana_msg = tk.Toplevel(self)
        ventana_msg.overrideredirect(True)  # Quitar borde
        ventana_msg.attributes("-topmost", True)  # Siempre encima

        #Colores según el tema actual
        bg_color = cons.ColorFondoDark if self.DarkTheme else cons.ColorFondoLight
        fg_color = cons.ColorTextoDark if self.DarkTheme else cons.ColorTextoLight

        # Posicionar cerca del centro
        x = self.winfo_x() + 100
        y = self.winfo_y() + 100
        ventana_msg.geometry(f"+{x}+{y}")

        etiqueta = tk.Label(
            ventana_msg,
            text=texto,
            bg=bg_color,
            fg=fg_color,
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8,
            relief="ridge",
            borderwidth=2
    )
        etiqueta.pack()

        # Cerrar automáticamente después del tiempo indicado
        ventana_msg.after(duracion, ventana_msg.destroy)


    def ConstruirWidgetToggle(self):
        self.DarkTheme = True  # Inicia en modo oscuro
        FontAwesome = font.Font(family="FontAwesome", size=12)
        self.ThemeButton = tk.Button(
            self,
            text="Modo Claro 🌞",  # ☀️ cuando está en oscuro
            width=13,
            font=FontAwesome,
            bd=0,
            borderwidth=0,
            highlightthickness=0,
            relief=tk.FLAT,
            command=self.ToggleTheme,
            bg=cons.ColorBotonesEspecialesDark,
            fg=cons.ColorTextoDark
        )
        self.ThemeButton.grid(row=0, column=0, columnspan=2, pady=0, padx=0, sticky="nw")
        
    def confingWindow(self):
        self.title("GUI Calculadora")
        self.configure(bg=cons.ColorFondoDark)
        self.attributes("-alpha", 0.96)
        w, h = 370, 570
        utilVentana.centrarVentana(self, w, h)

    def ConstruirWidget(self):
        self.OLabel = tk.Label(self, text="", font=("Arial", 16),
                               fg=cons.ColorTextoDark, bg=cons.ColorFondoDark, justify="right")
        self.OLabel.grid(row=0, column=3, padx=10, pady=10)
        
        self.entry = tk.Entry(self, width=12, font=("Arial", 40), bd=0,
                              fg=cons.ColorTextoDark, bg=cons.ColorCajaTextoDark, justify="right")
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            "C", "%", "<", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=",
        ]

        self.botones = []  # <--- lista para guardarlos

        rowVal, ColVal = 2, 0
        RobotoFont = font.Font(family="Roboto", size=16)

        for button in buttons:
            if button in ["=", "*", "/", "-", "+", "C", "<", "%"]:
                ColorFondo = cons.ColorBotonesEspecialesDark
                buttonFont = font.Font(size=16, weight="bold")
            else:
                ColorFondo = cons.ColorBotonesDark
                buttonFont = RobotoFont

            b = tk.Button(
                self,
                text=button,
                width=11 if button == "=" else 5,
                height=2,
                command=lambda b=button: self.OnButtonClick(b),
                bg=ColorFondo,
                fg=cons.ColorTextoDark,
                relief=tk.FLAT,
                font=buttonFont,
                padx=5,
                pady=5,
                bd=0,
                borderwidth=0,
                highlightthickness=0,
                overrelief='flat'
            )
            b.grid(row=rowVal, column=ColVal, columnspan=2 if button == "=" else 1, pady=5)
            self.botones.append(b)  # <-- guardarlo

            ColVal += 2 if button == "=" else 1
            if ColVal > 3:
                ColVal = 0
                rowVal += 1

    def ToggleTheme(self):
        if self.DarkTheme:  # Cambiar a claro
            self.configure(bg=cons.ColorFondoLight)
            self.entry.config(fg=cons.ColorTextoLight, bg=cons.ColorCajaTextosLight)
            self.OLabel.config(fg=cons.ColorTextoLight, bg=cons.ColorFondoLight)
            self.ThemeButton.configure(text="Modo Oscuro 🌜", bg=cons.ColorBotonesEspecialesLight, fg=cons.ColorTextoLight)

            # Actualizar botones
            for b in self.botones:
                if b["text"] in ["=", "*", "/", "-", "+", "C", "<", "%"]:
                    b.config(bg=cons.ColorBotonesEspecialesLight, fg=cons.ColorTextoLight)
                else:
                    b.config(bg=cons.ColorBotonessLight, fg=cons.ColorTextoLight)
        else:  # Volver a oscuro
            self.configure(bg=cons.ColorFondoDark)
            self.entry.config(fg=cons.ColorTextoDark, bg=cons.ColorCajaTextoDark)
            self.OLabel.config(fg=cons.ColorTextoDark, bg=cons.ColorFondoDark)
            self.ThemeButton.configure(text="Modo Claro 🌞", bg=cons.ColorBotonesEspecialesDark, fg=cons.ColorTextoDark)

            for b in self.botones:
                if b["text"] in ["=", "*", "/", "-", "+", "C", "<", "%"]:
                    b.config(bg=cons.ColorBotonesEspecialesDark, fg=cons.ColorTextoDark)
                else:
                    b.config(bg=cons.ColorBotonesDark, fg=cons.ColorTextoDark)

        self.DarkTheme = not self.DarkTheme#Invertir el tema

    def OnButtonClick (self, value):
        if value == "=":
            try:
                Expression = self.entry.get().replace("%","/100")
                result = eval(Expression) # enterder la expresion algebraica par asi realizar la opracion
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END, str(result))
                operation = Expression + " "+ value
                self.OLabel.config(text=operation)

            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.OLabel.config(text="")
        elif value == "C":
            self.entry.delete(0, tk.END)
            self.OLabel.config(text="")
        elif value == "<":
            CurrentText = self.entry.get()
            if CurrentText:
                NewText = CurrentText[:-1] # Elimina el ultimo caracter
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, NewText)
                self.OLabel.config(text=NewText + "") # Actualizar la etiqueta de operacion
        else:
            CurrentText = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END,CurrentText + value)
            if value == "=":
                self.OLabel.config(text="")