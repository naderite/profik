<script>
  export let handleClick;
  export let buttonText;
</script>

<div>
  <button on:click={handleClick}>{buttonText}</button>
</div>
