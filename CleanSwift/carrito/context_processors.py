from .Carro import Carro

def carro(request):
    return {'carro': Carro(request)}