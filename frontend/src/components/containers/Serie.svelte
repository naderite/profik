<script>
  import ExerciseComponent from "../Exercise/Exercise.svelte";
  import PageHeadComponent from "../common/PageHead.svelte";

  export let exercises;
  export let selectedCourse;
  import styles from "./serie.module.css"; // Import the CSS module
</script>

<main class={styles.mainContainer}>
  <PageHeadComponent
    title="Exercises for {selectedCourse.title}"
    indication=""
  />
  {#each exercises as exercise, index}
    <h2 class={styles.exerciseTitle}>Exercice {index + 1}</h2>
    <ExerciseComponent
      exercise={exercise.exercise}
      questions={exercise.questions}
    />
  {/each}
</main>
