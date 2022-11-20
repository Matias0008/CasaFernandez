from modules.init import *


def vajillas():
    top_empleados = Toplevel()
    top_empleados.title("Casa Fernandez - Registrar vajilla")
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
        "id": conseguir_ultima_id(conseguir_vajillas()) + 1,
        "nombre": nombre_var.get()
    }, top_empleados, nombre_var), font=("Helvetica", 14)).grid(
        column=0, row=2)

    top_empleados.mainloop()


def agregar(data, frame, var):
    actualizar_json("vajillas.json", data)
    messagebox.showinfo("Vajilla agregada",
                        f"Se agrego la vajilla {data['nombre']}", parent=frame)
    var.set("")
