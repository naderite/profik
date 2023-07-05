<script>
  export let exercise;
  export let questions;
</script>

<main>
  <h2>Search Results</h2>
  <div>
    <p>Enoncé:</p>
    <p>{exercise.head}</p>
  </div>

  <div>
    <p>Questions:</p>
    {#each questions as question}
      <div>
        <p>{question.order}</p>
        <p>Text: {question.text}</p>
        {#if question.correction}
          <div>
            <p>Correction:</p>
            <p>Text: {question.correction.text}</p>

            <hr />
          </div>
        {/if}
      </div>
    {/each}
  </div>
</main>
