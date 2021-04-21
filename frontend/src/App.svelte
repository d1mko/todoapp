<script>
    import {Route, Router} from 'svelte-routing';
    import Home from './Home.svelte'
    import Auth from './auth/Auth.svelte'
    import Redirect from './components/Redirect.svelte'

    import { sessionEmail } from "./stores/auth";

    $: isAuth = $sessionEmail;

</script>

<Router>
    {#if !isAuth || typeof isAuth === undefined}
        <Route path="login/"><Auth/></Route>
        <Route path="*"><Redirect to="login"/></Route>
    {:else}
        <Route path="/"><Home/></Route>
    {/if}

</Router>