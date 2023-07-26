<script>
  export let selectedCourse;
  import MathTextComponent from "../common/MathText.svelte";
  import PageHeadComponent from "../common/PageHead.svelte";
  import styles from "./resumes.module.css"; // Import the CSS module
</script>

<main class={styles.mainContainer}>
  <PageHeadComponent title={selectedCourse.title} indication="" />
  <div class={styles.summaryText}>
    <MathTextComponent latexText={selectedCourse.resume} />
  </div>
</main>
