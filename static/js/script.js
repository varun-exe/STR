addButtons = document.querySelectorAll(".addBtn");

addButtons.forEach(function(btn) {
    document.getElementById(btn.getAttribute("data-increement")).value = Number(document.getElementById(btn.getAttribute("data-for")).rows.length); 
    btn.addEventListener("click", addRow);
})


function addRow() {
    table = document.getElementById(this.getAttribute("data-for"));
    row = table.rows[0];
    value_pattern = /value=('|")(.*)('|")/gi;
    textarea_pattern = /(<textarea.*>).*(<[/]textarea>)/gi;
    code = row.innerHTML.replaceAll("row1", "row" + (table.rows.length + 1));
    code = code.replaceAll(value_pattern, '');
    code = code.replaceAll('>1<', '>' + (table.rows.length + 1)+ '<');
    code = code.replaceAll(textarea_pattern, '$1$2');
    table.insertAdjacentHTML("beforeend", code);
    document.getElementById(this.getAttribute("data-increement")).value = Number(document.getElementById(this.getAttribute("data-increement")).value) + 1; 
}

