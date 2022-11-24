from modules.init import *

def clientes():
    top = Toplevel()
    top.title("Casa Fernandez - Clientes")
    top.config(width=300, height=300)
    top.resizable(0, 0)

    frame = LabelFrame(top, text="Registrar cliente",
                       font=("Helvetica", 16, "bold"), padx=20, pady=20)
    frame.grid(column=1, row=0, pady=(40, 15), padx=30)
    frame_tv = Frame(top)
    frame_tv.grid(column=0, row=0)
    Label(frame_tv, text="Clientes",
          font=("Helvetica", 16, "bold")).grid(column=0, row=1, pady=(0, 10))
    def doble_click(event):
        mostrar_pedido(list(filter(lambda pedido: pedido.get('dni') == str(tv.item(tv.selection())['values'][0]), conseguir_pedidos())), conseguir_un_cliente(str(tv.item(tv.selection())['values'][0])))

    tv = ttk.Treeview(frame_tv, height=13,
                      selectmode="browse")
    tv.grid(column=0, row=2, padx=30, sticky=N)
    tv["columns"] = ("DNI", "Nombre", "Apellido", "Teléfono")
    tv.bind('<Double-Button-1>', doble_click)
    tv.column("#0", stretch=NO, width=0)
    tv.column("DNI", width=150, anchor=N)
    tv.column("Nombre", width=100, anchor=N)
    tv.column("Apellido", width=100, anchor=N)
    tv.column("Teléfono", width=150, anchor=N)
    tv.heading("#0")
    tv.heading("DNI", text="DNI")
    tv.heading("Nombre", text="Nombre")
    tv.heading("Apellido", text="Apellido")
    tv.heading("Teléfono", text="Teléfono")
    insertar_clientes(conseguir_clientes(), tv)

    Label(frame, text="Nombre",
          font=("Helvetica", 14, "bold")).grid(column=1, row=0, pady=(10, 0))
    Label(frame, text="Apellido",
          font=("Helvetica", 14, "bold")).grid(column=2, row=0)
    Label(frame, text="Dirección",
          font=("Helvetica", 14, "bold")).grid(column=1, row=2)
    Label(frame, text="DNI",
          font=("Helvetica", 14, "bold")).grid(column=2, row=2)
    Label(frame, text="Telefono",
          font=("Helvetica", 14, "bold")).grid(column=1, row=4, columnspan=2)
    nombre_var = StringVar()
    apellido_var = StringVar()
    direccion_var = StringVar()
    dni_var = StringVar()
    telefono_var = StringVar()
    nombre_e = Entry(frame, textvariable=nombre_var,
                     width=15, font=("Helvetica", 14))
    nombre_e.grid(column=1, row=1, pady=(0, 20), padx=10)
    apellido_e = Entry(frame, textvariable=apellido_var,
                       width=15, font=("Helvetica", 14))
    apellido_e.grid(column=2, row=1, pady=(0, 20))
    direccion_e = Entry(frame, textvariable=direccion_var,
                        width=15, font=("Helvetica", 14))
    direccion_e.grid(column=1, row=3, pady=(0, 20))
    dni_e = Entry(frame, textvariable=dni_var,
                  width=15, font=("Helvetica", 14))
    dni_e.grid(column=2, row=3, pady=(0, 20))
    telefono_e = Entry(frame, textvariable=telefono_var,
                       width=15, font=("Helvetica", 14))
    telefono_e.grid(column=1, row=5, pady=(0, 20), columnspan=2)
    Button(frame, text="Agregar", command=lambda: agregar({
        "nombre": nombre_var.get(),
        "apellido": apellido_var.get(),
        "direccion": direccion_var.get(),
        "dni": dni_var.get(),
        "telefono": telefono_var.get()
    }, top, nombre_var, apellido_var, direccion_var, dni_var, telefono_var, tv), font=("Helvetica", 14), fg="green").grid(
        column=1, row=6, columnspan=2, ipadx=25)

    top.mainloop()

def mostrar_pedido(pedidos, cliente):
    top = Toplevel()
    top.title(f"Pedidos del cliente {cliente.get('nombre')} {cliente.get('apellido')}")
    frame = Frame(top)
    frame.grid(column=0, row=0, padx=20, pady=20)
    Label(frame, text=f"Pedidos del cliente {cliente.get('nombre')} {cliente.get('apellido')}",
          font=("Helvetica", 14, "bold")).grid(column=0, row=0, pady=(0, 5))
    tv = ttk.Treeview(frame, height=13,
                      selectmode="none")
    tv.grid(column=0, row=1,  sticky=N)
    tv.tag_configure('entregado', background='#D3D3D3')
    tv["columns"] = ("ID", "DNI","Fecha de entrega", "Total", "Entregado")
    tv.column("#0", stretch=NO, width=0)
    tv.column("ID", width=50, anchor=N)
    tv.column("DNI", width=100, anchor=N)
    tv.column("Fecha de entrega", width=150, anchor=N)
    tv.column("Total", width=100, anchor=N)
    tv.column("Entregado", width=100, anchor=N)
    tv.heading("#0")
    tv.heading("ID", text="ID")
    tv.heading("DNI", text="DNI")
    tv.heading("Fecha de entrega", text="Fecha de entrega")
    tv.heading("Total", text="Total")
    tv.heading("Entregado", text="Entregado")
    insertar_pedidos(pedidos, tv)

    if pedidos:
        Label(frame, text=f"Pedidos totales: {len(pedidos)}\nMonto total: ${obtener_monto_total(pedidos)}\nMayor monto de un pedido: ${obtener_mayor_monto(pedidos)}\n\nFecha ultimo pedido: {ultimo_pedido(pedidos).get('fecha')}\nFecha de entrega del ultimo pedido: {ultimo_pedido(pedidos).get('fecha_entrega')}\nMonto del ultimo pedido: ${ultimo_pedido(pedidos).get('total')}\n\nFecha primer pedido: {primer_pedido(pedidos).get('fecha')}\nFecha de entrega del primer pedido: {primer_pedido(pedidos).get('fecha_entrega')}\nMonto del primer pedido: ${primer_pedido(pedidos).get('total')}",
            font=("Helvetica", 14, "bold")).grid(column=1, row=1, padx=(40, 0), pady=(0, 5), rowspan=2)
    else:
            Label(frame, text=f"No hay datos para mostrar",
          font=("Helvetica", 14, "bold")).grid(column=1, row=1, padx=(40, 0), rowspan=3)

    Button(frame, text="Salir", command=lambda: top.destroy(),
           font=("Helvetica", 14), fg="red").grid(column=1, row=3,  ipadx=59, padx=(40, 0))
    top.mainloop()

def agregar(data, frame, nombre_var, apellido_var, direccion_var, dni_var, telefono_var, tv):
    if not conseguir_un_cliente(data.get('dni')):
        rta = messagebox.askokcancel(
            "Agregar cliente", f"Se agregara el cliente cuyos datos son: \nNombre y apellido: {data.get('nombre')} {data.get('apellido')}\nDirección: {data.get('direccion')}\nDNI: {data.get('dni')}\nTeléfono: {data.get('telefono')}", parent=frame)
        if rta:
            actualizar_json("clientes.json", {
                "nombre": data.get('nombre'),
                "apellido": data.get('apellido'),
                "direccion": data.get('direccion'),
                "dni": data.get('dni'),
                "telefono": data.get('telefono')
            })
            messagebox.showinfo("Cliente agregado",
                                f"Se agrego el cliente {data.get('nombre')} {data.get('apellido')}", parent=frame)
            insertar_clientes(conseguir_clientes(), tv)
            nombre_var.set('')
            apellido_var.set('')
            direccion_var.set('')
            dni_var.set('')
    else:
        messagebox.showerror(
            "Error", "Error, el cliente ya existe", parent=frame)

def obtener_monto_total(pedidos, sum=0, i=0):
    if i == len(pedidos): return sum

    return obtener_monto_total(pedidos, sum + pedidos[i].get('total'), i + 1)

obtener_mayor_monto = lambda pedidos: max(pedidos, key=lambda pedido: pedido.get('total')).get('total')
primer_pedido = lambda pedidos: pedidos[0]
ultimo_pedido = lambda pedidos: pedidos[-1]