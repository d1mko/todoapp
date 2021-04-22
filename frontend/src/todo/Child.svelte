<script>
    import {getCSRF} from "../shared";

    export let removeFn;
    export let child;

    let remove = false;
    const confirmText = `Do you really remove TODO: ${child.id}`

</script>

<style>
    button {
        display: inline-block;
        border: none;

        background-color: #333333;
        color: #ffffff;
        text-transform: uppercase;
        font-size: 14px;
        font-family: "Montserrat", sans-serif;

        transition: color .1s linear;
    }


    button:hover {
        color: #fce38a;
        cursor: pointer;
    }

    .child {
        padding: 15px 15px 15px 60px;
        font-size: 14px;
        display: block;

    }

    .child__inner {
        display: block;
        justify-content: space-between;
        align-items: center;
    }

    .child__remove {
        display: inline-block;
        width: 10%;
    }

    .child__title {
        display: inline-block;
        width: 85%;
    }

    .child__title textarea {
        resize: none;
        width: 100%;
    }
</style>

<article>
    <div class="child">
        <div class="child__inner">
            <div class="child__title">
                <textarea readonly>{child.content}</textarea>
            </div>
            <div class="child__remove">
                <form on:submit|preventDefault={() => remove = true}>
                    <button type="submit">Delete</button>
                </form>
            </div>

            {#if remove}
            <div class="confirm-delete">
                <form on:submit|preventDefault={removeFn}>
                    <textarea readonly>{confirmText}</textarea>
                    <button type="submit">Yes</button>
                    <button on:click={ () => remove = false} type="reset">Cancel</button>
                </form>
            </div>
                {/if}
        </div>
    </div>
</article>

