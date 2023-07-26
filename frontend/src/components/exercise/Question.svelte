<script>
  import MathText from "../common/MathText.svelte";
  import CorrectionDropdown from "./CorrectionDropdown.svelte";

  export let question;
  import styles from "./question.module.css"; // Import the CSS module
  let questionHead = question.order + ") " + question.text;
</script>

<div class={styles.questionContainer}>
  <MathText latexText={questionHead} />
  {#if question.correction}
    <CorrectionDropdown {question} />
  {/if}
</div>
