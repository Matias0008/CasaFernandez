import json
from tkinter import messagebox
from datetime import datetime
from time import *


def mostrar_hora(label, col, row):
    label.grid(column=col, row=row)
    label.config(text=strftime('%H:%M:%S %p'))
    label.after(1000, lambda: mostrar_hora(label, col, row))


def conseguir_pedidos():
    with open("assets/json/pedidos.json") as f:
        return json.load(f)


def conseguir_pedidos_tv(ids, tv):
    return list(filter(lambda pedido: pedido['id'] in mapear_ids(ids, tv, temp=[]), conseguir_pedidos()))


"""
Se recibe una tupla de IDS que corresponden a las posiciones del Treeview de Pedidos
El objetivo es mapear cada ID asociado al item del treeview, que una vez
mapeados corresponderan a los pedidos.
"""


def mapear_ids(ids, tv, temp=[], i=0):
    if i == len(ids):
        return tuple(map(lambda id: id, temp))

    temp.append(tv.item(ids[i])['values'][0])
    return mapear_ids(ids, tv, temp, i + 1)


def conseguir_un_pedido(id):
    return list(filter(lambda pedido: pedido.get('id') == id, conseguir_pedidos()))[0]


def ordenar_fechas_pedidos(pedidos, tv):
    pedidos.sort(key=lambda pedido: strptime(
        pedido['fecha_entrega'], '%d/%m/%Y'))

    tv.delete(*tv.get_children())
    return pedidos


def filtrar_entregados(pedidos):
    return list(filter(lambda pedido: pedido['entregado'], pedidos))


def filtrar_no_entregados(pedidos):
    return list(filter(lambda pedido: not pedido['entregado'], pedidos))


def insertar_pedidos(pedidos, tv,  i=0, limpiar_tv=False):
    if limpiar_tv:
<<<<<<< HEAD

=======
        print(tv.get_children(), *tv.get_children())
>>>>>>> 8cf9f9aba8a5c0ee1b89824360abb0d6923558b1
        tv.delete(*tv.get_children())

    if i == len(pedidos):
        return

    tv.insert("", 'end', id=i, values=(
        pedidos[i]['id'],
        pedidos[i]['dni'], pedidos[i]['fecha_entrega'], {True: "Si", False: "No"}[pedidos[i]['entregado']]), tags={True: "entregado", False: ""}[pedidos[i]['entregado']])

    return insertar_pedidos(pedidos, tv, i + 1)


"""
Funciones para trabajar con las vajillas
"""


def agregar_vajillas(id, vajillas):
    return list(filter(lambda vajilla: str(vajilla['id']) in id, vajillas))


def conseguir_vajillas():
    with open("assets/json/vajillas.json") as f:
        return json.load(f)


def insertar_vajillas(vajillas, tv, i=0):
    if i == len(vajillas):
        return

    tv.insert("", 'end', id=i, values=(
        vajillas[i]['id'], vajillas[i]['nombre'],))

    return insertar_vajillas(vajillas, tv, i + 1)


def conseguir_ultima_id(iterable):
    if list(filter(lambda item: item['id'], iterable)):
        return list(filter(lambda item: item['id'], iterable))[-1]['id']
    return 0


def conseguir_fecha():
    return datetime.now().strftime('%d/%m/%Y %H:%M')


"""
Funciones para trabajar con los clientes y trabajadores
"""


def conseguir_empleados():
    with open("assets/json/empleados.json") as f:
        return json.load(f)


def conseguir_un_empleado(nombre):
    return list(filter(lambda trabaj: trabaj['nombre'] == nombre, conseguir_empleados()))[0]


def conseguir_nombres_empleados():
    return list(map(lambda trabaj: trabaj['nombre'], conseguir_empleados()))


def conseguir_clientes():
    with open("assets/json/clientes.json") as f:
        return json.load(f)

def insertar_clientes(clientes, tv, i=0, limpiar_tv=False):
    if limpiar_tv:
        tv.delete(*tv.get_children())
    if i == len(clientes):
        return

    tv.insert("", 'end', id=i, values=(
        clientes[i]['dni'], clientes[i]['nombre'], clientes[i]['apellido'], clientes[i]['telefono']))

    return insertar_clientes(clientes, tv, i + 1)

def insertar_clientes(clientes, tv, i=0, limpiar_tv=False):
    if limpiar_tv:
        tv.delete(*tv.get_children())
    if i == len(clientes):
        return

    tv.insert("", 'end', id=i, values=(
        clientes[i]['dni'], clientes[i]['nombre'], clientes[i]['apellido'], clientes[i]['telefono']))

    return insertar_clientes(clientes, tv, i + 1)


def conseguir_un_cliente(dni):
    if list(filter(lambda cliente: cliente['dni'] == dni, conseguir_clientes())):
        return list(filter(lambda cliente: cliente['dni'] == dni, conseguir_clientes()))[0]
    return []


def conseguir_un_cliente_dni(optionmenu, var, dni):
    optionmenu['menu'].delete(0, 'end')

    if list(filter(lambda cliente: cliente['dni'] == dni, conseguir_clientes())):
        var.set(conseguir_un_cliente(dni)[
                'nombre'] + " " + conseguir_un_cliente(dni)['apellido'])
    else:
        var.set("Ingrese el DNI de un cliente")


def vaciar_selecciones(tv, selecciones, i=0):
    if i == len(selecciones):
        return

    tv.selection_remove(selecciones[i])
    return vaciar_selecciones(tv, selecciones, i + 1)


def actualizar_json(filename, entry):
    with open(f"assets/json/{filename}", "r") as file:
        data = json.load(file)

    data.append(entry)

    with open(f"assets/json/{filename}", "w") as file:
        json.dump(data, file, indent=4)


def reemplazar_json(filename, data):
    with open(f"assets/json/{filename}", "w") as file:
        json.dump(data, file, indent=4)


def conseguir_indice_true(lista, i=0):
    if lista[i]:
        return i

    if i == len(lista):
        return -1

    return conseguir_indice_true(lista, i + 1)


def registrar_entrega(id, tv, frame):
    with open(f"assets/json/pedidos.json", "r") as file:
        data = json.load(file)
        if messagebox.askyesno({False: "Registrar la entrega", True: "Desmarcar la entrega"}[data[(conseguir_indice_true(list(map(lambda item: item['id'] == id, data))))]['entregado']], {
                False: "Esta seguro de registrar la entrega?", True: "Esta seguro de desmarcar la entrega?"}[data[(conseguir_indice_true(list(map(lambda item: item['id'] == id, data))))]['entregado']], parent=frame):

            data[(conseguir_indice_true(list(map(lambda item: item['id'] == id, data))))]['entregado'] = not data[(conseguir_indice_true(
                list(map(lambda item: item['id'] == id, data))))]['entregado']
            reemplazar_json("pedidos.json", data)
            insertar_pedidos(data, tv, limpiar_tv=True)
            frame.destroy()
