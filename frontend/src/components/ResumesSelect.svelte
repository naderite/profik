<script>
  import { onMount } from "svelte";
  import ReumesPage from "./ReumesPage.svelte";
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
</script>

{#if !buttonClicked}
  <main class="main-container">
    <h2 class="title">Nos resumés</h2>
    <p class="indication">choisir une resumé</p>
    <div class="course-buttons">
      {#each courses as course}
        <div class="course-button">
          <button on:click={() => handleClick(course)}
            >resumé de {course.title}</button
          >
        </div>
      {/each}
    </div>
  </main>
{:else}
  <ReumesPage {selectedCourse} />
{/if}
