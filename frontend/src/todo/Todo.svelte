<script>
    import {getCSRF} from "../shared";
    import Child from './Child.svelte';

    export let deleteFn;
    export let deleteChildFn;
    export let update;
    export let todo;
    export let i;

    let show = false;
    let remove = false;
    let content;
    const confirmText = `Do you really remove TODO: ${todo.id}?`

    async function addChild() {
        const csrf = await getCSRF();

        let todoId = todo.id;
        const request = await fetch(`http://localhost:8000/api/${todoId}/replies/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-CSRFToken": csrf,
            },
            credentials: "include",
            body: JSON.stringify({
                "content": content,
                "color": '#ffffff',
            })
        }).then(res => res.json())
            .then(data => console.log(data));

        await update();
    }
</script>

<style>
    article {
        position: relative;
        padding: 0 0 0 2em;
        border-bottom: 1px solid #eee;
    }

    h2 {
        font-size: 1em;
        margin: 0.5em 0;
    }

    span {
        position: absolute;
        left: 0;
    }

    a {
        color: #333;
    }

    .todo__inner {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .todo__add-child {
        display: inline-block;
    }

    .todo__remove {
        display: inline-block;
        width: 10%;
    }

    .todo__title {
        display: inline-block;
        width: 85%;
    }

    .todo__title textarea {
        resize: none;
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

    .todo__add-child button {
        padding: 10px;
    }

    .todo {
        padding: 15px;
    }

    .add_child {
        position: relative;
        display: flex;
        width: 90%;
        padding-top: 15px;
        padding-left: 60px;


    }

    .add_child form, .form__inner .left, .add_text {
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

    .left {
        display: inline-block;
    }

    .right {
        display: inline-block;
        position: relative;
        float: right;
        vertical-align: center;
    }

    .confirm-delete {
        float: right;
    }

    .confirm-delete textarea{
        resize: none;
    }
</style>

<article>
    <div class="todo" style="background-color: {todo.color}">
        <div class="todo__inner">
            <div class="todo__add-child">
                <button on:click={ () => show = !show }>+</button>
            </div>
            <div class="todo__title">
                <textarea readonly>{todo.content}</textarea>
            </div>
            <div class="todo__remove">
                <form on:submit|preventDefault={ () => remove = true}>
                    <button type="submit">Delete</button>
                </form>
            </div>
        </div>
    </div>

    {#if remove}
        <div class="confirm-delete">
            <form on:submit|preventDefault={deleteFn}>
                <textarea readonly>{confirmText}</textarea>
                <button on:click={remove = false} type="submit">Yes</button>
                <button on:click={ () => remove = false} type="reset">Cancel</button>
            </form>
        </div>
    {/if}

    {#if show}
        <div class="add_child">
            <form on:submit|preventDefault={addChild}>
                <div class="form__inner">
                    <div class="left">
                        <textarea class="add_text" bind:value={content}></textarea>
                    </div>
                    <div class="right">
                        <button on:click={show = false} type="submit">Add todo</button>
                        <button on:click={ () => { show = !show; content = ''; }}>Cancel</button>
                    </div>
                </div>
            </form>
        </div>
    {/if}


    <div class="replies">
        {#if todo.children}
            {#each todo.children as child}
                <Child removeFn={async () => await deleteChildFn(child)} {child}/>
            {/each}
        {/if}
    </div>

</article>
