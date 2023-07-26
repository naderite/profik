<script>
  import MathTextComponent from "../common/MathText.svelte";
  import QuestionComponent from "./Question.svelte";
  export let exercise;
  export let questions;
  import styles from "./exercise.module.css"; // Import the CSS module
</script>

<div class={styles.exerciseContainer}>
  <h3>Enoncé:</h3>
  <MathTextComponent latexText={exercise.head} />
</div>

{#each questions as question}
  <QuestionComponent {question} />
{/each}
