function decrement() {
    var elem = document.getElementById("count");
    var count = Number(elem.innerText);
    elem.innerText = Math.max(count - 1, 0);
}
function increment() {
    var elem = document.getElementById("count");
    var count = Number(elem.innerText);
    elem.innerText = count + 1;
}

function getDate(){
    var elem = document.getElementById("date");
    elem.innerText = (new Date()).toDateString();
}
