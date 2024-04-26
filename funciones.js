function validarMail(){
    let user = document.querySelector("#user")
    if(user.value.length >= 6){
        user.classList.add("correct");
        user.classList.remove("incorrect");
        document.querySelector("#error-user").innerHTML = "&nbsp;";

    }else{
        user.classList.add("incorrect");
        user.classList.remove("correct");
        document.querySelector("#error-user").innerHTML = "error, ingrese 6 caracteres minimo.";

    }


}

function validarPass(){
    let clave = document.querySelector("#clave");
    if(clave.value.length > 5 && clave.value.length <= 12){
        clave.classList.add("correct");
        clave.classList.remove("incorrect");
        document.querySelector("#error-clave").innerHTML = "&nbsp;";
    }else{
        clave.classList.add("incorrect");
        clave.classList.remove("correct");
        document.querySelector("#error-clave").innerHTML = "error, ingrese entre 6 y 12 caracteres.";

    }

}
function validarPass(){
    let clave = document.querySelector("#clave");
    if(clave.value.length > 5 && clave.value.length <= 12){
        clave.classList.add("correcto");
        clave.classList.remove("incorrecto");
        document.querySelector("#error-clave").innerHTML = "&nbsp;";
    }else{
        clave.classList.add("incorrecto");
        clave.classList.remove("correcto");
        document.querySelector("#error-clave").innerHTML = "error, ingrese entre 6 y 12 caracteres.";

    }

}

function validarFormulario(){
    let inputs = document.querySelectorAll("input");
    let correctos = true;
    inputs.forEach(element => {
        if(element.classList.contains("incorrecto")){
            correctos = false
        }
        
    });
    if(correctos){
        document.querySelector("form").submit();
    }else{
        document.querySelector("#error-form").innerHTML = "error, revise los campos";

    }
}