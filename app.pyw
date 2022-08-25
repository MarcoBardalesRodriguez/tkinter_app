from glob import glob
from tkinter import *
from tkinter.filedialog import *
import pyautogui as ag
import pygetwindow as gw
import time


def crear_botones():
    global btn_salir
    global btn_limpiar
    global btn_calcular
    global btn_imprimir

    btn_salir = Button(root, text="Salir", bg="#ff5555", fg="#ffffff", width=12)
    btn_salir.config(command=cerrar_ventana)
    btn_limpiar = Button(root, text="Limpiar", bg="#ecc406", fg="#ffffff", width=12)
    btn_limpiar.config(command=limpiar_pantalla)
    btn_calcular = Button(root, text="Calcular", bg="#55cc55", fg="#ffffff", width=12)
    btn_calcular.config(command=calcular_precios)
    btn_imprimir = Button(root, text="Imprimir", bg="#55cc55", fg="#ffffff", width=12)
    btn_imprimir.config(command=tomar_captura)


    btn_salir.grid(row=10, column=1, padx=10, pady=20)
    btn_limpiar.grid(row=10, column=2, padx=10, pady=20)
    btn_calcular.grid(row=10, column=3, padx=10, pady=20)
    btn_imprimir.grid(row=10, column=6, padx=10, pady=20)


def destruir_botones():
    btn_salir.destroy()
    btn_limpiar.destroy()
    btn_calcular.destroy()
    btn_imprimir.destroy()


def limpiar_pantalla():
    txt_dni.delete(0, "end")
    txt_apellidos.delete(0, "end")
    txt_nombres.delete(0, "end")
    txt_direccion.delete(0, "end")
    txt_telefono.delete(0, "end")
    txt_cod_1.delete(0, "end")
    txt_cod_2.delete(0, "end")
    txt_cod_3.delete(0, "end")
    txt_cant_1.delete(0, "end")
    txt_cant_2.delete(0, "end")
    txt_cant_3.delete(0, "end")

    subtotal_1.set("")
    subtotal_2.set("")
    subtotal_3.set("")
    total.set("")


def obtener_datos():
    datos = {}

    datos['producto_cant_1'] = txt_cant_1.get()
    datos['producto_cant_2'] = txt_cant_2.get()
    datos['producto_cant_3'] = txt_cant_3.get()

    datos['producto_precio_1'] = txt_precio_1.get()
    datos['producto_precio_2'] = txt_precio_2.get()
    datos['producto_precio_3'] = txt_precio_3.get()

    datos['producto_total'] = txt_total.get()

    return datos


def calcular_precios():

    datos = obtener_datos()

    cantidad_1 = float(datos['producto_cant_1'])
    cantidad_2 = float(datos['producto_cant_2'])
    cantidad_3 = float(datos['producto_cant_3'])

    precio_1 = float(datos['producto_precio_1'])
    precio_2 = float(datos['producto_precio_2'])
    precio_3 = float(datos['producto_precio_3'])

    costo_1 = cantidad_1 * precio_1
    costo_2 = cantidad_2 * precio_2
    costo_3 = cantidad_3 * precio_3

    costo_total = costo_1 + costo_2 + costo_3
    costo_total = costo_total + (costo_total * 0.18)
    

    subtotal_1.set(str(costo_1))
    subtotal_2.set(str(costo_2))
    subtotal_3.set(str(costo_3))
    total.set(str(costo_total))


def obtener_posicion():
    # print(gw.getAllTitles())

    sistema_venta = gw.getWindowsWithTitle('Sistema de Venta')[0]

    pad_left = sistema_venta.left
    pad_top = sistema_venta.top
    ancho = sistema_venta.width
    alto = sistema_venta.height

    #recortar la posicion a capturar
    pad_left = pad_left + 15
    pad_top = pad_top + 35
    ancho = ancho - 30
    alto = alto - 80
    
    posicion = (pad_left, pad_top, ancho, alto)

    return posicion


def tomar_captura():

    destruir_botones()
    
    time.sleep(1)

    captura = ag.screenshot('imagen.png', region=obtener_posicion())
    ruta = asksaveasfilename()
    captura.save(ruta+"_sistema_ventas.png")

    time.sleep(1)

    crear_botones()


def cerrar_ventana():
    root.destroy()



###   INICIO DE LA INTERFAZ   ###


root = Tk()
root.title("Sistema de Venta")

ancho_ventana = 1000
alto_ventana = 450
x_ventana = root.winfo_screenwidth()  //  2 - ancho_ventana  // 2
y_ventana = root.winfo_screenheight()  //  2 - alto_ventana  // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

root.geometry(posicion)
root.resizable(False, False)


title = Label(root, text="Ferreteria el Tornillo Feliz", fg="#ff0000", font="Times 18")
title.grid(row=0, column=0, columnspan=7, pady=15, sticky="we")



# Labels
root.option_add("*Font", "Times 12")

lbl_dni = Label(root, text="DNI", fg="#000000")
lbl_apellidos = Label(root, text="Apellidos", fg="#000000")
lbl_nombres = Label(root, text="Nombres", fg="#000000")
lbl_direccion = Label(root, text="Direccion", fg="#000000")
lbl_telefono = Label(root, text="Telefono", fg="#000000")

lbl_dni.grid(row=1, column=0, sticky="w", padx=10)
lbl_apellidos.grid(row=2, column=0, sticky="w", padx=10)
lbl_nombres.grid(row=2, column=3, sticky="e", padx=10)
lbl_direccion.grid(row=3, column=0, sticky="w", padx=10)
lbl_telefono.grid(row=4, column=0, sticky="w", padx=10)

# Entrys

txt_dni = Entry(root, fg="#000000")
txt_apellidos = Entry(root, fg="#000000")
txt_nombres = Entry(root, fg="#000000")
txt_direccion = Entry(root, fg="#000000")
txt_telefono = Entry(root, fg="#000000")

txt_dni.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)
txt_apellidos.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
txt_nombres.grid(row=2, column=4, columnspan=3, sticky="ew", pady=5)
txt_direccion.grid(row=3, column=1, columnspan=6, sticky="ew", pady=5)
txt_telefono.grid(row=4, column=1, columnspan=6, sticky="ew", pady=5)


# Labels

lbl_cod_producto = Label(root, text="Cod Produc.", fg="#000000")
lbl_descripcion = Label(root, text="Descripcion", fg="#000000")
lbl_unidad = Label(root, text="Unidad", fg="#000000")
lbl_cantidad = Label(root, text="Cantidad", fg="#000000")
lbl_precio = Label(root, text="Precio", fg="#000000")
lbl_subtotal = Label(root, text="Sub Total", fg="#000000")
lbl_total = Label(root, text="Total + IGV", fg="#000000")

lbl_cod_producto.grid(row=5, column=0, sticky="we", padx=10, pady=15)
lbl_descripcion.grid(row=5, column=1, sticky="we", padx=10, pady=15)
lbl_unidad.grid(row=5, column=2, sticky="we", padx=10, pady=15)
lbl_cantidad.grid(row=5, column=3, sticky="we", padx=10, pady=15)
lbl_precio.grid(row=5, column=4, sticky="we", padx=10, pady=15)
lbl_subtotal.grid(row=5, column=5, sticky="we", padx=10, pady=15)
lbl_total.grid(row=9, column=6, sticky="we", padx=10, pady=15)



# Non ReadOnly entrys

txt_cod_1 = Entry(root, fg="#000000", width=10)
txt_cod_2 = Entry(root, fg="#000000", width=10)
txt_cod_3 = Entry(root, fg="#000000", width=10)
txt_cant_1 = Entry(root, fg="#000000", width=15)
txt_cant_2 = Entry(root, fg="#000000", width=15)
txt_cant_3 = Entry(root, fg="#000000", width=15)

txt_cod_1.grid(row=6, column=0, padx=10)
txt_cod_2.grid(row=7, column=0, padx=10, pady=10)
txt_cod_3.grid(row=8, column=0, padx=10)
txt_cant_1.grid(row=6, column=3, padx=10)
txt_cant_2.grid(row=7, column=3, padx=10, pady=10)
txt_cant_3.grid(row=8, column=3, padx=10)

# ReadOnly entrys

descripcion_1 = StringVar()
descripcion_1.set("Tornillos 4x50mm")
descripcion_2 = StringVar()
descripcion_2.set("Tarugos PVC")
descripcion_3 = StringVar()
descripcion_3.set("Tarugos de Nylon")

txt_descripcion_1 = Entry(root,textvariable=descripcion_1, state=DISABLED)
txt_descripcion_1.grid(row=6, column=1, padx=10)
txt_descripcion_2 = Entry(root,textvariable=descripcion_2, state=DISABLED)
txt_descripcion_2.grid(row=7, column=1, padx=10, pady=10)
txt_descripcion_3 = Entry(root,textvariable=descripcion_3, state=DISABLED)
txt_descripcion_3.grid(row=8, column=1, padx=10)

unidad_1 = StringVar()
unidad_1.set("Caja x500 unidades")
unidad_2 = StringVar()
unidad_2.set("Caja x100 unidades")
unidad_3 = StringVar()
unidad_3.set("Caja x100 unidades")

txt_unidad_1 = Entry(textvariable=unidad_1, state=DISABLED)
txt_unidad_1.grid(row=6, column=2, padx=10)
txt_unidad_2 = Entry(textvariable=unidad_2, state=DISABLED)
txt_unidad_2.grid(row=7, column=2, padx=10, pady=10)
txt_unidad_3 = Entry(textvariable=unidad_3, state=DISABLED)
txt_unidad_3.grid(row=8, column=2, padx=10)

precio_1 = StringVar()
precio_1.set("81.90")
precio_2 = StringVar()
precio_2.set("8.20")
precio_3 = StringVar()
precio_3.set("24.90")

txt_precio_1 = Entry(textvariable=precio_1, state=DISABLED, width=10)
txt_precio_1.grid(row=6, column=4, padx=10)
txt_precio_2 = Entry(textvariable=precio_2, state=DISABLED, width=10)
txt_precio_2.grid(row=7, column=4, padx=10, pady=10)
txt_precio_3 = Entry(textvariable=precio_3, state=DISABLED, width=10)
txt_precio_3.grid(row=8, column=4, padx=10)

subtotal_1 = StringVar()
subtotal_1.set("")
subtotal_2 = StringVar()
subtotal_2.set("")
subtotal_3 = StringVar()
subtotal_3.set("")

txt_subtotal_1 = Entry(textvariable=subtotal_1, state=DISABLED, width=10)
txt_subtotal_1.grid(row=6, column=5, padx=10)
txt_subtotal_2 = Entry(textvariable=subtotal_2, state=DISABLED, width=10)
txt_subtotal_2.grid(row=7, column=5, padx=10, pady=10)
txt_subtotal_3 = Entry(textvariable=subtotal_3, state=DISABLED, width=10)
txt_subtotal_3.grid(row=8, column=5, padx=10)

total = StringVar()
total.set("")
txt_total = Entry(textvariable=total, state=DISABLED, width=10)
txt_total.grid(row=9, column=5, padx=10, pady=10)


# Buttons
crear_botones()


root.mainloop()