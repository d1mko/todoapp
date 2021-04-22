<script>
    import Todo from './Todo.svelte';
    import Logout from '../auth/Logout.svelte'
    import {sessionEmail} from "../stores/auth";
    import {getCSRF} from "../shared";
    import {onMount} from "svelte";

    let content;
    let color = '#ffffff';
    let show = false;
    let email;
    let todos;
    let colours = [
        '#6aa84f', '#ffffff', "#f9cb9c", "#6fa8dc"
    ]

    const unsubscribe = sessionEmail.subscribe(value => {
        email = value;
    });

    onMount(async () => await updateTodo())

    async function updateTodo() {
        await fetch('http://localhost:8000/api/', {
            method: 'GET',
            credentials: 'include'
        })
            .then(res => res.json())
            .then(data => {
                todos = data
                window.scrollTo(0, 0);
            });
    }

    async function createNewTodo(content, color, parent_id = null) {
        const csrf = await getCSRF();
        if (!color in colours) {
            color = '#ffffff';
        }

        let url;

        if (parent_id) {
            url = `http://localhost:8000/api/${parent_id}/replies`;
        } else {
            url = 'http://localhost:8000/api/';
        }

        let new_todo;
        const request = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-CSRFToken": csrf,
            },
            credentials: "include",
            body: JSON.stringify({
                "content": content,
                "color": color,
            })
        }).then(res => res.json())
            .then(data => new_todo = data);

        await updateTodo();
    }

    async function deleteTodo(deletedTodo) {
        const csrf = await getCSRF();
        const todo_id = deletedTodo.id;

        const request = (await fetch(`http://localhost:8000/api/${todo_id}/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-CSRFToken": csrf,
            },
            credentials: "include"
        })).status

        await updateTodo();
    }

</script>

<style>
    .loading {
        opacity: 0;
        animation: 0.4s 0.8s forwards fade-in;
    }

    @keyframes fade-in {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    .header {
        width: 100%;

        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;

        padding: 10px 0;
    }

    .header__inner {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .nav {
        font-size: 16px;
        text-transform: uppercase;
        width: 100%;
    }


    button {
        display: inline-block;
        border: none;

        background-color: #333333;
        color: #ffffff;
        text-transform: uppercase;
        font-size: 17px;
        font-family: "Montserrat", sans-serif;

        transition: color .1s linear;
    }

    button:hover {
        color: #fce38a;
        cursor: pointer;
    }

    .nav__link {
        display: inline-block;
        vertical-align: center;
        margin: 0 15px;
        position: relative;

        color: #333333;
        text-decoration: none;

        transition: color .1s linear;
    }

    .section {
        padding: 70px 0;
    }

    .container {
        width: 100%;
        max-width: 1230px;
        margin: 0 auto;
        padding: 15px 15px;
        justify-content: center;
    }

    .left {
        display: inline-block;
    }

    .right {
        display: inline-block;
        position: relative;
        float: right;
        vertical-align: center;
    }

    .add_form {
        position: relative;
        display: flex;
        width: 100%;
    }

    .add_form form, .form__inner .left, .add_text {
        width: 100%;
    }

    .form__inner {
        justify-content: space-between;
        align-content: center;
    }

    .form__inner .left textarea {
        resize: none;
        width: 100%;
    }
</style>


<header class="header">
    <div class="container">
        <div class="header__inner">
            <nav class="nav">
                <div class="left">
                    <button on:click={() => show = !show } id="add_todo_btn">Add Todo</button>
                </div>
                <div class="right">
                    <a class="nav__link" href="#">Hello, {email}</a>
                    <Logout/>
                </div>
            </nav>
        </div>
    </div>
</header>

<div class="section">
    <div class="container">
        {#if show}
            <div class="add_todo">
                <div class="add_title">
                    <h2>Add todo</h2>
                </div>

                <div class="add_form">
                    <form on:submit|preventDefault={ () => {show=false; createNewTodo(content, color);} }>
                        <div class="form__inner">
                            <div class="left">
                                <textarea class="add_text" bind:value={content}></textarea>
                            </div>
                            <div class="right">
                                <input bind:value={color} type="color" style="height: 50px" list="colors">
                                <datalist id="colors">
                                    <option>#6aa84f</option>
                                    <option>#ffffff</option>
                                    <option>#f9cb9c</option>
                                    <option>#6fa8dc</option>
                                </datalist>
                                <button type="submit">Add todo</button>
                                <button on:click={() => { show = false; content = ''; }}>Cancel</button>
                            </div>
                        </div>
                    </form>
                </div>

            </div>
        {/if}

        <div class="todos">
            <h2>Your todos</h2>
            {#if todos}
                {#each todos as todo, i}
                    <Todo deleteFn={ async () => await deleteTodo(todo)}
                          deleteChildFn="{deleteTodo}"
                          update="{updateTodo}"
                          {i}
                          {todo}/>
                {/each}
            {:else}
                ...Loading
            {/if}
        </div>
    </div>
</div>