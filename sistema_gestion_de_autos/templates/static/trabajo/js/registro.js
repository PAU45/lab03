document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("VehiculoForm");
    const requiredFields = form.querySelectorAll("[required]");

  
    form.addEventListener("submit", function (event) {
        let valid = true;

      
        requiredFields.forEach(field => {
            if (field.value.trim() === "") {
                valid = false;
                alert(`El campo ${field.previousElementSibling.innerText} es obligatorio.`);
            }
        });

        
        if (!valid) {
            event.preventDefault();
        }
    });
});