document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registrationForm");

    form.addEventListener("submit", function (event) {
        let valid = true;

        // Name validation
        const name = document.getElementById("name").value.trim();
        const nameError = document.getElementById("nameError");
        if (name === "") {
            nameError.textContent = "Name is required.";
            valid = false;
        } else {
            nameError.textContent = "";
        }

        // Email validation
        const email = document.getElementById("email").value.trim();
        const emailError = document.getElementById("emailError");
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailPattern.test(email)) {
            emailError.textContent = "Enter a valid email address.";
            valid = false;
        } else {
            emailError.textContent = "";
        }

        // Phone number validation
        const phone = document.getElementById("phone").value.trim();
        const phoneError = document.getElementById("phoneError");
        const phonePattern = /^[0-9]{10}$/;
        if (!phonePattern.test(phone)) {
            phoneError.textContent = "Enter a valid 10-digit phone number.";
            valid = false;
        } else {
            phoneError.textContent = "";
        }

        // Age validation
        const age = document.getElementById("age").value.trim();
        const ageError = document.getElementById("ageError");
        if (age === "" || isNaN(age) || age < 1) {
            ageError.textContent = "Enter a valid age.";
            valid = false;
        } else {
            ageError.textContent = "";
        }

        if (!valid) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});
