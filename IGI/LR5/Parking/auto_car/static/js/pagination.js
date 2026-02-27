document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".services-grid");
    const items = Array.from(container.children);
    const pagination = document.getElementById("pagination");
    const perPageSelect = document.getElementById("per-page-select");

    let perPage = Number(localStorage.getItem("per_page")) || 3;

    perPageSelect.value = perPage;

    let currentPage = 1;

    function render() {
        const totalPages = Math.ceil(items.length / perPage);

        items.forEach(el => el.style.display = "none");
        const start = (currentPage - 1) * perPage;
        const end = start + perPage;
        items.slice(start, end).forEach(el => el.style.display = "");

        pagination.innerHTML = "";
        for (let i = 1; i <= totalPages; i++) {
            const btn = document.createElement("button");
            btn.textContent = i;
            if (i === currentPage) btn.classList.add("active");
            btn.onclick = () => {
                currentPage = i;
                render();
            }
            pagination.appendChild(btn);
        }
    }

    perPageSelect.addEventListener("change", () => {
        perPage = Number(perPageSelect.value);
        localStorage.setItem("per_page", perPage);
        currentPage = 1;
        render();
    });

    render();
});
