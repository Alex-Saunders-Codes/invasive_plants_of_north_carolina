
plantSubmit = document.getElementById();



plantSubmit.addEventListener('click', function () {
    plantInput = document.getElementById("plantInput").value;
    state = document.getElementById("stateList");
    sessionStorage.setItem('plant', plantInput);
    sessionStorage.setItem('state', state);
    window.location.href = 'dashboard.html';
}
