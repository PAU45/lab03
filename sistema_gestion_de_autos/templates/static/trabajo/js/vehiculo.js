document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("vehiculoForm");
    const matriculaInput = document.getElementById("id_matricula");

   
    matriculaInput.addEventListener("input", function () {
        // Eliminar caracteres no numéricos
        this.value = this.value.replace(/[^0-9]/g, "");
        
     
        if (this.value.length > 3) {
            this.value = this.value.slice(0, 3) + '-' + this.value.slice(3, 6);
        }
    });

   
    form.addEventListener("submit", function (event) {
        let valid = true;

        // Validar que todos los campos requeridos estén completos
        const requiredFields = form.querySelectorAll("[required]");
        requiredFields.forEach(field => {
            if (field.value.trim() === "") {
                valid = false;
                alert(`El campo ${field.previousElementSibling.innerText} es obligatorio.`);
            }
        });

        
        if (matriculaInput.value.length !== 7) { // 6 dígitos + 1 guion
            valid = false;
            alert("La matrícula debe tener 6 dígitos en total, con un guion después del tercer dígito.");
        }

        
        if (!valid) {
            event.preventDefault();
        }
    });
});