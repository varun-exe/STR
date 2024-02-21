function setup_percentage() {
    document.querySelectorAll(".percentage").forEach(function(elem) {
    
        elem.addEventListener('input', function() {
            let name_field = elem.getAttribute('name');
            let num = name_field.substring(name_field.length - 1, name_field.length);
            name_field = name_field.substring(0, name_field.length - 2);
    
            percentage = document.querySelector("input[name=" + name_field + "P" + num + "]");
            attendended = document.querySelector("input[name=" + name_field + "A" + num + "]");
            total = document.querySelector("input[name=" + name_field + "T" + num + "]");
            
            if (Number(attendended.value) <= Number(total.value))
            {
                percentage.value = (Number(attendended.value) / Number(total.value) * 100).toFixed(2);
            }
            else
            {
                percentage.value = "-";
            }
        });
    });
}

setup_percentage();

// set nav-link as active
let nav_links = document.querySelectorAll(".nav-link");
for (var i = 0; i < nav_links.length; i++) {
  if (nav_links[i].href === window.location.href || nav_links[i].href == window.location.href.replace("-edit?", "")) {
    nav_links[i].parentNode.classList.add("active-link");
  }
}


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
    code = code.replaceAll(value_pattern, "value=''");
    code = code.replaceAll('>1<', '>' + (table.rows.length + 1)+ '<');
    code = code.replaceAll(textarea_pattern, '$1$2');
    table.insertAdjacentHTML("beforeend", code);
    document.getElementById(this.getAttribute("data-increement")).value = Number(document.getElementById(this.getAttribute("data-increement")).value) + 1; 
    setup_percentage();
}

