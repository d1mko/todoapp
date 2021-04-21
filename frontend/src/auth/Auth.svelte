<script>
    import {getCSRF, isAuthenticate, restResponseHandler} from "../shared";
    import { sessionEmail } from '../stores/auth'

    let authType = "login";
    let successMessage;
    let errorMessage;

    let email;
    let password;
    let passwordConfirm;

    function passwordCheck(pass) {
        let checkLower, checkUpper, checkDigits;

        checkLower = !!pass.match(/[a-z]+/);
        checkUpper = !!pass.match(/[A-Z]+/);
        checkDigits = !!pass.match(/[0-9]+/);

        return checkLower && checkUpper && checkDigits;
    }

    async function signupHandler() {
        if (password !== passwordConfirm) {
            errorMessage = "Your passwords must match. Please enter a matching Password and Confirm Password combination.";
        } else if (!passwordCheck(password)) {
            errorMessage = "Your passwords must contain at least one lowercase character, uppercase character and number.";
        } else {
            const request = await fetch("http://localhost:8000/api/auth/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                body: JSON.stringify({
                    "email": email,
                    "password": password,
                    "password2": passwordConfirm
                }),
            });

            const signUpUser = await restResponseHandler(request);
            if (signUpUser.success) {
                location.replace('/')
            } else {
                errorMessage = signUpUser.response;
            }
        }
    }

    async function loginHandler() {
        // let csrfToken = getCSRF();
        const resp = (await fetch("http://localhost:8000/api/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            credentials: 'include',
            body: JSON.stringify({
                "email": email,
                "password": password
            }),
        })).status

        if (resp === 200)
        {
            let authenticated = await isAuthenticate();
            if(authenticated) {
                localStorage.setItem('sessionEmail', email);
                sessionEmail.set(localStorage.getItem('sessionEmail'));

                location.replace('/');
            }
        }

    }
</script>

<style>

</style>

<div>
    <div class="container">
        <div class="header">
        </div>

        <div class="authorization">
            {#if errorMessage}
                <div class="notification">
                    <p>{errorMessage}</p>
                </div>
            {/if}

            {#if authType === "login"}
                <form on:submit|preventDefault={loginHandler}>
                    <p class="strong">Email</p>
                    <input bind:value={email} placeholder="name@example.com"/>
                    <p class="string">Password</p>
                    <input bind:value={password} type="password" placeholder="Password">
                    <button type="submit">Login</button>
                </form>
                <hr/>
                <button on:click={() => authType = 'signup'}>Create a New Account Instead</button>
            {:else if authType === "signup"}
                <form on:submit|preventDefault={signupHandler}>
                    <p class="strong">Email</p>
                    <input bind:value={email} placeholder="name@example.com"/>
                    <p class="string">Password</p>
                    <input bind:value={password} on:keyup={passwordCheck(password)} on:change={passwordCheck(password)} type="password" placeholder="Password">
                    <p class="string">Confirm password</p>
                    <input bind:value={passwordConfirm} type="password" placeholder="Password">
                    <button type="submit">Create account</button>
                </form>
                <button on:click={() => authType = 'login'}>Login With My Account Instead</button>
            {/if}
        </div>
    </div>
</div>