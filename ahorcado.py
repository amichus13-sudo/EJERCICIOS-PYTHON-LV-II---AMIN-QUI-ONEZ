import random
import tkinter as tk
from tkinter import messagebox

# Lista de palabras secretas para el juego
PALABRAS = [
    "PYTHON",
    "PROGRAMACION",
    "COMPUTADORA",
    "TECNOLOGIA",
    "DESARROLLO",
    "UNINORTE",
    "MULTI",
    "TERERE",
    "MASIVO",
    "INFORMATICA",
    "PALABRA",
    "CONTRASEÑA",
    "PROGRAMADOR",
    "MESSI",
    "FREEFIRE",
    "ROBLOX",
    "CR7",
    "ALFARO",
    "ASADO",
    "COCACOLA",
    "CHATGPT",
    "GEMINI",
    "MOUSE",
    "MONITOR",
    "COLEGIO",
]

class AhorcadoApp:

  def __init__(self, ventana):
    self.ventana = ventana
    self.ventana.title("Juego del Ahorcado")
    self.ventana.geometry("1520x820")
    self.ventana.config(bg="#f0f4f8")
    self.ventana.resizable(False, False)

    self.reiniciar_variables()

    # --- Elementos Visuales (Widgets) ---
    self.label_titulo = tk.Label(
        ventana,
        text="🎮 El Juego del Ahorcado",
        font=("Arial", 16, "bold"),
        bg="#f0f4f8",
        fg="#333",
    )
    self.label_titulo.pack(pady=15)

    self.label_intentos = tk.Label(
        ventana,
        text=f"Vidas restantes: {self.intentos}",
        font=("Arial", 12, "bold"),
        bg="#f0f4f8",
        fg="red",
    )
    self.label_intentos.pack(pady=5)

    # Palabra oculta con guiones bajos
    self.label_palabra = tk.Label(
        ventana,
        text=self.obtener_palabra_mostrada(),
        font=("Courier", 22, "bold"),
        bg="#f0f4f8",
        fg="#2c3e50",
    )
    self.label_palabra.pack(pady=20)

    self.label_letras = tk.Label(
        ventana,
        text="Letras usadas: Ninguna",
        font=("Arial", 10),
        bg="#f0f4f8",
    )
    self.label_letras.pack(pady=5)

    # Entrada de texto para escribir la letra
    self.entry_letra = tk.Entry(
        ventana, font=("Arial", 14), width=5, justify="center"
    )
    self.entry_letra.pack(pady=10)
    self.entry_letra.focus()
    # Permitir presionar la tecla Enter para adivinar directamente
    self.entry_letra.bind("<Return>", lambda event: self.verificar_letra())

    self.btn_adivinar = tk.Button(
        ventana,
        text="Adivinar Letra",
        font=("Arial", 11, "bold"),
        bg="#3498db",
        fg="white",
        command=self.verificar_letra,
    )
    self.btn_adivinar.pack(pady=5)

    self.btn_reiniciar = tk.Button(
        ventana,
        text="Reiniciar Juego",
        font=("Arial", 10),
        bg="#95a5a6",
        fg="white",
        command=self.reiniciar_partida,
    )
    self.btn_reiniciar.pack(pady=10)

  def reiniciar_variables(self):
    self.palabra_secreta = random.choice(PALABRAS)
    self.letras_adivinadas = set()
    self.intentos = 6

  def obtener_palabra_mostrada(self):
    # Muestra la letra si fue adivinada, o un guión bajo si no
    return " ".join(
        letra if letra in self.letras_adivinadas else "_"
        for letra in self.palabra_secreta
    )

  def verificar_letra(self):
    letra = self.entry_letra.get().upper().strip()
    self.entry_letra.delete(0, tk.END)

    # Validaciones básicas
    if not letra or len(letra) != 1 or not letra.isalpha():
      messagebox.showwarning(
          "Aviso", "Por favor, ingresá una sola letra válida."
      )
      return

    if letra in self.letras_adivinadas:
      messagebox.showinfo("Información", f"Ya habías probado la letra '{letra}'.")
      return

    # Agregar al conjunto de letras intentadas
    self.letras_adivinadas.add(letra)

    # Comprobar si la letra está en la palabra secreta
    if letra in self.palabra_secreta:
      # Verificar si ya completó todas las letras (ganó)
      if all(l in self.letras_adivinadas for l in self.palabra_secreta):
        self.label_palabra.config(text=" ".join(self.palabra_secreta))
        messagebox.showinfo(
            "¡Felicitaciones!", "¡Ganaste! Adivinaste la palabra completa."
        )
        self.reiniciar_partida()
    else:
      self.intentos -= 1
      if self.intentos == 0:
        self.label_palabra.config(text=" ".join(self.palabra_secreta))
        messagebox.showerror(
            "Game Over", f"¡Perdiste! La palabra era: {self.palabra_secreta}"
        )
        self.reiniciar_partida()

    # Actualizar la interfaz
    self.actualizar_interfaz()

  def actualizar_interfaz(self):
    self.label_palabra.config(text=self.obtener_palabra_mostrada())
    self.label_intentos.config(text=f"Vidas restantes: {self.intentos}")
    letras_ordenadas = ", ".join(sorted(list(self.letras_adivinadas)))
    self.label_letras.config(
        text=f"Letras usadas: {letras_ordenadas or 'Ninguna'}"
    )

  def reiniciar_partida(self):
    self.reiniciar_variables()
    self.actualizar_interfaz()


# --- Ejecución de la Aplicación ---
if __name__ == "__main__":
  root = tk.Tk()
  app = AhorcadoApp(root)
  root.mainloop()