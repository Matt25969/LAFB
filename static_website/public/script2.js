
function getAPrize() {

    let accountDetails = {
        "firstName": document.getElementById("FirstNameBox").value;
        "lastName": document.getElementById("LastNameBox").value;
    }

    let req = new XMLHttpRequest();

    req.onload = function () {
        promises(req);
    }
    
    req.open("POST", "server/addAccount");
    req.send(JSON.stringify(accountDetails));
}

function promises(req) {
    const createPromise = new Promise(
        function (res, rej) {
            if (req.status === 200) {
                let result = JSON.parse(req.responseText);
                res(result);
            } else {
                const reason = new Error(req.status);
                rej(reason);
            }
        }
    );

    createPromise
        .then(result => resolved(result))
        .catch(error => rejected(error))

}

function resolved(result) {
    let response = JSON.parse(req.response);
    console.log(response);
}

function rejected(reason) {
    console.log(reason);
}
        
