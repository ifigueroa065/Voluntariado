class Subtotal():
    def __init__(self, id, codigo, nombre, entregado, subtotal):
        self.id=id
        self.nombre=nombre
        self.entregado=entregado
        self.codigo = codigo
        self.subtotal = subtotal
 
class Datos():
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Reporte():
    def __init__(self, codigo, nombre, entregado_usuario):
        self.codigo = codigo
        self.nombre = nombre
        self.entregado_usuario = entregado_usuario