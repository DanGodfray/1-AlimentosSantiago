class Carro():
    def __init__(self, request):
        self.session = request.session
        
        # Se obtiene el carro de compras si existe
        carro = self.session.get("sesionCarro")
        
        # Si no existe un carro de compras, se crea uno
        if 'sesionCarro' not in request.session:
            carro = self.session['sesionCarro'] = {}
        
        # Se guarda el carro de compras en la sesión
        self.carro = carro
        
    def add(self, plato):
        # Se obtiene el id del plato
        id_plato = str(plato.id_plato)
        
        # Se verifica si el plato ya se encuentra en el carro
        if id_plato in self.carro:
            pass
        
        else:
            if plato.descuento_activo:
                print(f'CARRO.PY: Plato en oferta')
                varPrecio = plato.oferta_plato
                print(f'CARRO.PY: Precio con descuento: {varPrecio}')
                
                self.carro[id_plato] = {'precio': plato.oferta_plato}
            else:
                print(f'CARRO.PY: Plato sin oferta')
                varPrecio = plato.precio_plato
                
                self.carro[id_plato] = {'precio': plato.precio_plato}
        
        # Se guarda el carro de compras en la sesión
        self.session.modified = True