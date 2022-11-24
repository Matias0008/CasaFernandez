from modules.init import *
from gui.clientes import clientes
from gui.empleados import empleados
from gui.pedidos import pedidos
from gui.vajillas import vajillas


root = Tk()
root.config(width=500, height=500)
root.resizable(0, 0)
root.title("Casa Fernandez")
style = ttk.Style()
style.configure("Treeview", rowheight=22,)
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.configure("Treeview", font=("Helvetica", 12))
image = Image.open("assets/logo.png")
image = image.resize((250, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

frame = Frame(root)
frame.grid(column=0, row=0, padx=50, pady=50)
label_image = Label(frame, image=img)
label_image.grid(column=0, row=1, columnspan=3)

Label(frame, text="Casa Fernandez",
      font=("Helvetica", 38, "bold")).grid(column=0, row=2, columnspan=3, pady=(20, 0))
mostrar_hora(tk.Label(frame, font=("Helvetica", 16)), 0, 3, columnspan=3, pady=(0, 20))

Button(frame, text="Pedidos", command=lambda: pedidos(), font=("Helvetica", 14)).grid(
    column=0, row=4)
Button(frame, text="Empleados", command=lambda: empleados(), font=("Helvetica", 14)).grid(
    column=1, row=4)
Button(frame, text="Clientes", command=lambda: clientes(), font=("Helvetica", 14)).grid(
    column=2, row=4)
Button(frame, text="Vajillas", command=lambda: vajillas(), font=("Helvetica", 14)).grid(
    column=1, row=5, pady=20, ipadx=17)
Button(frame, text="Salir", command=lambda: root.destroy(),
           font=("Helvetica", 14), fg="white", bg="red").grid(column=1, row=6,  ipadx=60, pady=(10, 0))



root.mainloop()
