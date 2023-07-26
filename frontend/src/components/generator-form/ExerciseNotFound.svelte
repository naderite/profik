<script>
  import styles from "./exerciseNotFound.module.css"; // Import the CSS module
</script>

<div class={styles.errorContainer}>
  <h3 class={styles.errorTitle}>EXERCICE N'EXISTE PAS!!</h3>
  <p class={styles.errorMessage}>
    L'exercice que vous avez demandé est introuvable.
  </p>
  <button class={styles.closeButton} on:click>Fermer</button>
</div>
