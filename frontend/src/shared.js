async function getCSRF() {
    let csrfToken;

    const json = (await fetch("http://localhost:8000/api/auth/csrf", {
        credentials: 'include'
    }).then(res => {
        csrfToken = res.headers.get('X-CSRFToken');
    }));

    return csrfToken;
}

async function isAuthenticate() {
    let isUser;

    return await fetch("http://localhost:8000/api/auth/authenticated", {
        credentials: 'include'
    })
        .then(res => res.json())
        .then(data => {
            isUser = data.isAuthenticated !== 0;
            return isUser
        });
}

function restResponseHandler(request) {
    if (request.ok) {
        const response = request.json();
        const success = true;
        return {success: success, response: response};
    } else {
        const success = false;
        const status = 'There seems to have been a problem with your request: ' + request.status + ' ' + request.statusText;
        return {success: success, response: status};
    }
}

export {getCSRF, isAuthenticate, restResponseHandler}
