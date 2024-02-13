document.getElementById("iatTotalRows").value = document.getElementById("iatTable").rows.length;
document.getElementById("attendanceTotalRows").value = document.getElementById("attendanceTable").rows.length;
console.log(document.getElementById("iatTotalRows").value); 

let attendanceBtn = document.getElementById("attendanceAddBtn");
attendanceBtn.addEventListener("click", addRowAttendance);

let iatBtn = document.getElementById("iatAddBtn");
iatBtn.addEventListener("click", addRowIat);


function addRowIat() {
    let tbody = document.getElementById("iatTable");
    let row = tbody.insertRow(-1);

    for (let i = 0; i < 8; i++)
    {
        c = row.insertCell(i);
        elem = document.createElement("input");
        elem.type = "text";
        c.appendChild(elem);

    }

    document.getElementById("iatTotalRows").value = Number(document.getElementById("iatTotalRows").value) + 1;
    console.log(document.getElementById("iatTotalRows").value);

}

function addRowAttendance() {
    let tbody = document.getElementById("attendanceTable");
    let row = tbody.insertRow(-1);

    for (let i = 0; i < 12; i++)
    {
        c = row.insertCell(i);
        elem = document.createElement("input");
        elem.type = "text";
        c.appendChild(elem);

    }

    document.getElementById("attendanceTotalRows").value = Number(document.getElementById("attendanceTotalRows").value) + 1;
    console.log(document.getElementById("attendanceTotalRows").value);

}