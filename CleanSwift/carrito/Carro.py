from decimal import Decimal

class Carro:
    def __init__(self, request):
        self.session = request.session
        carro = self.session.get('session_key')

        if 'session_key' not in request.session:
            carro = self.session['session_key'] = {}

        self.carro = carro

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            self.carro[producto_id]['cantidad'] += 1
        else:
            self.carro[producto_id] = {
                'titulo': producto.titulo,
                'marca': producto.marca.nombre,
                'precio': float(producto.precio),  # Convertir Decimal a float
                'cantidad': 1,
            }
        self.session.modified = True

    def disminuir(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            if self.carro[producto_id]['cantidad'] > 0:
                self.carro[producto_id]['cantidad'] -= 1
            if self.carro[producto_id]['cantidad'] == 0:
                self.borrar(producto_id)
        self.session.modified = True

    def limpiar(self):
        self.carro = self.session['session_key'] = {}
        self.session.modified = True

    def borrar(self, producto_id):
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.session.modified = True

    def __str__(self):
        return f'El carro del usuario tiene {self.carro}'

    def __len__(self):
        cantidad = sum(item['cantidad'] for item in self.carro.values())
        return cantidad
