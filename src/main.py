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

    def realizar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)


if __name__ == "__main__":
    producto1 = Producto("Bicicleta", 150.0)
    producto2 = Producto("Casco", 25.0)
    
    pedido1 = Pedido(1, datetime.now())
    pedido1.agregar_producto(producto1)
    pedido1.agregar_producto(producto2)

    cliente1 = Cliente("Juan Pérez", "juan@email.com")
    cliente1.realizar_pedido(pedido1)

    print(f"Cliente: {cliente1.nombre}, Email: {cliente1.email}")
    for pedido in cliente1.pedidos:
        print(f"Pedido ID: {pedido.id}, Fecha: {pedido.fecha}")
        for producto in pedido.productos:
            print(f"- Producto: {producto.nombre}, Precio: {producto.precio}")
