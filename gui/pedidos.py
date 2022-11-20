from modules.init import *
from tkcalendar import Calendar


def pedidos():
    top_pedidos = Toplevel()
    top_pedidos.title("Casa Fernandez - Pedidos")
    top_pedidos.config(width=800, height=800)
    top_pedidos.resizable(0, 0)

    frame_titulo = Frame(top_pedidos)
    frame_titulo.grid(column=1, row=0)
    Label(frame_titulo, text="Casa Fernandez",
          font=("Helvetica", 34, "bold")).grid(column=1, row=0)
    Label(frame_titulo, text="Alquiler de vajillas",
          font=("Helvetica", 15, "italic")).grid(column=1, row=1)

    mostrar_hora(tk.Label(frame_titulo, font=("Helvetica", 14)), 1, 2)

    def insertar_clientes(cliente, top):
        Label(top, text="\n Cliente" + "\n" + cliente['nombre'] + " " + cliente['apellido'] + "\n" + cliente['direccion'], font=(
            "Helvetica", 14)).grid(column=1, row=3, )

    def registrar_pedido(id, cliente, top, var):
        if var == "Ingrese el DNI de un cliente" or not agregar_vajillas(tuple(map(lambda item: str(int(item) + 1), id)), conseguir_vajillas()):

            messagebox.showerror(
                "Error", "Se ha producido un error", parent=top)
        else:
            top_registrar = Toplevel()
            top_registrar.title("Registrar pedido")
            top_registrar.config(width=800, height=800)
            top_registrar.resizable(0, 0)

            Label(top_registrar, text="Vajillas seleccionadas",
                  font=("Helvetica", 14)).grid(column=0, row=0, padx=20, pady=30)
            tv_selec = ttk.Treeview(top_registrar, height=13)
            tv_selec.grid(column=0, row=1, padx=30, pady=30)
            tv_selec["columns"] = ("Id", "Nombre")
            tv_selec.column("#0", stretch=NO, width=0)
            tv_selec.column("Nombre", width=200, anchor=N)
            tv_selec.column("Id", width=50, anchor=N)
            tv_selec.heading("#0")
            tv_selec.heading("Id", text="Id")
            tv_selec.heading("Nombre", text="Nombre")
            frame_calendar = Frame(top_registrar)
            frame_calendar.grid(column=1, row=1, padx=30)
            Label(frame_calendar, text="Fecha de entrega",
                  font=("Helvetica", 14)).grid(column=1, row=1)
            cal = Calendar(frame_calendar, selectmode='day',
                           year=2022, month=11,
                           day=24, date_pattern='dd/MM/yyyy')
            cal.grid(column=1, row=2, pady=15)
            Label(top_registrar, text=conseguir_fecha(),
                  font=("Helvetica", 14)).grid(column=1, row=0, padx=20, pady=30)
            Label(top_registrar, text="Cliente",
                  font=("Helvetica", 14)).grid(column=1, row=2, padx=20, pady=30)

            insertar_clientes(conseguir_un_cliente(cliente), frame_calendar)
            insertar_vajillas(agregar_vajillas(
                tuple(map(lambda item: str(int(item) + 1), id)), conseguir_vajillas()), tv_selec)

            trabajadores_var = StringVar()
            trabajadores_var.set("Seleccione un empleado")
            trabajadores = OptionMenu(
                top_registrar, trabajadores_var, *conseguir_nombres_empleados())
            menu = top_pedidos.nametowidget(trabajadores.menuname)
            menu.config(font=("Helvetica", 14))
            trabajadores.config(font=("Helvetica", 14))
            trabajadores.grid(column=0, row=2, padx=30, pady=30)

            Button(top_registrar, text="Confirmar pedido", font=("Helvetica", 14), command=lambda: confirmar_pedido(
                top_registrar, agregar_vajillas(tuple(map(lambda item: str(int(item) + 1), id)), conseguir_vajillas()), conseguir_un_cliente(cliente), trabajadores_var.get(), conseguir_fecha(), cal.get_date()), fg="green").grid(column=1, row=2, padx=30, pady=30)

            top_registrar.mainloop()

    def confirmar_pedido(top, vajillas, cliente, trabajador, fecha, fecha_entrega):
        actualizar_json("pedidos.json", {
            "id": conseguir_ultima_id(conseguir_pedidos()) + 1,
            "vajilla": vajillas,
            "nombre": cliente['nombre'],
            "apellido": cliente['apellido'],
            "direccion": cliente['direccion'],
            "dni": cliente['dni'],
            "telefono": cliente['telefono'],
            "trabajador": trabajador,
            "fecha": fecha,
            "fecha_entrega": fecha_entrega,
            "entregado": False},
        )
        messagebox.showinfo("Pedido registrado",
                            "Registraste el pedido", parent=top)
        vaciar_selecciones(tv_vajillas, tv_vajillas.selection())
        tv_pedidos.delete(*tv_pedidos.get_children())
        insertar_pedidos(conseguir_pedidos(), tv_pedidos)
        top.destroy()

    """
    Creando el treeview de las vajillas
    """

    vajilla_frame = Frame(top_pedidos)
    vajilla_frame.grid(column=0, row=1)
    Label(vajilla_frame, text="Vajillas",
          font=("Helvetica", 16, "bold")).grid(column=0, row=1, pady=5)

    tv_vajillas = ttk.Treeview(vajilla_frame, height=12)
    tv_vajillas.grid(column=0, row=2,   padx=30, columnspan=1)
    tv_vajillas["columns"] = ("Id", "Nombre")
    tv_vajillas.column("#0", stretch=NO, width=0)
    tv_vajillas.column("Nombre", width=350, anchor=N)
    tv_vajillas.column("Id", width=50, anchor=N)
    tv_vajillas.heading("#0")
    tv_vajillas.heading("Nombre", text="Nombre")
    tv_vajillas.heading("Id", text="ID")
    insertar_vajillas(conseguir_vajillas(), tv_vajillas)

    """
    Creacion de el OptionMenu para seleccionar un cliente
    """

    cliente_frame = Frame(top_pedidos)
    cliente_frame.grid(row=0, column=0, pady=30)
    Label(cliente_frame, text="Buscar cliente por DNI",
          font=("Helvetica", 16, "bold")).grid(column=0, row=0)
    dni_var = StringVar()
    nombre_e = Entry(cliente_frame, textvariable=dni_var,
                     width=15, font=("Helvetica", 14))
    nombre_e.bind('<Return>', lambda x: conseguir_un_cliente_dni(
        clientes, cliente_var, dni_var.get()))
    nombre_e.grid(column=0, row=2, pady=10)

    cliente_var = StringVar()
    cliente_var.set("Ingrese el DNI de un cliente")
    clientes = OptionMenu(cliente_frame, cliente_var, *[
        "Ingrese el DNI de un cliente"])
    menu = top_pedidos.nametowidget(clientes.menuname)
    menu.config(font=("Helvetica", 14))

    clientes.config(font=("Helvetica", 14))
    clientes.grid(column=0, row=1)

    """
    Treeview para los pedidos
    """

    def doble_click(event):
        ampliar_pedido(conseguir_un_pedido(
            tv_pedidos.item(tv_pedidos.selection())['values'][0]), tv_pedidos)

    pedidos_frame = Frame(top_pedidos)
    pedidos_frame.grid(column=1, row=1)
    Label(pedidos_frame, text="Pedidos",
          font=("Helvetica", 16, "bold")).grid(column=1, row=1, pady=5)
    tv_pedidos = ttk.Treeview(pedidos_frame, height=12, selectmode="browse")
    tv_pedidos.tag_configure('entregado', background='#D3D3D3')

    tv_pedidos.bind('<Double-Button-1>', doble_click)
    tv_pedidos.grid(column=1, row=2, padx=(50, 30), sticky=N)
    tv_pedidos["columns"] = ("ID", "DNI", "Fecha de Entrega", "Entregado")
    tv_pedidos.column("#0", stretch=NO, width=0)
    tv_pedidos.column("ID", width=50, anchor=N)
    tv_pedidos.column("DNI", width=100, anchor=N)
    tv_pedidos.column("Fecha de Entrega", width=150, anchor=N)
    tv_pedidos.column("Entregado", width=100, anchor=N)
    tv_pedidos.heading("#0")
    tv_pedidos.heading("ID", text="ID")
    tv_pedidos.heading("DNI", text="DNI")
    tv_pedidos.heading("Fecha de Entrega", text="Fecha de Entrega")
    tv_pedidos.heading("Entregado", text="Entregado")

    insertar_pedidos(conseguir_pedidos(), tv_pedidos)
    frame_cmd = LabelFrame(top_pedidos, text="Comandos",
                           font=("Helvetica", 16, "bold"), padx=10, pady=10)
    frame_cmd.grid(column=0, row=2, columnspan=4, padx=15, pady=20)

    Button(frame_cmd, text="Registrar pedido", command=lambda: registrar_pedido(
        tv_vajillas.selection(), dni_var.get(), top_pedidos, cliente_var.get()), font=("Helvetica", 14), fg="green").grid(column=0, row=2, padx=7, pady=(0, 10))
    Button(frame_cmd, text="Limpiar selección", command=lambda: vaciar_selecciones(tv_vajillas,
                                                                                   tv_vajillas.selection()), font=("Helvetica", 14)).grid(column=1, row=2, padx=7, pady=(0, 10))

    Button(frame_cmd, text="Ordenar pedidos", command=lambda: insertar_pedidos(ordenar_fechas_pedidos(conseguir_pedidos_tv(
        tv_pedidos.get_children(), tv_pedidos), tv_pedidos), tv_pedidos),
        font=("Helvetica", 14)).grid(column=2, row=2,  padx=7, pady=(0, 10))

    Button(frame_cmd, text="Filtrar entregados", command=lambda: insertar_pedidos(filtrar_entregados(conseguir_pedidos()), tv_pedidos, 0, True),
           font=("Helvetica", 14)).grid(column=0, row=3,   padx=7, pady=(0, 10), columnspan=3)

    Button(frame_cmd, text="Filtrar no entregados", command=lambda: insertar_pedidos(filtrar_no_entregados(conseguir_pedidos()), tv_pedidos, 0, True),
           font=("Helvetica", 14)).grid(column=2, row=3, padx=7, pady=(0, 10), columnspan=2)

    Button(frame_cmd, text="Restaurar", command=lambda: insertar_pedidos(conseguir_pedidos(), tv_pedidos, 0, True),
           font=("Helvetica", 14)).grid(column=3, row=2,  ipadx=20, padx=7, pady=(0, 10))

    Button(frame_cmd, text="Salir", command=lambda: top_pedidos.destroy(),
           font=("Helvetica", 14), fg="red").grid(column=4, row=2,  ipadx=30, padx=7, pady=(0, 10))


def ampliar_pedido(pedido, tv_pedidos):
    top = Toplevel()
    top.title(f"Ampliar pedido {pedido.get('id')}")
    top.resizable(0, 0)
    frame = Frame(top)
    frame.grid(column=0, row=0, padx=30, pady=30)
    Label(frame, text="Vajillas pedidas",
          font=("Helvetica", 16, "bold")).grid(column=0, row=0, pady=5)
    tv = ttk.Treeview(frame, height=12,
                      selectmode="none")
    tv.grid(column=0, row=1, padx=30, sticky=N, pady=20)
    tv["columns"] = ("ID", "Nombre")
    tv.column("#0", stretch=NO, width=0)
    tv.column("ID", width=50, anchor=N)
    tv.column("Nombre", width=200, anchor=N)
    tv.heading("#0")
    tv.heading("ID", text="ID")
    tv.heading("Nombre", text="Nombre")
    insertar_vajillas(pedido.get('vajilla'), tv)

    Label(frame, text=pedido.get('fecha'),
          font=("Helvetica", 16, "bold")).grid(column=2, row=0, padx=30)

    Label(frame, text=f"Cliente\n{pedido.get('nombre')} {pedido.get('apellido')}\n{pedido.get('direccion')}\n{pedido.get('dni')}\n{pedido.get('telefono')}\n\nTrabajador: {pedido.get('trabajador')}",
          font=("Helvetica", 16, "bold")).grid(column=2, row=1, padx=30)

    Button(frame, text={True: "Desmarcar entrega", False: "Registrar entrega"}[pedido.get('entregado')], command=lambda: registrar_entrega(pedido.get('id'), tv_pedidos, top),
           font=("Helvetica", 14), fg={True: "red", False: "blue"}[pedido.get('entregado')]).grid(column=0, row=3, pady=20)

    Label(frame, text=f"Fecha de entrega\n{pedido.get('fecha_entrega')}",
          font=("Helvetica", 16, "bold")).grid(column=0, row=2, )

    Button(frame, text="Salir", command=lambda: top.destroy(),
           font=("Helvetica", 14), fg="red").grid(column=2, row=3, ipadx=50)
    top.mainloop()
