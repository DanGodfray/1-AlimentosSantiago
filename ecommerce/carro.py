class Carro():
    def __init__(self, request):
        self.session = request.session
        
        #se obtiene el carro de compras si existe
        carro = self.session.get("sesionCarro")
        
        #si no existe un carro de compras se crea uno
        if 'sesionCarro' not in request.session:
            carro = self.session['sesionCarro'] = {}
        
        #se guarda el carro de compras en la sesion
        self.carro = carro
        
    def add(self, plato):
        #se obtiene el id del plato
        id_plato = str(plato.id_plato)
        
        #se verifica si el plato ya se encuentra en el carro
        if id_plato in self.carro:
            #self.carro[id_plato]['cantidad'] += 1
            pass
        
        else:
            self.carro[id_plato] = {'precio': str(plato.precio_plato)}
        
        #se guarda el carro de compras en la sesion
        self.session.modified = True