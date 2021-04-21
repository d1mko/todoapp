<script>
    import {getCSRF} from "../shared";
    import { sessionEmail } from '../stores/auth'

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
            localStorage.clear();
            sessionEmail.set(null);
            location.replace('/');
        }

    }
</script>

<button on:click={logout}>Logout</button>