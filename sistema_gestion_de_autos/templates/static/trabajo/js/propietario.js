// propietario.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("propietarioForm");
    const errorMessage = document.createElement("div");
    errorMessage.className = "error-message";
    errorMessage.style.color = "red";
    errorMessage.style.marginBottom = "15px";
    form.insertBefore(errorMessage, form.firstChild); // Agregar el mensaje de error al inicio del formulario

    form.addEventListener("submit", function (event) {
        errorMessage.textContent = ""; // Limpiar mensajes de error
        errorMessage.style.display = "none"; // Ocultar mensaje de error

        const nombre = document.getElementById("id_nombre").value.trim();
        const numeroApartamento = document.getElementById("id_numero_apartamento").value.trim();
        const telefono = document.getElementById("id_telefono").value.trim();
        const email = document.getElementById("id_email").value.trim();

        // Validaciones
        if (!nombre || !numeroApartamento || !telefono || !email) {
            errorMessage.textContent = "Todos los campos son requeridos.";
            errorMessage.style.display = "block"; // Mostrar mensaje de error
            event.preventDefault();
            return;
        }

        // Validar  (solo 3 dígitos)
        if (!/^\d{3}$/.test(numeroApartamento)) {
            errorMessage.textContent = "El número de apartamento debe tener exactamente 3 dígitos.";
            errorMessage.style.display = "block"; // Mostrar mensaje de error
            event.preventDefault();
            return;
        }

        // Validar  (exactamente 9 dígitos)
        if (!/^\d{9}$/.test(telefono)) {
            errorMessage.textContent = "El teléfono debe contener exactamente 9 dígitos.";
            errorMessage.style.display = "block"; // Mostrar mensaje de error
            event.preventDefault();
            return;
        }

        // Validar 
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            errorMessage.textContent = "Por favor, introduce un email válido.";
            errorMessage.style.display = "block"; // Mostrar mensaje de error
            event.preventDefault();
            return;
        }
    });
});