<script>
  export let selectedCourse;
  import MathTextComponent from "../common/MathText.svelte";
  import PageHeadComponent from "../common/PageHead.svelte";
</script>

<main class="main-container">
  <PageHeadComponent title={selectedCourse.title} indication="" />
  <MathTextComponent latexText={selectedCourse.resume} />
</main>
