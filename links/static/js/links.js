function checkURLS() {
    var table = document.getElementById("linksTable");
    for (var i = 1, row; row = table.rows[i]; i++) {
        var url = row.cells[1].firstChild.textContent
        var btn = document.getElementById("btn_" + i);
        if (btn.classList.contains('btn-light')) {
            continue;
        }
        checkUrlStatus(row.id, url);
    }

    setTimeout(checkURLS, getTimerSec());

}

function checkUrlStatus(rowId, url) {
    var request = new XMLHttpRequest();
    request.open('POST', '/checkURL/', true);
    request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    request.onreadystatechange = function(){
            var row = document.getElementById(rowId);
            if (request.status === 200) {
                var result = JSON.parse(request.responseText);
                if(result['status'] == 200) {
                    row.style.backgroundColor = 'green';
                } else {
                    row.style.backgroundColor = 'red';
                }
            } else {
                row.style.backgroundColor = 'red';
            }
    };
    let data = "url="+url;
    request.send(data);
}

function getTimerSec() {
    let timerInput = document.getElementById("timer");
    var waitSec = timerInput.value * 1000;
    return waitSec;
}

document.addEventListener('DOMContentLoaded', function(){
    setTimeout(checkURLS, getTimerSec());
});

function pause(id) {
    var btn = document.getElementById("btn_" + id);
    if (btn.classList.contains('btn-light')) {
        btn.classList.remove('btn-light');
        btn.classList.add('btn-success');
        btn.textContent = 'Active';
    } else {
        btn.classList.remove('btn-success');
        btn.classList.add('btn-light');
        btn.textContent = 'Inactive';
    }

}
