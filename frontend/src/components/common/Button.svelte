<script>
  export let handleClick;
  export let buttonText;
  import styles from "./button.module.css"; // Import the CSS module
</script>

<button class={styles.button} on:click={handleClick}>{buttonText}</button>
