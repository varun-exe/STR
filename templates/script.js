let addRowBtn = document.getElementById("addBtn");
addRowBtn.addEventListener("click", addRow);

function addRow() {
    let tbody = document.getElementById("attendanceTable");
    let row = tbody.insertRow(-1);

    for (let i = 0; i < 12; i++)
    {
        c = row.insertCell(i);
        elem = document.createElement("input");
        elem.type = "text";
        c.appendChild(elem);

    }

}