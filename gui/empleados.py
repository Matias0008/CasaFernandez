from modules.init import *


def empleados():
    top_empleados = Toplevel()
    top_empleados.title("Casa Fernandez - Registrar empleado")
    top_empleados.config(width=500, height=500)

    top_empleados.resizable(0, 0)

    frame = Frame(top_empleados)
    frame.grid(column=0, row=0, padx=100, pady=100)
    Label(frame, text="Nombre",
          font=("Helvetica", 16, "bold")).grid(column=0, row=0)
    nombre_var = StringVar()
    nombre_e = Entry(frame, textvariable=nombre_var,
                     width=15, font=("Helvetica", 16))

    nombre_e.grid(column=0, row=1, pady=10)
    Button(frame, text="Agregar", command=lambda: agregar({
        "nombre": nombre_var.get()
    }, top_empleados, nombre_var), font=("Helvetica", 14)).grid(
        column=0, row=2)

    top_empleados.mainloop()


def agregar(data, frame, var):
    actualizar_json("empleados.json", data)
    messagebox.showinfo("Empleado agregado",
                        f"Se agrego el empleado {data['nombre']}", parent=frame)
    var.set("")
