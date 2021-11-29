""" Primero se piden los valores necesarios para realizar la
compra y para el rol, la cantidad y el precio, que son 
valores fundamentales para que el código funcione se les 
raliza un try except para evitar errores por un valor inesperado
"""
def pedir_datos():
    cedula = input("Número de cédula: ")
    valor_rol = False
    valor_cantidad = False
    valor_precio = False
    while valor_rol == False:
        try:
            rol = int(input("Rol, escriba 1 si es profesor o 2 si es estudiante: "))
            if rol == 1 or rol == 2:
                valor_rol = True
            else:
                ("El número que ingresó no es valido")
        except:
            print("Lo que ingreso no es valido")
    codigo = input("Código del producto: ")
    while valor_cantidad == False:
        try:
            cantidad = int(input("Número de unidades: "))
            valor_cantidad = True
        except ValueError:
            print("Lo que ingresó no es valido")
    while valor_precio == False:
        try:
            precio = float(input("Precio (Sin puntos ni comas) : "))
            valor_precio = True
        except ValueError:
            print("Lo que ingresó no es valido")
    return(cedula, rol, codigo, cantidad, precio)
"""Se realizan los calculos necesarios para obtener el 
precio total incluyendo el desuento dependiendo si es profesor 
o estudiante
"""
def calcular_valor_a_pagar(cedula, rol, codigo, cantidad, precio):
    precio_total = cantidad * precio
    if rol == 1:
        precio_descuento = precio_total * 0.8
        print("El profesor con cédula", cedula, "debe pagar",
            precio_descuento, "por el producto", codigo)
    elif rol == 2:
        precio_descuento = precio_total * 0.5
        print("El estudiante con cédula", cedula, "debe pagar",
            precio_descuento, "por el producto", codigo)
""" Mientras continuar sea igual a 1 se va a seguir haciendo todo el proceso
para calcular el valor a pagar a nuevas personas, hasta que el usuario ingrese
el número 2
"""
continuar = 1
while continuar == 1:
    [cedula, rol, codigo, cantidad, precio] = pedir_datos()
    calcular_valor_a_pagar(cedula, rol, codigo, cantidad, precio)
    continuar = int(input("Escriba 1 si agregar otro cliente, escriba 2 si desea terminar: "))
