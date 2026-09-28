import random
import tkinter as tk

# --- Configuración de la Ventana ---
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera - Versión Visual")
ventana.geometry("1520x820")
ventana.config(bg="#f0f0f0")

# Variables de puntaje
victorias_usuario = 0
victorias_maquina = 0


# --- Funciones ---
def jugar(usuario):
  global victorias_usuario, victorias_maquina

  opciones = ["piedra", "papel", "tijera"]
  maquina = random.choice(opciones)

  # Lógica
  if usuario == maquina:
    resultado = "¡Empate!"
    color = "orange"
  elif (
      (usuario == "piedra" and maquina == "tijera")
      or (usuario == "papel" and maquina == "piedra")
      or (usuario == "tijera" and maquina == "papel")
  ):
    resultado = "¡Ganaste esta ronda!"
    color = "green"
    victorias_usuario += 1
  else:
    resultado = "¡Perdiste esta ronda!"
    color = "red"
    victorias_maquina += 1

  # Actualizar textos en pantalla
  label_jugada.config(
      text=f"Vos elegiste: {usuario.upper()}  |  La máquina: {maquina.upper()}"
  )
  label_resultado.config(text=resultado, fg=color)
  label_marcador.config(
      text=f"Marcador -> Vos: {victorias_usuario} | Máquina: {victorias_maquina}"
  )


def reiniciar():
  global victorias_usuario, victorias_maquina
  victorias_usuario = 0
  victorias_maquina = 0
  label_marcador.config(text="Vos: 0 | Máquina: 0")
  label_resultado.config(text="¡Elegí una opción para empezar!", fg="blue")
  label_jugada.config(text="")


# --- Elementos Visuales (Widgets) ---

tk.Label(
    ventana,
    text="Piedra, Papel o Tijera",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
).pack(pady=15)

label_marcador = tk.Label(
    ventana, text="Vos: 0 | Máquina: 0", font=("Arial", 14), bg="#f0f0f0"
)
label_marcador.pack(pady=5)

label_jugada = tk.Label(ventana, text="", font=("Arial", 12), bg="#f0f0f0")
label_jugada.pack(pady=15)

label_resultado = tk.Label(
    ventana,
    text="¡Elegí una opción para empezar!",
    font=("Arial", 14, "bold"),
    fg="blue",
    bg="#f0f0f0",
)
label_resultado.pack(pady=10)

# --- Botones de Opciones ---
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=20)

btn_piedra = tk.Button(
    frame_botones,
    text="Piedra 🪨",
    font=("Arial", 12),
    width=10,
    bg="lightgray",
    command=lambda: jugar("piedra"),
)
btn_piedra.grid(row=0, column=0, padx=5)

btn_papel = tk.Button(
    frame_botones,
    text="Papel 📄",
    font=("Arial", 12),
    width=10,
    bg="lightgray",
    command=lambda: jugar("papel"),
)
btn_papel.grid(row=0, column=1, padx=5)

btn_tijera = tk.Button(
    frame_botones,
    text="Tijera ✂️",
    font=("Arial", 12),
    width=10,
    bg="lightgray",
    command=lambda: jugar("tijera"),
)
btn_tijera.grid(row=0, column=2, padx=5)

# Botón Reiniciar
tk.Button(
    ventana,
    text="Reiniciar Partida",
    font=("Arial", 10),
    bg="#ff9999",
    command=reiniciar,
).pack(pady=20)

# --- Bucle Principal ---
ventana.mainloop()