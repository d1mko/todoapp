<script>
    import {Route, Router} from 'svelte-routing';
    import Home from './Home.svelte'
    import Auth from './auth/Auth.svelte'
    import Redirect from './components/Redirect.svelte'

    let isLoaded;
    let isAuth;
    $: fetch("http://localhost:8000/api/auth/authenticated", {
        credentials: 'include'
    })
        .then(res => res.json())
        .then(data => {
            isAuth = data.isAuthenticated !== 0;
            isLoaded = true;
        });


</script>

<Router>
    {#if isLoaded}
        {#if !isAuth}
            <Route path="login/"><Auth/></Route>
            <Route path="*"><Redirect to="login"/></Route>
        {:else}
            <Route path="/"><Home/></Route>
            <Route path="/login"><Redirect to="/"/></Route>
        {/if}
    {:else}
        ...Loading
    {/if}
</Router>