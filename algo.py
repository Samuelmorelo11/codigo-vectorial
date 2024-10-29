import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, integrate, sqrt, pi

# Definir las variables simbólicas
x, y, z, r, theta = symbols('x y z r theta')

# Crear la ventana principal y definir su color de fondo
root = tk.Tk()
root.title("Calculadora de Integrales Dobles y Triples")
root.geometry("600x4000")
root.configure(bg="#f0f8ff")  # Fondo de la ventana principal en azul claro

# Función para calcular las integrales
def calcular_integral():
    opcion = opcion_var.get()
    
    try:
        if opcion == 1:
            resultado = integrate(integrate(x + y, (y, 0, x)), (x, 0, 2))
            resultado_str = f"Resultado: {resultado}"
        
        elif opcion == 2:
            resultado = integrate(integrate(x**2 + y**2, (y, -sqrt(4 - x**2), sqrt(4 - x**2))), (x, -2, 2))
            resultado_str = f"Resultado: {resultado}"
        
        elif opcion == 3:
            resultado = integrate(integrate(sqrt(x**2 + y**2), (y, 0, sqrt(1 - x**2))), (x, 0, 1))
            resultado_str = f"Resultado: {resultado}"
        
        elif opcion == 4:
            resultado = integrate(integrate(integrate(x + y + z, (z, 0, 1)), (y, 0, 1)), (x, 0, 1))
            resultado_str = f"Resultado: {resultado}"
        
        elif opcion == 5:
            resultado = integrate(
                integrate(
                    integrate(x**2 + y**2, (z, -sqrt(4 - x**2 - y**2), sqrt(4 - x**2 - y**2))),
                    (y, -sqrt(4 - x**2), sqrt(4 - x**2))
                ), (x, -2, 2)
            )
            resultado_str = f"Resultado: {resultado}"
        
        elif opcion == 6:
            resultado = integrate(integrate(integrate(r**2, (z, 0, sqrt(1 - r**2))), (r, 0, 1)), (theta, 0, 2*pi))
            resultado_str = f"Resultado: {resultado}"
        
        else:
            resultado_str = "Seleccione una opción válida."
        
        resultado_label.config(text=resultado_str, font=("Arial", 12, "bold"), foreground="#004d00")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Configurar estilos
style = ttk.Style()
style.configure("TLabel", background="#f0f8ff", font=("Arial", 12))  # Fondo de los labels
style.configure("TRadiobutton", background="#f0f8ff", font=("Arial", 10))  # Fondo de los radio buttons

# Crear widgets de la interfaz
opcion_var = tk.IntVar()
ttk.Label(root, text="Seleccione una integral para calcular:", font=("Arial", 14, "bold"), background="#f0f8ff").pack(pady=10)

# Opciones de las integrales
opciones = [
    "Integral doble: ∫∫ (x + y) dy dx, 0 <= y <= x, 0 <= x <= 2",
    "Integral doble: ∫∫ (x^2 + y^2) dx dy, x^2 + y^2 <= 4",
    "Integral doble en coordenadas polares: ∫∫ sqrt(x^2 + y^2) dy dx, 0 <= y <= sqrt(1 - x^2), 0 <= x <= 1",
    "Integral triple: ∫∫∫ (x + y + z) dz dy dx, 0 <= z <= 1, 0 <= y <= 1, 0 <= x <= 1",
    "Integral triple sobre esfera: ∫∫∫ (x^2 + y^2) dz dy dx, x^2 + y^2 + z^2 <= 8",
    "Integral triple en coordenadas cilíndricas: ∫∫∫ r^2 dz dθ dr, 0 <= z <= sqrt(1 - r^2), 0 <= θ <= 2π, 0 <= r <= 1"
]

# Crear un frame para las opciones de selección y darle color de fondo
frame_opciones = tk.Frame(root, bg="#f0f8ff")  # Fondo azul claro para el frame de opciones
frame_opciones.pack(pady=10, padx=20, anchor="w")

for i, texto in enumerate(opciones, start=1):
    ttk.Radiobutton(frame_opciones, text=texto, variable=opcion_var, value=i).pack(anchor="w")

# Botón para calcular la integral con color de fondo y fuente
ttk.Button(root, text="Calcular Integral", command=calcular_integral).pack(pady=15)

# Área para mostrar el resultado con fondo diferenciado
resultado_frame = tk.Frame(root, bg="#e0ffd8", padx=10, pady=10)  # Fondo verde claro para el área de resultados
resultado_frame.pack(fill="x", padx=20, pady=10)

resultado_label = ttk.Label(resultado_frame, text="Resultado:", font=("Arial", 14, "bold"), background="#e0ffd8", foreground="#004d00")
resultado_label.pack(anchor="w")

# Iniciar el loop de la interfaz
root.mainloop()
