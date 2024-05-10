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








let cartasPoke = [
    {
        "nombre":"V-Batle deck Victini",
        "precio":"24990",
        "imagen":"Images/mazo pokemon.png"

    },
    {
        "nombre":"V-Batle deck Gardevoir",
        "precio":"24990",
        "imagen":"Images/mazo gardevoir.png"
    },
    {
        "nombre":"V-Batle deck Victini & Gardevoir",
        "precio":"61990",
        "imagen":"Images/pack pokemon victini y gardevoir.png"

    },
    {
        "nombre":"Caja Pokemon 151 Ultra-Premium Collection",
        "precio":"149990",
        "imagen":"Images/caja pokemon 151.png"
    }


]

function cargarPOKE(){
    fetch('https://mindicador.cl/api').then(function(response) {
        return response.json();
    }).then(function(dailyIndicators) {
        let dolar = parseFloat(dailyIndicators.dolar.valor);
        let productos = document.querySelector("#productosPOKE");
        for(let item of cartasPoke){
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


let cartasMYL = [
    {
        "nombre":"Sobre Mitos y Leyendas Furia",
        "precio":"2000",
        "imagen":"Images/sobre 11 cartas myl.png"

    },
    {
        "nombre":"Caja sobres Furia x24",
        "precio":"30000",
        "imagen":"Images/caja 24 sobres myl f.png"
    },
    {
        "nombre":"Caja sobre Primer Bloque x24",
        "precio":"35000",
        "imagen":"Images/caja sobre primer bloque.webp"
    },
    {
        "nombre":"Mqzo Dinastia del Dragon",
        "precio":"14990",
        "imagen":"Images/Mazo-dinastia-del-dragon_1024x1024@2x.webp"
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



let articulosYugi = [
    {
        "nombre":"Mazo estructura Yugi Muto",
        "precio":14990,
        "imagen":"Images/mazo estructura yugi.png"
    },
    {
        "nombre":"Caja sobres x24 Yu-Gi-Oh",
        "precio":34990,
        "imagen":"Images/caja sobre yugi.png"
    },
    {
        "nombre":"Mazo Dragon balnco de ojos azules",
        "precio":99990,
        "imagen":"Images/mazo dragon blanco.png"
    },
    {
        "nombre":"Sobre Yu-Gi-Oh",
        "precio":3990,
        "imagen":"Images/sobre yu gi oh.pngg"
    }
    
]



function cargarYugi(){
    fetch('https://mindicador.cl/api').then(function(response) {
        return response.json();
    }).then(function(dailyIndicators) {
        let dolar = parseFloat(dailyIndicators.dolar.valor);
        let productos = document.querySelector("#cartasYugi");
        for(let item of articulosYugi){
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