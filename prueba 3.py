import json

#VARIABLE PARA PIZZAS PRECIOS

precios_pizzas = {
    "cuatro quesos": {
        "Pequeña": 6000,
        "Mediana": 9000,
        "Familia": 12000
    },
    "hawaiana": {
        "Pequeña": 6000,
        "Mediana": 9000,
        "Familia": 12000
    },
    "napolitana": {
        "Pequeña": 5500,
        "Mediana": 8500,
        "Familia": 11000
    },
    "pepperoni": {
        "Pequeña": 7000,
        "Mediana": 10000,
        "Familia": 13000
    }
}
    
ventas = []

def registrar_ventas():
    print("Registros de nuevas ventas: ")
    cliente = input("Ingrese el nombre del cliente: ")
    tipo_pizza = input("Ingrese el tipo de pizza (Cuatro quesos, Hawaiana, Napolitana, Pepperoni): ").lower()
    tamaño = input("Ingrese el tamaño de la pizza(Pequeña, Mediana, Familiar): ").capitalize()
    cantidad = int(input("Ingrese la cantidad de pizzas vendidas: "))

#CALCULO DE PRECIOS
    precio_unitario = precios_pizzas[tipo_pizza][tamaño]
    precio_total = cantidad * precio_unitario

#DESCUENTO USUSARIOS

    tipo_usuario = input("Ingrese el tipo de usuario (Estudiante diurno, Estudiante vespertino, Administrativo): ").lower()
    descuento = 0
    if tipo_usuario == "estudiante diurno":
        descuento = 0.12
    elif tipo_usuario == "estudiante vespertino":
        descuento = 0.14
    elif tipo_usuario == "administrativo":
        descuento = 0.10
    
    precio_final = precio_total * (1 - descuento)

#GUARDADO DE VENTAS

    venta = {
        "cliente": cliente,
        "tipo_pizza": tipo_pizza,
        "tamaño": tamaño,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "precio_total": precio_total,
        "tipo_usuario": tipo_usuario,
        "descuento_aplicado": descuento,
        "precio_final": precio_final
    }
    ventas.append(venta)
    print("Venta registrada correctamente.")

##FUNCION PARA MOSTRAR LAS VENTAS

def mostrar_ventas():
    print("\nListado de todas las ventas:")
    for venta in ventas:
        print(f"Cliente: {venta['cliente']}, Pizza: {venta['tipo_pizza']} ({venta['tamaño']}), Cantidad: {venta['cantidad']}, Precio Total: ${venta['precio_total']:.2f}")

##BUSQUEDA POR CLIENTES

def buscar_por_cliente():
    cliente_buscar = input("Ingrese el nombre del cliente a buscar: ")
    print(f"\nVentas encontradas para '{cliente_buscar}':")
    encontradas = False
    for venta in ventas:
        if venta['cliente'].lower() == cliente_buscar.lower():
            encontradas = True
            print(f"Pizza: {venta['tipo_pizza']} ({venta['tamaño']}), Cantidad: {venta['cantidad']}, Precio Total: ${venta['precio_total']:.2f}")
    if not encontradas:
        print(f"No se encontraron ventas para '{cliente_buscar}'.")

##GUARDADO DE VENTAS

def guardar_ventas():
    with open("ventas.json", "w") as file:
        json.dump(ventas, file)
    print("Ventas guardadas en 'ventas.json'.")

##CARGAR VENTAS

def cargar_ventas():
    global ventas
    try:
        with open("ventas.json", "r") as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'. No hay ventas cargadas.")

##GENERADOR DE BOLETA

def generar_boleta():
    cliente = input("Ingrese el nombre del cliente para generar la boleta: ")
    encontrado = False
    for venta in ventas:
        if venta['cliente'].lower() == cliente.lower():
            encontrado = True
            print("\n======= Boleta =======")
            print(f"Cliente: {venta['cliente']}")
            print(f"Pizza: {venta['tipo_pizza']} ({venta['tamaño']})")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio Total: ${venta['precio_total']:.2f}")
            print(f"Descuento aplicado: {venta['descuento_aplicado']*100}%")
            print(f"Precio Final: ${venta['precio_final']:.2f}")
            print("======================")
    if not encontrado:
        print(f"No se encontraron ventas para '{cliente}'.")

##ANULAR LA VENTA

def anular_venta():
    cliente = input("Ingrese el nombre del cliente para eliminar la venta: ")
    encontrada = False
    for venta in ventas:
        if venta['cliente'].lower() == cliente.lower():
            encontrada = True
            confirmacion = input(f"¿Está seguro que desea eliminar la venta de {venta['tipo_pizza']} ({venta['tamaño']}) al cliente {cliente}? (s/n): ")
            if confirmacion.lower() == 's':
                ventas.remove(venta)
                print("Venta eliminada correctamente.")
                break
    if not encontrada:
        print(f"No se encontraron ventas para '{cliente}'.")

##MENU DE OPCIONES

def menu():
    while True:
        print("\n==== Sistema de Ventas de Pizzas - DUOC UC ====")
        print("1. Registrar una venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar ventas por cliente")
        print("4. Guardar las ventas en un archivo")
        print("5. Cargar las ventas desde un archivo")
        print("6. Generar Boleta")
        print("7. Anular venta")
        print("8. Salir del programa")

        opcion = input("\nIngrese la opción que desea realizar: ")

        if opcion == '1':
            registrar_ventas()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            buscar_por_cliente()
        elif opcion == '4':
            guardar_ventas()
        elif opcion == '5':
            cargar_ventas()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            anular_venta()
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")

if __name__ == "__main__":
    menu()





