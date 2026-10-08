const API_URL = "http://127.0.0.1:8000";

const token =
    localStorage.getItem("accessToken");


if (!token) {
    window.location.href = "login.html";
}


const headers = {
    Authorization: `Bearer ${token}`
};


async function getData(endpoint) {

    const response = await fetch(
        `${API_URL}${endpoint}`,
        {
            headers
        }
    );

    if (response.status === 401) {

        logout();

        return null;
    }

    if (!response.ok) {
        throw new Error(
            "Error al consultar la API."
        );
    }

    return response.json();
}


async function loadDashboard() {

    try {

        const students =
            await getData("/api/students/");

        const classes =
            await getData("/api/classes/");

        const attendance =
            await getData("/api/attendance/");


        if (!students ||
            !classes ||
            !attendance) {

            return;
        }


        document.getElementById(
            "studentCount"
        ).textContent =
            students.length;


        document.getElementById(
            "classCount"
        ).textContent =
            classes.length;


        document.getElementById(
            "attendanceCount"
        ).textContent =
            attendance.length;


        const table =
            document.getElementById(
                "studentsTable"
            );

        table.innerHTML = "";


        students.forEach(student => {

            const row =
                document.createElement("tr");

            row.innerHTML = `
                <td>
                    ${student.first_name}
                    ${student.last_name}
                </td>

                <td>
                    ${student.level || "-"}
                </td>

                <td>
                    ${student.email || "-"}
                </td>
            `;

            table.appendChild(row);

        });

    } catch (error) {

        console.error(error);

    }
}


function logout() {

    localStorage.removeItem(
        "accessToken"
    );

    localStorage.removeItem(
        "refreshToken"
    );

    window.location.href =
        "login.html";
}


document
    .getElementById("logoutButton")
    .addEventListener(
        "click",
        logout
    );


loadDashboard();