document.addEventListener('DOMContentLoaded', () => {
    const checkoutProductsContainer = document.querySelector('.checkout-products');
    const valorTotal = document.querySelector('.total-pagar');
    
    // Obtener los productos del carrito desde localStorage
    const allProducts = JSON.parse(localStorage.getItem('cartProducts')) || [];

    // Función para mostrar los productos en la página de checkout
    const showCheckoutProducts = () => {
        let total = 0;

        checkoutProductsContainer.innerHTML = ''; // Limpiar contenido anterior

        allProducts.forEach(product => {
            const productElement = document.createElement('div');
            productElement.classList.add('checkout-product');

            productElement.innerHTML = `
                <div class="info-checkout-product">
                    <span class="cantidad-producto">${product.quantity}</span>
                    <p class="titulo-producto">${product.title}</p>
                    <span class="precio-producto">$${(product.price * product.quantity).toLocaleString('de-DE')}</span>
                </div>
            `;

            checkoutProductsContainer.append(productElement);

            total += product.price * product.quantity;
        });

        valorTotal.innerText = `$${total.toLocaleString('de-DE')}`;
    };

    // Mostrar los productos al cargar la página
    showCheckoutProducts();
});





// Mensaje de confirmar la compra

document.getElementById('confirm-purchase').addEventListener('click', () => {
    alert('Compra confirmada!');

    // Limpiar el carrito y el localStorage
    localStorage.removeItem('cartProducts');
    window.location.href = 'thankyou.html'; // Redirigir a una página de agradecimiento
});
