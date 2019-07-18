function createAccount() {
    let account = {
        firstName: document.getElementById('firstNameForm').value,
        lastName: document.getElementById('lastNameForm').value
    }

    let req = new XMLHttpRequest();

    req.onload = function () {
        let response = JSON.parse(req.response);
        console.log(response);

    }
    req.open("POST", "http://localhost:5002/account/test");
    req.send(JSON.stringify(account));
    return console.log(response.text);
}

