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

  $: {
    if (courseSelected && !coursePartsFetched) {
      fetchCoursePartOptions()
        .then((data) => {
          coursePartOptions = data;
          coursePartsFetched = true;
        })
        .catch((error) => {
          console.error("Error while fetching course part options:", error);
        });
    }
  }

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
    formFilled = !!exerciseFormData.course && !!exerciseFormData.coursePart;
    if (!formFilled) {
      console.log("Form not filled yet");
      return;
    }

    try {
      const queryParams = new URLSearchParams();
      queryParams.append("coursePart", exerciseFormData.coursePart);
      queryParams.append("length", exerciseFormData.length);
      queryParams.append("reasoning", exerciseFormData.reasoning);
      queryParams.append("difficulty", exerciseFormData.difficulty);
      queryParams.append("hasTheorem", correctionFormData.hasTheorem);
      queryParams.append("hasMethods", correctionFormData.hasMethods);
      queryParams.append("comments", correctionFormData.comments);

      const response = await fetch(
        `http://localhost:8000/api/submit/?${queryParams}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const data = await response.json();
      const exercise = data.exercise.exercise;
      const questions = data.exercise.questions || [];

      searchResultData = { exercise, questions };
      formSubmitted = true;
    } catch (error) {
      console.error("Error while submitting the form:", error);
    }
  }
</script>

{#if !formSubmitted}
  <main class="main-container">
    <h2 class="title">Générateur des exercices personnalisés</h2>
    {#if !formFilled}
      <p class="warning">Choisir un cours et une partie de cours</p>
      <hr />
    {/if}
    <div class="form-section">
      <div class="form-column">
        <ExerciseForm
          {courseOptions}
          {coursePartOptions}
          bind:exerciseFormData
        />
      </div>
      <div class="form-column">
        <CorrectionForm bind:correctionFormData />
        <div class="button-container">
          <button id="form-submit-button" on:click={handleSubmit}
            >Générer</button
          >
        </div>
      </div>
    </div>
  </main>
{/if}

{#if searchResultData}
  <main class="main-container">
    <SearchResult
      exercise={searchResultData.exercise}
      questions={searchResultData.questions}
    />
  </main>
{/if}

<style>
  @import "../css/GeneratorForm.css";
</style>
