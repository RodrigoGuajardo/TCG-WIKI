function validarMail(){
    let user = document.querySelector("#mail");
    if(mail.value.length >=6){
        user.classList.add("correct")
        user.classList.remove("incorrect")
    }else{
        user.classList.add("incorrect")
        user.classList.remove("correct")
        

    };

}