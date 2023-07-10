<script>
  export let exercise;
  export let questions;
  let activeQuestion = null;

  function toggleCorrection(question) {
    if (activeQuestion === question) {
      activeQuestion = null;
    } else {
      activeQuestion = question;
    }
  }
</script>

<main class="main-container">
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
            <div class="correction-dropdown">
              <button on:click={() => toggleCorrection(question)}>
                Correction
              </button>
              {#if activeQuestion === question}
                <p>{question.correction.text}</p>
              {/if}
            </div>
          </div>
        {/if}
      </div>
    {/each}
  </div>
</main>

<style>
  @import "./SearchResult.css";
</style>
