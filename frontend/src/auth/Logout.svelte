<script>
    import {getCSRF} from "../shared";
    import {sessionEmail} from '../stores/auth'

    async function logout() {
        let csrf = await getCSRF();

        const resp = (await fetch("http://localhost:8000/api/auth/whoami", {
            method: "GET",
            headers: {
                "X-CSRFToken": csrf,
            },
            credentials: 'include'
        })).json();

        const logOut = (await fetch("http://localhost:8000/api/auth/logout", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrf,
            },
            credentials: "include"
        })).status

        if (logOut === 200) {
            location.replace('/');
            {
                localStorage.removeItem('sessionEmail');
                sessionEmail.update(() => localStorage.getItem('sessionEmail'));
            }

        }
    }
</script>

<style>
    .nav__btn {
        display: inline-block;
        border: none;

        background-color: #333333;
        color: #ffffff;
        text-transform: uppercase;
        font-size: 17px;
        font-family: "Montserrat", sans-serif;

        transition: color .1s linear;
    }


    .nav__btn:hover {
        color: #fce38a;
        cursor: pointer;
    }
</style>

<button class="nav__btn" on:click={logout}>Logout</button>