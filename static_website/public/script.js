const URLstring = "http://51.140.119.170";
function getAPrize() {
	
}

function makeRequest(method, url, body) {
    return new Promise(
        (resolve, reject) => {
            let req = new XMLHttpRequest();
            if ("withCredentials" in req) {
                // Check if the XMLHttpRequest object has a "withCredentials" property.
                // "withCredentials" only exists on XMLHTTPRequest2 objects.
                req.open(method, url, true);
                req.setRequestHeader('Content-Type', 'application/json');
                req.send(body);
            } else if (typeof XDomainRequest != "undefined") {
                // Otherwise, check if XDomainRequest.
                // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
                req = new XDomainRequest();
                req.open(method, url);
                req.setRequestHeader('Content-Type', 'application/json');
                req.send(body);
            } else {
                // Otherwise, CORS is not supported by the browser.
                throw new Error('CORS not supported');
            }

            req.onload = () => {
                if (req.status >= 200 && req.status <= 299) {
                    resolve(req.responseText);
                } else {
                    console.log(req.responseText)
                    const reason = new Error("Rejected");
                    reject(reason);
                }
            }

        });
}
