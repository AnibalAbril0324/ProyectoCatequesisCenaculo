document.addEventListener("DOMContentLoaded", function() {
    const nombreField = document.getElementById("nombres");
    const apellidoField = document.getElementById("apellidos");
    const telefonoField = document.getElementById("telefono");

    if (!nombreField) {
        console.error("El campo de nombre no existe.");
        return;
    }

    if(!apellidoField){
        console.error("El campo de apellido no existe");
        return;
    }

    if(!telefonoField){
        console.error("El campo telefono no existe");
    }

    const nombreErrorDiv = crearErrorDiv(nombreField);
    const apellidoErrorDiv = crearErrorDiv(apellidoField);
    const telefonoErrorDiv = crearErrorDiv(telefonoField);

    nombreField.addEventListener("blur", function() {
        validarCampo(nombreField.value.trim(), nombreErrorDiv,"El Nombre debe contener solo letras",validarsololetras);
    });

    apellidoField.addEventListener("blur", function(){
        validarCampo(apellidoField.value.trim(),apellidoErrorDiv,"El Apellido debe contener solo letras",validarsololetras);
    });

    telefonoField.addEventListener("blur",function(){
        validarCampo(telefonoField.value.trim(),telefonoErrorDiv,"El telefono debe contener solo numeros",validarsolonumeros)
    });

    function crearErrorDiv(parentField) {
        const errorDiv = document.createElement("div");
        errorDiv.style.color = "red";
        parentField.parentNode.appendChild(errorDiv);
        return errorDiv;
    }

    function validarCampo(valor,errorDiv,mensajedeerror,validacion) {

        //los valores que recibimos son el valor que hace referencia al nombre ingresado
        //el error en caso de que esto suceda
        //y el mensaje de error que aparecera cuando exista el error

        console.log('valor ingresado:', valor);

        if (valor === "") {
            errorDiv.textContent = "";
            return;
        }

        if (!validacion(valor)) {
            //el codigo va a mostrar el error porque el usuario ingreso un nombre
            //que contenga otros caracteres no validos
            mostrarerror(errorDiv, mensajedeerror,"red");
            console.log(mensajedeerror);
        } else {
            //este codigo se ejecutara cuando el nombre ingresado solo letras
            mostrarCheck(errorDiv, "✔️", "green"); // Emoji de check
            console.log("El valor es válido.");
        }
    }

    function mostrarerror(errorDiv, mensaje,color){
        errorDiv.textContent = mensaje;
        errorDiv.style.color = color;
    }

    function mostrarCheck(errorDiv, mensaje, color) {
        errorDiv.textContent = mensaje;
        errorDiv.style.color = color;
        errorDiv.classList.add('success-check');
    }

    //funcion que me permite validar que el campo solo permita ingresar letras
    function validarsololetras(valor) {
        const regex = /^[a-zA-Z\s]+$/;
        return regex.test(valor);
    }

    //funcion que me permite validar que el campo solo permita ingresar numeros
    function validarsolonumeros(valor){
        const regex = /^[0-9]+$/;
        return regex.test(valor);
    }
});