"use strict";
function goBack() {
    alert("Ortga qaytdingiz!");
}

function saveData() {
    const name = document.getElementById("name").value.trim();
    const weight = document.getElementById("weight").value.trim();
    const date = document.getElementById("date").value.trim();

    let valid = true;

    document.getElementById("nameError").textContent = "";
    document.getElementById("weightError").textContent = "";
    document.getElementById("dateError").textContent = "";
    document.getElementById("result").textContent = "";

    if (name === "") {
        document.getElementById("nameError").textContent = "Sabzavot nomini kiriting!";
        valid = false;
    }
    if (weight === "") {
        document.getElementById("weightError").textContent = "Og'irligini kiriting!";
        valid = false;
    }
    if (date === "") {
        document.getElementById("dateError").textContent = "Sana kiriting!";
        valid = false;
    }

    if (valid) {
        document.getElementById("result").textContent =
            `Saqlangan: ${name}, ${weight} kg, sana: ${date}`;
    }
}
