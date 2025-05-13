from datetime import datetime


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self, id: int, fecha: datetime):
        self.id = id
        self.fecha = fecha
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)


class Cliente:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email
        self.pedidos = []
        self.pagos = []

    def realizar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def realizar_pago(self, pago: 'Pago'):
        self.pagos.append(pago)


class Pago:
    def __init__(self, id: int, cantidad: float, metodo: str):
        self.id = id
        self.cantidad = cantidad
        self.metodo = metodo

    def procesar_pago(self):
        print(f"Procesando pago de {self.cantidad} usando el método: {self.metodo}")


if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Bicicleta", 150.0)
    producto2 = Producto("Casco", 25.0)

    # Crear un pedido
    pedido1 = Pedido(1, datetime.now())
    pedido1.agregar_producto(producto1)
    pedido1.agregar_producto(producto2)

    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", "juan@email.com")
    cliente1.realizar_pedido(pedido1)

    # Realizar un pago
    pago1 = Pago(1, 175.0, "Tarjeta de Crédito")
    cliente1.realizar_pago(pago1)
    pago1.procesar_pago()

    # Mostrar detalles del cliente, pedidos y productos
    print(f"Cliente: {cliente1.nombre}, Email: {cliente1.email}")
    for pedido in cliente1.pedidos:
        print(f"Pedido ID: {pedido.id}, Fecha: {pedido.fecha}")
        for producto in pedido.productos:
            print(f"- Producto: {producto.nombre}, Precio: {producto.precio}")
    
    # Mostrar pagos realizados
    for pago in cliente1.pagos:
        print(f"Pago ID: {pago.id}, Monto: {pago.cantidad}, Método: {pago.metodo}")
