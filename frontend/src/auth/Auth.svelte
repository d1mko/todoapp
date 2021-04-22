<script>
    import {isAuthenticate, restResponseHandler} from "../shared";
    import {sessionEmail} from '../stores/auth'

    let authType = "login";
    let successMessage;
    let errorMessage;

    let email = "";
    let password = "";
    let passwordConfirm = "";

    function passwordCheck(pass) {
        let checkLower, checkUpper, checkDigits;

        checkLower = !!pass.match(/[a-z]+/);
        checkUpper = !!pass.match(/[A-Z]+/);
        checkDigits = !!pass.match(/[0-9]+/);

        return checkLower && checkUpper && checkDigits;
    }

    async function signupHandler() {

        console.log(password, email, passwordConfirm)

        if (password === '' || password === null &&
            passwordConfirm === '' || password === null &&
            email === '' || email === null){
            errorMessage = "Fill all fields";

        } else if (password !== passwordConfirm) {
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

        if (resp === 200) {
            let authenticated = await isAuthenticate();
            if (authenticated) {
                localStorage.setItem('sessionEmail', email);
                sessionEmail.update(() => localStorage.getItem('sessionEmail'));
                location.replace('/');
            }
        } else {
            errorMessage = `An error occur ${resp.statusText}`
        }
    }


</script>

<style>
    main {
        margin: 0;
        font-family: "Montserrat", sans-serif;
        font-size: 15px;
        line-height: 1.6;
        color: #333;
    }

    *,
    *:after,
    *:before {
        box-sizing: border-box;
    }

    h1, h2, h3, h4, h5, h6 {
        margin: 0;
    }

    .section {
        padding: 120px 0;
    }

    .container {
        width: 100%;
        max-width: 1230px;
        margin: 0 auto;
        padding: 15px 15px;
        justify-content: center;
    }

    .section__title {
        font-size: 30px;
        color: #333;
        font-weight: 700;
        text-transform: uppercase;
        text-align: center;
    }

    .auth {
        font-family: "Montserrat", sans-serif;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        position: relative;
    }

    .auth_form {
        padding: 30px 20px 10px;
        margin-bottom: 10px;
    }

    .notification {
        font-weight: 600;
        color: #722417;
        text-align: center;
    }

    .auth_form p {
        width: 100%;
    }

    .auth_input {
        font-family: "Montserrat", sans-serif;
        font-size: 15px;
        width: 100%;
    }

    .auth_btn {
        display: inline-block;
        vertical-align: top;
        padding: 8px 30px;
        width: 100%;

        background-color: #333333;
        border: 3px solid #fff;
        transition: background .1s linear, color .1s linear;

        text-transform: uppercase;
        text-decoration: none;
        font-size: 14px;
        font-weight: 700;
        color: #ffffff;
    }


    .auth_btn:hover {
        color: #fce38a;
        cursor: pointer;
    }
</style>

<div class="page">
    <section class="section">
        <div class="container">
            <div class="auth">
                <div>
                </div>

                <div class="auth_form">
                    {#if authType === "login"}

                        <div class="section__title">
                            <h2>Login</h2>
                        </div>


                        {#if errorMessage}
                            <div class="notification">
                                <p>{errorMessage}</p>
                            </div>
                        {/if}

                        <form on:submit|preventDefault={loginHandler}>
                            <p><input class="auth_input" bind:value={email} placeholder="email"/></p>
                            <p><input class="auth_input" bind:value={password} type="password" placeholder="password"></p>
                            <p><button class="auth_btn" type="submit">Login</button></p>
                        </form>

                        <hr/>
                        <button class="auth_btn" on:click={() => authType = 'signup'}>Create a New Account Instead</button>

                    {:else if authType === "signup"}

                        <div class="section__title">
                            <h2>Create account</h2>
                        </div>

                        {#if errorMessage}
                            <div class="notification">
                                <p>{errorMessage}</p>
                            </div>
                        {/if}

                        <form on:submit|preventDefault={signupHandler}>
                            <p><input class="auth_input" bind:value={email} placeholder="email"/></p>
                            <p><input class="auth_input" bind:value={password} on:keyup={passwordCheck(password)} type="password" placeholder="password"></p>
                            <p><input class="auth_input" bind:value={passwordConfirm} type="password" placeholder="confirm password"></p>
                            <p><button class="auth_btn" type="submit">Create account</button></p>
                        </form>
                        <button class="auth_btn" on:click={() => authType = 'login'}>Login With My Account Instead</button>
                    {/if}
                </div>

                <div>
                </div>
            </div>
        </div>
    </section>
</div>