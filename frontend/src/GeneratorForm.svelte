<script>
  import { onMount, afterUpdate } from "svelte";
  import ExerciseForm from "./ExerciseForm.svelte";
  import CorrectionForm from "./CorrectionForm.svelte";
  import SearchResult from "./SearchResult.svelte";

  let courseOptions = [];
  let coursePartOptions = [];
  let courseSelected = false;
  let coursePartsFetched = false;
  let exerciseFormData = {};
  let correctionFormData = {};
  let searchResultData = null;
  let formSubmitted = false;
  let formFilled = true;
  onMount(async () => {
    // Fetch course options from the server
    courseOptions = await fetchCourseOptions();
  });

  // Fetch course part options whenever the course value changes
  afterUpdate(async () => {
    if (courseSelected && !coursePartsFetched) {
      coursePartOptions = await fetchCoursePartOptions();
      coursePartsFetched = true;
    }
  });

  async function fetchCourseOptions() {
    try {
      const response = await fetch("http://localhost:8000/api/courses/");
      const data = await response.json();
      courseSelected = true;
      return data.courses;
    } catch (error) {
      console.error("Error while fetching course options:", error);
      return [];
    }
  }

  async function fetchCoursePartOptions() {
    try {
      const response = await fetch("http://localhost:8000/api/course-parts/");
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error while fetching course part options:", error);
      return [];
    }
  }

  async function handleSubmit() {
    // Check if exerciseFormData is filled
    if (!exerciseFormData.course || !exerciseFormData.coursePart) {
      formFilled = false;
      console.log("form not filled yet");
      return;
    }

    try {
      formFilled = true;
      // Construct the query parameters
      const queryParams = new URLSearchParams();
      queryParams.append("coursePart", exerciseFormData.coursePart);
      queryParams.append("length", exerciseFormData.length);
      queryParams.append("reasoning", exerciseFormData.reasoning);
      queryParams.append("difficulty", exerciseFormData.difficulty);
      queryParams.append("hasTheorem", correctionFormData.hasTheorem);
      queryParams.append("hasMethods", correctionFormData.hasMethods);
      queryParams.append("comments", correctionFormData.comments);

      // Send the request to the API
      const response = await fetch(
        `http://localhost:8000/api/submit/?${queryParams}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      // Handle the response from the API
      const data = await response.json();

      // Set the searchResultData to update the SearchResult component
      const exercise = data.exercise.exercise;
      const questions = data.exercise.questions || [];

      searchResultData = { exercise, questions };

      // Set formSubmitted to true to hide the generator form
      formSubmitted = true;
    } catch (error) {
      console.error("Error while submitting the form:", error);
    }
  }
</script>

{#if formFilled}
  {#if !formSubmitted}
    <main class="main-container">
      <h2 class="title">Générateur des exercices personalisés</h2>
      <p class="indication">
        Cliquer sur les menus pour specifier l'exercice puis cliquer sur
        "Générer" pour voir l'exercice
      </p>
      <ExerciseForm {courseOptions} {coursePartOptions} bind:exerciseFormData />

      <CorrectionForm bind:correctionFormData />

      <button id="form-submit-button" on:click={handleSubmit}>Submit</button>
    </main>
  {/if}
{:else}
  <main class="main-container">
    <h2 class="title">Générateur des exercices personalisés</h2>
    <p class="warning">choisir un cours et un partie de cours</p>
    <hr />
    <ExerciseForm {courseOptions} {coursePartOptions} bind:exerciseFormData />
    <CorrectionForm bind:correctionFormData />

    <button id="form-submit-button" on:click={handleSubmit}>Générer</button>
  </main>
{/if}

<!-- Pass searchResultData to the SearchResult component -->
{#if searchResultData}
  <SearchResult
    exercise={searchResultData.exercise}
    questions={searchResultData.questions}
  />
{/if}

<style>
  @import "./GeneratorForm.css";
</style>
