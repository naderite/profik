<script>
  import ButtonComponent from "../common/Button.svelte";
  import MathTextComponent from "../common/MathText.svelte";

  let activeQuestion = null;
  export let question;

  function toggleCorrection(question) {
    if (activeQuestion === question) {
      activeQuestion = null;
    } else {
      activeQuestion = question;
    }
  }
  import styles from "./correctionDropdown.module.css"; // Import the CSS module
</script>

<div class={styles.correctionContainer}>
  <button
    class={styles.correctionButton}
    on:click={() => toggleCorrection(question)}>Correction</button
  >
  {#if activeQuestion}
    <MathTextComponent latexText={question.correction.text} />
  {/if}
</div>
