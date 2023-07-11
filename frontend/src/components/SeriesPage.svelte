<script>
  import SearchResult from "./SearchResult.svelte";
  export let exercises;
  export let selectedCourse;
</script>

<main>
  <h2>Exercises for {selectedCourse.title}</h2>

  {#each exercises as exercise, index}
    <p>Exercice {index + 1}</p>
    <SearchResult exercise={exercise.exercise} questions={exercise.questions} />
  {/each}
</main>
