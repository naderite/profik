<script>
  import { onMount } from "svelte";
  import ResumeContainer from "../src/components/containers/Resumes.svelte";
  import PageHeadComponent from "../src/components/common/PageHead.svelte";
  import ButtonComponent from "../src/components/common/Button.svelte";

  export let courses = [];
  export let selectedCourse = null;
  let buttonClicked = false;

  onMount(async () => {
    // Fetch course options from the server
    courses = await fetchCourses();
  });

  async function fetchCourses() {
    try {
      const response = await fetch("http://localhost:8000/api/courses/");
      const data = await response.json();
      return data.courses;
    } catch (error) {
      console.error("Error while fetching course options:", error);
      return [];
    }
  }

  function handleClick(course) {
    selectedCourse = course;
    buttonClicked = true;
  }
  import styles from "./resemusPage.module.css"; // Import the CSS module
</script>

{#if !buttonClicked}
  <main class={styles.mainContainer}>
    <PageHeadComponent title="Nos Resumés" indication="Choisir une resumé" />
    <div class={styles.courseButtons}>
      {#each courses as course}
        <ButtonComponent
          handleClick={() => handleClick(course)}
          buttonText="Resumé de {course.title}"
        />
      {/each}
    </div>
  </main>
{:else}
  <ResumeContainer {selectedCourse} />
{/if}
