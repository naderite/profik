<script>
  import ExerciseComponent from "../Exercise/Exercise.svelte";
  import PageHeadComponent from "../common/PageHead.svelte";

  export let exercises;
  export let selectedCourse;
</script>

<main class="main-container">
  <PageHeadComponent
    title="Exercises for {selectedCourse.title}"
    indication=""
  />
  {#each exercises as exercise, index}
    <p>Exercice {index + 1}</p>
    <ExerciseComponent
      exercise={exercise.exercise}
      questions={exercise.questions}
    />
  {/each}
</main>
