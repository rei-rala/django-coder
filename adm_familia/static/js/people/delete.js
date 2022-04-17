document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    confirm(
        "¿Estás seguro de que quieres eliminar la entrada?"
    ) && e.target.submit();
});