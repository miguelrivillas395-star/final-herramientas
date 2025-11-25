class Producto:
    def __init__(self, nombre, precio, categoria, stock):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Nuevo stock de {self.nombre}: {self.stock}")

        # Objetos creados desde la clase Producto
producto1 = Producto("Taladro eléctrico", 250000, "Herramientas", 15)
producto2 = Producto("Sierra circular", 320000, "Herramientas", 10)
producto3 = Producto("Lijadora orbital", 180000, "Herramientas", 8)

# Mostrar atributos y métodos
producto1.mostrar_info()
producto2.mostrar_info()
producto3.mostrar_info()

producto1.actualizar_stock(5)
producto2.actualizar_stock(-2)

# Clase hija 1: ProductoVenta
class ProductoVenta(Producto):
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Descuento aplicado. Nuevo precio de {self.nombre}: ${self.precio}")

    def mostrar_precio_final(self, iva=19):
        total = self.precio * (1 + iva / 100)
        print(f"Precio final con IVA de {self.nombre}: ${total}")

# Clase hija 2: ProductoHerramienta
class ProductoHerramienta(Producto):
    def verificar_seguridad(self):
        print(f"{self.nombre} cumple con normas de seguridad industrial.")

    def mostrar_manual_uso(self):
        print(f"Manual de uso de {self.nombre}: Encender, ajustar velocidad, aplicar sobre superficie.")

        # Crear objetos heredados desde producto1
producto_venta = ProductoVenta("Taladro eléctrico", 250000, "Herramientas", 15)
producto_herramienta = ProductoHerramienta("Taladro eléctrico", 250000, "Herramientas", 15)

# Métodos únicos de cada clase hija
producto_venta.aplicar_descuento(10)
producto_venta.mostrar_precio_final()

producto_herramienta.verificar_seguridad()
producto_herramienta.mostrar_manual_uso()