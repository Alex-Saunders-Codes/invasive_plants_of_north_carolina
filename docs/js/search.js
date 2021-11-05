
let plantSubmit = document.getElementById('plantSubmit');



plantSubmit.addEventListener('click', function () {
    let plantInput = document.getElementById("plantInput").value;
    let state = document.getElementById("stateList").value;
    sessionStorage.setItem('plant', plantInput);
    sessionStorage.setItem('state', state);
    console.log(sessionStorage.getItem('plant'));
    console.log(sessionStorage.getItem('state'));
    window.location.href = 'dashboard.html';
})
