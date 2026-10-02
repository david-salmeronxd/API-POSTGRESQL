import tkinter as tk
from tkinter import ttk, messagebox
import urllib.request
import json

API_URL = "http://localhost:3000/api/productos"

def cargar_productos():
    """Obtiene los productos de la API y los muestra en la tabla."""
    for row in tabla.get_children():
        tabla.delete(row)

    try:
        req = urllib.request.Request(API_URL, method='GET')
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                productos = json.loads(response.read().decode('utf-8'))
                for p in productos:
                    tabla.insert("", tk.END, values=(
                        p.get("id"),
                        p.get("nombre"),
                        f"${p.get('precio'):.2f}",
                        p.get("descripcion") or "Sin descripción"
                    ))
            else:
                messagebox.showerror("Error", f"Estado: {response.status}")
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo obtener los datos:\n{e}")

def enviar_producto():
    """Envía un nuevo producto a la API."""
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    descripcion = entry_descripcion.get().strip()

    if not nombre or not precio:
        messagebox.showwarning("Campos obligatorios", "Ingresa el nombre y el precio.")
        return

    try:
        precio_float = float(precio)
    except ValueError:
        messagebox.showerror("Error de formato", "El precio debe ser un número válido.")
        return

    payload = json.dumps({
        "nombre": nombre,
        "precio": precio_float,
        "descripcion": descripcion
    }).encode('utf-8')

    req = urllib.request.Request(
        API_URL, 
        data=payload, 
        headers={'Content-Type': 'application/json'},
        method='POST'
    )

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                messagebox.showinfo("Éxito", "Producto registrado correctamente")
                limpiar_campos()
                cargar_productos()
            else:
                messagebox.showerror("Error", f"Estado: {response.status}")
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la API:\n{e}")

def eliminar_producto():
    """Elimina el producto seleccionado en la tabla."""
    item_seleccionado = tabla.selection()
    if not item_seleccionado:
        messagebox.showwarning("Atención", "Por favor selecciona un producto de la tabla.")
        return

    valores = tabla.item(item_seleccionado, 'values')
    producto_id = valores[0]
    nombre_prod = valores[1]

    confirmar = messagebox.askyesno(
        "Confirmar eliminación", 
        f"¿Estás seguro de que deseas eliminar '{nombre_prod}' (ID: {producto_id})?"
    )
    if not confirmar:
        return

    url_delete = f"{API_URL}/{producto_id}"
    req = urllib.request.Request(url_delete, method='DELETE')

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
                cargar_productos()
            else:
                messagebox.showerror("Error", f"Estado: {response.status}")
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo eliminar el producto:\n{e}")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

root = tk.Tk()
root.title("Gestión de Productos - API PostgreSQL")
root.geometry("640x560")
root.resizable(False, False)

frame_form = tk.LabelFrame(root, text=" Registrar Nuevo Producto ", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_form.pack(fill="x", padx=15, pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(frame_form, width=25)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Precio ($):").grid(row=0, column=2, sticky="w", pady=5)
entry_precio = tk.Entry(frame_form, width=15)
entry_precio.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_form, text="Descripción:").grid(row=1, column=0, sticky="w", pady=5)
entry_descripcion = tk.Entry(frame_form, width=50)
entry_descripcion.grid(row=1, column=1, columnspan=3, sticky="w", padx=5, pady=5)

btn_guardar = tk.Button(
    frame_form, 
    text="Guardar Producto", 
    bg="#28a745", 
    fg="white", 
    font=("Arial", 9, "bold"),
    command=enviar_producto
)
btn_guardar.grid(row=2, column=0, columnspan=4, pady=10)

frame_tabla = tk.LabelFrame(root, text=" Productos en Base de Datos ", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_tabla.pack(fill="both", expand=True, padx=15, pady=(0, 10))

columnas = ("id", "nombre", "precio", "descripcion")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)

tabla.heading("id", text="ID")
tabla.heading("nombre", text="Nombre")
tabla.heading("precio", text="Precio")
tabla.heading("descripcion", text="Descripción")

tabla.column("id", width=40, anchor="center")
tabla.column("nombre", width=150)
tabla.column("precio", width=80, anchor="e")
tabla.column("descripcion", width=280)

scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

frame_acciones = tk.Frame(root)
frame_acciones.pack(pady=(0, 15))

btn_refrescar = tk.Button(
    frame_acciones, 
    text="🔄 Actualizar Tabla", 
    font=("Arial", 9),
    command=cargar_productos
)
btn_refrescar.pack(side="left", padx=10)

btn_eliminar = tk.Button(
    frame_acciones, 
    text="🗑️ Eliminar Seleccionado", 
    bg="#dc3545", 
    fg="white", 
    font=("Arial", 9, "bold"),
    command=eliminar_producto
)
btn_eliminar.pack(side="left", padx=10)

cargar_productos()

root.mainloop()