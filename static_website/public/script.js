function createAccount() {
    let account = {
        firstName: document.getElementById('firstNameForm').value,
        lastName: document.getElementById('lastNameForm').value
    };
    console.log(JSON.stringify(account));

    let req = new XMLHttpRequest();

    req.onload = function () {
        console.log(req.responseText);

    }
    req.open("POST", "http://51.144.95.241:8084/addAccount");
    req.send(JSON.stringify(account));
    console.log(req.responseText);
}


