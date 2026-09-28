import random
import string
import tkinter as tk
from tkinter import messagebox

def generar_password():
  # Obtener la longitud del slider
  longitud = scale_longitud.get()

  # Construir el conjunto de caracteres según los checkboxes activos
  caracteres = ""
  if var_minus.get():
    caracteres += string.ascii_lowercase
  if var_mayus.get():
    caracteres += string.ascii_uppercase
  if var_nums.get():
    caracteres += string.digits
  if var_simbs.get():
    caracteres += string.punctuation

  # Validar que al menos una opción esté marcada
  if not caracteres:
    messagebox.showwarning(
        "Cuidado", "¡Tenés que seleccionar al menos una opción!"
    )
    return

  # Generar contraseña aleatoria
  password = "".join(random.choice(caracteres) for _ in range(longitud))

  # Mostrar el resultado en la caja de texto (habilitándola temporalmente)
  entry_resultado.config(state="normal")
  entry_resultado.delete(0, tk.END)
  entry_resultado.insert(0, password)
  entry_resultado.config(state="readonly")


def copiar_portapapeles():
  password = entry_resultado.get()
  if password:
    ventana.clipboard_clear()
    ventana.clipboard_append(password)
    messagebox.showinfo("¡Listo!", "Contraseña copiada al portapapeles 📋")


# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("ClaveSegura - Generador Visual")
ventana.geometry("1520x820")
ventana.config(bg="#f4f4f9")
ventana.resizable(False, False)

# Título
tk.Label(
    ventana,
    text="ClaveSegura 🔒",
    font=("Arial", 18, "bold"),
    bg="#f4f4f9",
    fg="#333",
).pack(pady=15)

# Slider para la longitud
tk.Label(
    ventana, text="Longitud de la contraseña:", font=("Arial", 11), bg="#f4f4f9"
).pack(anchor="w", padx=50)
scale_longitud = tk.Scale(
    ventana, from_=6, to=32, orient="horizontal", bg="#f4f4f9", length=300
)
scale_longitud.set(12)  # Valor por defecto inicial
scale_longitud.pack(pady=5)

# Opciones con Checkbuttons (Casillas de verificación)
frame_opciones = tk.Frame(ventana, bg="#f4f4f9")
frame_opciones.pack(pady=10)

var_minus = tk.BooleanVar(value=True)
var_mayus = tk.BooleanVar(value=True)
var_nums = tk.BooleanVar(value=True)
var_simbs = tk.BooleanVar(value=True)

tk.Checkbutton(
    frame_opciones,
    text="Incluir minúsculas (a-z)",
    variable=var_minus,
    bg="#f4f4f9",
    font=("Arial", 10),
).pack(anchor="w", pady=2)
tk.Checkbutton(
    frame_opciones,
    text="Incluir mayúsculas (A-Z)",
    variable=var_mayus,
    bg="#f4f4f9",
    font=("Arial", 10),
).pack(anchor="w", pady=2)
tk.Checkbutton(
    frame_opciones,
    text="Incluir números (0-9)",
    variable=var_nums,
    bg="#f4f4f9",
    font=("Arial", 10),
).pack(anchor="w", pady=2)
tk.Checkbutton(
    frame_opciones,
    text="Incluir símbolos (!@#$)",
    variable=var_simbs,
    bg="#f4f4f9",
    font=("Arial", 10),
).pack(anchor="w", pady=2)

# Botón principal para generar
tk.Button(
    ventana,
    text="Generar Contraseña",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=22,
    command=generar_password,
).pack(pady=15)

# Área de resultado y botón de copiado rápido
frame_resultado = tk.Frame(ventana, bg="#f4f4f9")
frame_resultado.pack(pady=5)

entry_resultado = tk.Entry(
    frame_resultado,
    font=("Courier", 12, "bold"),
    width=18,
    justify="center",
    state="readonly",
)
entry_resultado.pack(side="left", padx=5)

tk.Button(
    frame_resultado,
    text="📋 Copiar",
    bg="#2196F3",
    fg="white",
    font=("Arial", 10),
    command=copiar_portapapeles,
).pack(side="left")

# --- Bucle Principal ---
ventana.mainloop()