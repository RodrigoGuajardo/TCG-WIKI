function validarMail(){
    let user = document.querySelector("#mail");
    if(mail.value.length >=6){
        user.classList.add("correct")
        user.classList.remove("incorrect")
        document.querySelector("#error-mail").innerHTML =""
    }else{
        user.classList.add("incorrect")
        user.classList.remove("correct")
        document.querySelector("#error-mail").innerHTML ="El usuario debe contener minimo 6 caracteres!!!"

    };

}

