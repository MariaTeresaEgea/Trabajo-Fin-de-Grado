const API_URL = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("loginForm");
    const errorMessage = document.getElementById("errorMessage");

    if (!form) {
        console.error("No se encontró el formulario loginForm");
        return;
    }

    form.addEventListener("submit", async (event) => {

        event.preventDefault();

        const username =
            document.getElementById("username").value.trim();

        const password =
            document.getElementById("password").value;

        errorMessage.textContent = "";
        errorMessage.style.color = "#c62828";

        try {

            const response = await fetch(
                `${API_URL}/api/token/`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json; charset=UTF-8"
                    },

                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "Usuario o contraseña incorrectos."
                );
            }

            localStorage.setItem(
                "accessToken",
                data.access
            );

            localStorage.setItem(
                "refreshToken",
                data.refresh
            );

            window.location.href = "dashboard.html";

        } catch (error) {

            console.error("Error de login:", error);

            errorMessage.textContent =
                error.message;
        }
    });
});