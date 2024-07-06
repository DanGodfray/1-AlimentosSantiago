// Selecciona el botón del carrito y el contenedor de productos del carrito
const btnCart = document.querySelector('.container-cart-icon');
const containerCartProducts = document.querySelector('.container-cart-products');

// Función para alternar la visibilidad del carrito de compras
function toggleCart() {
    containerCartProducts.classList.toggle('hidden-cart');
}

// Oculta inicialmente el carrito de compras al cargar la página
containerCartProducts.classList.add('hidden-cart');

// Agrega un evento de clic al botón del carrito para alternar su visibilidad
btnCart.addEventListener('click', toggleCart);

/* ========================= */
const cartInfo = document.querySelector('.cart-product');
const rowProduct = document.querySelector('.row-product');

// Lista de todos los contenedores de productos
const productsList = document.querySelectorAll('.container-items, #nath-adulto');

// Variable de arreglos de Productos
let allProducts = JSON.parse(localStorage.getItem('cartProducts')) || [];

const valorTotal = document.querySelector('.total-pagar');
const countProducts = document.querySelector('#contador-productos');

const cartEmpty = document.querySelector('.cart-empty');
const cartTotal = document.querySelector('.cart-total');

// Función para mostrar HTML
const showHTML = () => {
    if (!allProducts.length) {
        cartEmpty.classList.remove('hidden');
        rowProduct.classList.add('hidden');
        cartTotal.classList.add('hidden');
    } else {
        cartEmpty.classList.add('hidden');
        rowProduct.classList.remove('hidden');
        cartTotal.classList.remove('hidden');
    }

    // Limpiar HTML
    rowProduct.innerHTML = '';

    let total = 0;
    let totalOfProducts = 0;

    allProducts.forEach(product => {
        const containerProduct = document.createElement('div');
        containerProduct.classList.add('cart-product');

        containerProduct.innerHTML = `
            <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">$${(product.price * product.quantity).toLocaleString('de-DE')}</span>
            </div>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="icon-close"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                />
            </svg>
        `;

        rowProduct.append(containerProduct);

        total += product.price * product.quantity;
        totalOfProducts += product.quantity;
    });

    valorTotal.innerText = `$${total.toLocaleString('de-DE')}`;
    countProducts.innerText = totalOfProducts;
};

// Función para guardar en localStorage
const saveToLocalStorage = () => {
    localStorage.setItem('cartProducts', JSON.stringify(allProducts));
};

// Mostrar los productos guardados al cargar la página
document.addEventListener('DOMContentLoaded', showHTML);

productsList.forEach(container => {
    container.addEventListener('click', e => {
        if (e.target.classList.contains('btn-add-cart')) {
            const product = e.target.closest('.item, .texto');

            // Obtener el precio del producto y convertirlo a un número
            const priceText = product.querySelector('.precio-item').textContent;
            const price = parseFloat(priceText.replace('$', ' ').replace('', '').replace('.', ','));

            const infoProduct = {
                quantity: 1,
                title: product.querySelector('h3').textContent,
                price: price, // Usar el precio convertido a número
            };

            const exists = allProducts.some(product => product.title === infoProduct.title);

            if (exists) {
                const products = allProducts.map(product => {
                    if (product.title === infoProduct.title) {
                        product.quantity++;
                        return product;
                    } else {
                        return product;
                    }
                });
                allProducts = [...products];
            } else {
                allProducts = [...allProducts, infoProduct];
            }

            saveToLocalStorage();
            showHTML();
        }
    });
});

rowProduct.addEventListener('click', e => {
    if (e.target.classList.contains('icon-close')) {
        const product = e.target.parentElement;
        const title = product.querySelector('p').textContent;

        allProducts = allProducts.filter(product => product.title !== title);

        saveToLocalStorage();
        showHTML();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    // Asumiendo que ya tienes tu código de carrito aquí

    // Añadir el evento de clic al botón "Comprar"
    document.getElementById('comprar-btn').addEventListener('click', () => {
        // Redirigir a la página de checkout
        window.location.href = '/checkout/';
    });
});

// Después de agregar un producto al carrito
localStorage.setItem('cartProducts', JSON.stringify(allProducts));
