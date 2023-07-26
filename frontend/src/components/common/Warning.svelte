<script>
  export let warningMessage;
  import styles from "./warning.module.css"; // Import the CSS module
</script>

<p class={styles.warning}>{warningMessage}</p>
