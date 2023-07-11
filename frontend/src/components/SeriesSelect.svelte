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
      console.log(exercises);
      console.log(typeof exercises);
      buttonClicked = true;
      // Handle the received data as needed
    } catch (error) {
      console.error("Error while fetching exercises:", error);
    }
  }
</script>

<main>
  {#if !buttonClicked}
    <h2>Series Page</h2>
    <div class="course-buttons">
      {#each courses as course}
        <button on:click={() => handleClick(course)}
          >serie sur {course.title}</button
        >
      {/each}
    </div>
  {:else}
    <SeriesPage exercises={exercises["exercises"]} {selectedCourse} />
  {/if}
</main>

<style>
  .course-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  button {
    padding: 10px;
    background-color: var(--button-background-color);
    color: var(--button-text-color);
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
</style>
