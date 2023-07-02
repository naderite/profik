<script>
  import { onMount } from "svelte";
  import ExerciseForm from "./ExerciseForm.svelte";
  import CorrectionForm from "./CorrectionForm.svelte";

  let courseOptions = [];
  let coursePartOptions = [];

  onMount(async () => {
    // Fetch course and course part options from the server
    courseOptions = await fetchCourseOptions();
    coursePartOptions = await fetchCoursePartOptions();
  });

  async function fetchCourseOptions() {
    // Implement logic to fetch course options from the server
    // Return the options as an array
    // Example: return [{ id: 1, name: 'Course 1' }, { id: 2, name: 'Course 2' }]
  }

  async function fetchCoursePartOptions() {
    // Implement logic to fetch course part options from the server
    // Return the options as an array
    // Example: return [{ id: 1, name: 'Part 1' }, { id: 2, name: 'Part 2' }]
  }
</script>

<main>
  <h2>Form Section 1</h2>
  <ExerciseForm {courseOptions} {coursePartOptions} />

  <h2>Form Section 2</h2>
  <CorrectionForm />
</main>
