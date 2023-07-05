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
    // Check if both exerciseFormData and correctionFormData are filled
    if (!exerciseFormData || !correctionFormData) {
      console.log("Please fill in both sections of the form");
      return;
    }

    try {
      // Construct the query parameters
      const queryParams = new URLSearchParams();
      queryParams.append("course", exerciseFormData.course);
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
      console.log(data);
      // Set the API response data to be used for rendering SearchResults component
      // Set the searchResultData to update the SearchResult component
      const exercise = data.exercise.exercise;
      const questions = data.exercise.questions || [];

      searchResultData = { exercise, questions };
      console.log(searchResultData);

      // Set formSubmitted to true to hide the generator form
      formSubmitted = true;
    } catch (error) {
      console.error("Error while submitting the form:", error);
    }
  }
</script>

{#if !formSubmitted}
  <main>
    <h2>Form Section 1</h2>
    <ExerciseForm {courseOptions} {coursePartOptions} bind:exerciseFormData />

    <h2>Form Section 2</h2>
    <CorrectionForm bind:correctionFormData />

    <button on:click={handleSubmit}>Submit</button>
  </main>
{/if}
<!-- Pass searchResultData to the SearchResult component -->
{#if searchResultData}
  <SearchResult
    exercise={searchResultData.exercise}
    questions={searchResultData.questions}
  />
{/if}
