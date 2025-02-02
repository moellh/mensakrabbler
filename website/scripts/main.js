"use strict";

const MONDAY = 1;
const TUESDAY = 2;
const WEDNESDAY = 3;
const THURSDAY = 4;
const FRIDAY = 5;
const SATURDAY = 6;
const SUNDAY = 0;

function setupTheme() {
    let body = document.body;
    const themeToggle = document.getElementById("theme-toggle");

    const savedTheme = localStorage.getItem("theme");
    const prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (savedTheme) {
        body.classList.add(savedTheme);
    } else if (prefersDarkMode) {
        body.classList.add("dark-mode");
        localStorage.setItem("theme", "dark-mode");
    } else {
        localStorage.setItem("theme", "light-mode");
    }

    themeToggle.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        const theme = body.classList.contains("dark-mode") ? "dark-mode" : "light-mode";
        localStorage.setItem("theme", theme);
    });
}

let activeWeekday = null;
function setActivateButton(weekday) {
    if (activeWeekday === weekday) {
        return;
    }

    // Remove css highlighting
    let buttons = document.getElementsByClassName("weekday-button");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("active");
    }

    // Highlight selected button
    let button = buttons[weekday - 1];
    console.log(button);
    button.classList.add("active");

    activeWeekday = weekday;
}

function showTodaysTable() {
    let today = new Date().getDay();

    // Show next weeks table on Saturday and Sunday
    if (today == SATURDAY || today == SUNDAY) {
        today = MONDAY;
    }

    showTable(today);
}

function showTable(weekday) {
    setActivateButton(weekday);

    let tables = document.querySelectorAll("#table-container div");
    tables.forEach(function (table) {
        table.style.display = "none";
    });
    tables[weekday - 1].style.display = "block";
}

document.addEventListener("DOMContentLoaded", function () {
    setupTheme();
    showTodaysTable();
});
