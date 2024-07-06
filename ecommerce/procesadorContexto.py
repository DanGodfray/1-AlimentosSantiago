from .carro import Carro

#se crea un contexto para el carro de compras
def carro(request):
    
    #se retorna el carro de compras
    return {'carro': Carro(request)}