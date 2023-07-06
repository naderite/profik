<script>
  export let exercise;
  export let questions;
</script>

<main>
  <div class="exercise-container">
    <p>Enoncé:</p>
    <p>{exercise.head}</p>
  </div>

  <div class="questions-container">
    {#each questions as question}
      <div class="question">
        <p>{question.order}) {question.text}</p>
        {#if question.correction}
          <div class="correction">
            <p>Correction: {question.correction.text}</p>
          </div>
        {/if}
      </div>
    {/each}
  </div>
</main>
