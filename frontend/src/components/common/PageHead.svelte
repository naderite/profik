<script>
  export let title;
  export let indication;
  import styles from "./pageHead.module.css"; // Import the CSS module
</script>

<h2 class={styles.title}>{title}</h2>
<p class={styles.indication}>{@html indication}</p>
