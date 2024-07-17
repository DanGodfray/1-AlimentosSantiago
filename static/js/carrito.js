var actualizarBotones = document.getElementsByClassName('actualiza-carrito');

for (var i = 0; i < actualizarBotones.length; i++) {
    actualizarBotones[i].addEventListener('click', function () {

        var idPlato = this.dataset.plato;
        var action = this.dataset.action;

        console.log('producto ID:', idPlato, ', acción:', action)

        console.log('USER:', usuario);

        if (user === 'AnonymousUser') {
            console.log('Usuario no autenticado');
        } else {
            //console.log('Usuario autenticado, enviando datos...');
            //actualizarPedidoUsuario(idPlato, action);

            var url = '/actualizar-carro/'

            fetch(url, {
                method: 'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({ 'platoId': idPlato, 'action': action })
            })
        
                .then((response) => {
                    return response.json();
                })
        
                .then((data) => {
                    console.log('data:', data);
                    //location.reload();
                });

        }
    });
}

function actualizarPedidoUsuario(platoId, action) {
    console.log('Usuario autenticado, enviando datos...');

    var url = '/actualizar-carro/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'platoId': platoId, 'action': action })
    })

        .then((response) => {
            return response.json();
        })

        .then((data) => {
            console.log('data:', data);
            location.reload();
        });
}