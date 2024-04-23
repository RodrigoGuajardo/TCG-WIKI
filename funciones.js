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