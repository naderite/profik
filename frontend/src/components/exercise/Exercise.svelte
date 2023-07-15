<script>
  import MathTextComponent from "../common/MathText.svelte";
  import QuestionComponent from "./Question.svelte";
  export let exercise;
  export let questions;
</script>

<div class="exercise-container">
  <p>Enoncé:</p>
  <MathTextComponent latexText={exercise.head} />
</div>

<div class="questions-container">
  {#each questions as question}
    <QuestionComponent {question} />
  {/each}
</div>
