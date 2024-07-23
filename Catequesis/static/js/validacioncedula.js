document.addEventListener("DOMContentLoaded", function() {
    const cedulaField = document.getElementById("cedula-field");
    if (!cedulaField) {
        console.error("El campo de cédula no existe.");
        return;
    }

    const errorDiv = document.createElement("div");
    errorDiv.style.color = "red";
    cedulaField.parentNode.appendChild(errorDiv);

    cedulaField.addEventListener("blur", function() {
        const cedulaIngresada = cedulaField.value.trim();

        console.log('Cédula ingresada:', cedulaIngresada);

        if (cedulaIngresada === "") {
            errorDiv.textContent = "";
            return;
        }

        if (cedulaIngresada.length !== 10) {
            errorDiv.textContent = "La cédula debe tener exactamente 10 dígitos.";
            errorDiv.style.color = "red";
            console.log("La cédula debe tener exactamente 10 dígitos.");
        } else {
            if (validarCedula(cedulaIngresada)) {
                console.log("La cédula es válida.");
                errorDiv.textContent = "Cédula correcta.";
                errorDiv.style.color = "green";
            } else {
                console.log("La cédula no es válida.");
                errorDiv.textContent = "Cédula incorrecta";
                errorDiv.style.color = "red";
            }
        }
    });

    function calcularDigitoVerificador(cedula) {
        const pesos = [2, 1, 2, 1, 2, 1, 2, 1, 2];
        let suma = 0;

        for (let i = 0; i < cedula.length - 1; i++) {
            let digito = parseInt(cedula[i]);
            let producto = digito * pesos[i];
            suma += (producto >= 10) ? producto - 9 : producto;
        }

        let digitoVerificador = (10 - (suma % 10)) % 10;
        console.log(`Suma: ${suma}, Dígito verificador calculado: ${digitoVerificador}`);
        return digitoVerificador;
    }

    function validarCedulaBasica(cedula) {
        const regex = /^\d{10}$/;
        return regex.test(cedula);
    }

    function validarCedula(cedula) {
        if (!validarCedulaBasica(cedula)) {
            console.log("La cédula no contiene solo números o no tiene 10 dígitos.");
            return false;
        }

        const digitoVerificadorCalculado = calcularDigitoVerificador(cedula);
        const digitoVerificadorIngresado = parseInt(cedula[9]);
        console.log(`Dígito verificador ingresado: ${digitoVerificadorIngresado}`);
        return digitoVerificadorCalculado === digitoVerificadorIngresado;
    }
});
