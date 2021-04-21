import {writable} from "svelte/store";

export const sessionEmail = writable(localStorage.getItem('sessionEmail'));