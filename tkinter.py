import tkinter as tk
import threading
import time

def boton_pulsado():
    print("¡El botón ha sido pulsado!")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ventana con Botón")
    
    boton = tk.Button(ventana, text="Pulsar", command=boton_pulsado)
    boton.pack(pady=20)
    
    ventana.mainloop()

# Iniciar la interfaz gráfica en un hilo separado
hilo_gui = threading.Thread(target=crear_ventana)
hilo_gui.daemon = True  # El hilo se cerrará cuando el programa principal termine
hilo_gui.start()

# Programa principal
for i in range(10):
    print(f"Ejecutando tarea principal {i}")
    time.sleep(1)

print("Programa principal terminado")
