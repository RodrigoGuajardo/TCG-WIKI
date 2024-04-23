function validarUser(){
    let user = document.querySelector("#user")
    if(user.value.length >= 6){
        user.classList.add("correcto");
        user.classList.remove("incorrecto");
        document.querySelector("#error-user").innerHTML = "&nbsp;";

    }else{
        user.classList.add("incorrecto");
        user.classList.remove("correcto");
        document.querySelector("#error-user").innerHTML = "error, ingrese 6 caracteres minimo.";

    }


}

function validarPass(){
    let clave = document.querySelector("#clave");
    if(clave.value.length > 5 && clave.value.length <11){
        clave.classList.add("correcto");
        clave.classList.remove("incorrecto");
        document.querySelector("#error-clave").innerHTML = "&nbsp;";
    }else{
        clave.classList.add("incorrecto");
        clave.classList.remove("correcto");
        document.querySelector("#error-clave").innerHTML = "error, ingrese 6 y 12 caracteres.";

    }

}