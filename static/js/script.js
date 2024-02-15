addButtons = document.querySelectorAll(".addBtn");

addButtons.forEach(function(btn) {
    document.getElementById(btn.getAttribute("data-increement")).value = 1;
    btn.addEventListener("click", addRow);
})


function addRow() {
    table = document.getElementById(this.getAttribute("data-for"));
    row = table.rows[0];
    table.insertAdjacentHTML("beforeend", row.innerHTML)
    document.getElementById(this.getAttribute("data-increement")).value = Number(document.getElementById(this.getAttribute("data-increement")).value) + 1; 
}