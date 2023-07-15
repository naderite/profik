<script>
  export let option;
  export let changeComponent;
  export let selected;
  export let index;
</script>

<button
  class={selected === option ? "nav-link active" : "nav-link"}
  on:click={changeComponent}
  id={index}
>
  <i class="logo material-symbols-outlined">
    {option.icon}
  </i>
  {option.label}
</button>
