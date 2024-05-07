function validarUser() {
    let user = document.querySelector("#user");
    if (user.value.length >= 6) {
        user.classList.add("correct");
        user.classList.remove("incorrect");
        document.querySelector("#error-user").innerHTML = "&nbsp;";
    } else {
        user.classList.add("incorrect");
        user.classList.remove("correct");
        document.querySelector("#error-user")
            .innerHTML = "Error, ingrese 6 caracteres mínimo.";
    }
}

function validarPass() {
    let clave = document.querySelector("#clave");
    if (clave.value.length > 5 && clave.value.length < 13) {
        clave.classList.add("correct");
        clave.classList.remove("incorrect");
        document.querySelector("#error-clave").innerHTML = "&nbsp;";
    } else {
        clave.classList.add("incorrect");
        clave.classList.remove("correct");
        document.querySelector("#error-clave")
            .innerHTML = "Error, ingrese entre 6 y 12 caracteres.";
    }
}

function validarFormulario() {
    let inputs = document.querySelectorAll("input");
    let correctos = true;
    inputs.forEach(element => {
        if (element.classList.contains("incorrect")) {
            correctos = false
        }
    });
    if (correctos) {
        document.querySelector("form").submit();
        
    } else {
        document.querySelector("#error-form")
            .innerHTML = "Error, revise los campos.";
    }
}










let cartasMYL = [
    {
        "nombre":"Sobre Mitos y Leyendas Furia",
        "precio":"20000",
        "imagen":"Images/sobre 11 cartas myl.png"

    }

]

function cargarMYL(){
    fetch('https://mindicador.cl/api').then(function(response) {
        return response.json();
    }).then(function(dailyIndicators) {
        let dolar = parseFloat(dailyIndicators.dolar.valor);
        let productos = document.querySelector("#productosMYL");
        for(let item of cartasMYL){
            let producto = document.createElement("div");
            producto.classList.add("producto");
            let imagen = document.createElement("div");
            imagen.classList.add("imagen");
            imagen.style.backgroundImage = 'url('+ item.imagen +')';
            producto.appendChild(imagen);
            let nombre = document.createElement("div");
            nombre.classList.add("nombre");
            nombre.innerHTML = item.nombre;
            producto.appendChild(nombre);
            let precio = document.createElement("div");
            precio.classList.add("precio");
            precio.innerHTML = "$"+item.precio + " (USD "+ (item.precio/dolar).toFixed(1) +")";
            producto.appendChild(precio);
            productos.appendChild(producto);
        }
    }).catch(function(error) {
        console.log('Requestfailed', error);
    });
}


let items = [
    {
        "nombre":"MTG BUNDLE: Modern Horizons 3 - Ingles",
        "precio":99990,
        "imagen":"Images/magic_modrn_horizons.png"
    },
    {
        "nombre":"MTG Mazo Inicial Commander - Triunfo de las Fichas",
        "precio":27990,
        "imagen":"Images/mazo inicial commander.png"
    },
    
]

function cargarMTG(){
    fetch('https://mindicador.cl/api').then(function(response) {
        return response.json();
    }).then(function(dailyIndicators) {
        let dolar = parseFloat(dailyIndicators.dolar.valor);
        let productos = document.querySelector("#productosMTG");
        for(let item of items){
            let producto = document.createElement("div");
            producto.classList.add("producto");

            let imagen = document.createElement("div");
            imagen.classList.add("imagen");
            imagen.style.backgroundImage = 'url('+ item.imagen +')';
            producto.appendChild(imagen);

            let nombre = document.createElement("div");
            nombre.classList.add("nombre");
            nombre.innerHTML = item.nombre;
            producto.appendChild(nombre);

            let precio = document.createElement("div");
            precio.classList.add("precio");
            precio.innerHTML = "$"+item.precio + " (USD "+ (item.precio/dolar).toFixed(1) +")";
            producto.appendChild(precio);

            productos.appendChild(producto);
        }
    }).catch(function(error) {
        console.log('Requestfailed', error);
    });
}