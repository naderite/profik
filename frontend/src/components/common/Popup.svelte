<script>
  export let messageComponent;
  import styles from "./popup.module.css"; // Import the CSS module
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div on:click|self class={styles.container}>
  <div class={styles.content}>
    <svelte:component this={messageComponent} on:click />
  </div>
</div>
