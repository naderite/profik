<script>
  import { onMount } from "svelte";
  import SeriesPage from "./SeriesPage.svelte";
  export let courses = [];
  export let exercises = [];
  let selectedCourse = null;
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

  async function handleClick(course) {
    selectedCourse = course;
    try {
      const response = await fetch("http://localhost:8000/api/exercises/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ course_id: course.id }),
      });

      if (!response.ok) {
        throw new Error("Failed to fetch exercises");
      }

      const data = await response.json();
      exercises = data;
      buttonClicked = true;
      // Handle the received data as needed
    } catch (error) {
      console.error("Error while fetching exercises:", error);
    }
  }
</script>

{#if !buttonClicked}
  <main class="main-container">
    <h2 class="title">Nos séries</h2>
    <p class="indication">choisir une série</p>
    <div class="course-buttons">
      {#each courses as course}
        <div class="course-button">
          <button on:click={() => handleClick(course)}
            >serie sur {course.title}</button
          >
        </div>
      {/each}
    </div>
  </main>
{:else}
  <SeriesPage exercises={exercises["exercises"]} {selectedCourse} />
{/if}
