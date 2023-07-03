<script>
  import { onMount, afterUpdate } from "svelte";
  import ExerciseForm from "./ExerciseForm.svelte";
  import CorrectionForm from "./CorrectionForm.svelte";

  let courseOptions = [];
  let coursePartOptions = [];
  let courseSelected = false;
  let coursePartsFetched = false;
  let exerciseFormData = {};
  let correctionFormData = {};

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
      // Combine exerciseFormData and correctionFormData into a single object
      const formData = {
        ...exerciseFormData,
        ...correctionFormData,
      };

      // Send the form data to the API
      const response = await fetch("http://localhost:8000/api/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      // Handle the response from the API
      const data = await response.json();
      console.log("API response:", data);
    } catch (error) {
      console.error("Error while submitting the form:", error);
    }
  }
</script>

<main>
  <h2>Form Section 1</h2>
  <ExerciseForm {courseOptions} {coursePartOptions} bind:exerciseFormData />

  <h2>Form Section 2</h2>
  <CorrectionForm bind:correctionFormData />

  <button on:click={handleSubmit}>Submit</button>
</main>
