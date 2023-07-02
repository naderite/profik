<script>
  import { onMount } from "svelte";
  import ExerciseForm from "./ExerciseForm.svelte";
  import CorrectionForm from "./CorrectionForm.svelte";

  let courseOptions = [];
  let coursePartOptions = [];

  onMount(async () => {
    // Fetch course options from the server
    courseOptions = await fetchCourseOptions();
    coursePartOptions = await fetchCoursePartOptions();
  });

  async function fetchCourseOptions() {
    try {
      const response = await fetch("http://localhost:8000/api/courses/");
      const stream = response.body;

      const reader = stream.getReader();
      const chunks = [];

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        chunks.push(value);
      }

      const allChunks = new Uint8Array(
        chunks.reduce((acc, chunk) => acc.concat(Array.from(chunk)), [])
      );
      const data = JSON.parse(new TextDecoder().decode(allChunks));

      return data.courses;
    } catch (error) {
      console.error("Error while fetching course options:", error);
      return [];
    }
  }
  async function fetchCoursePartOptions(courseId) {
    try {
      const response = await fetch(
        `http://localhost:8000/api/course-parts/?course_id=${courseId}`
      );
      const stream = response.body;

      const reader = stream.getReader();
      const chunks = [];

      while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        chunks.push(value);
      }

      const allChunks = new Uint8Array(
        chunks.reduce((acc, chunk) => acc.concat(Array.from(chunk)), [])
      );
      const data = JSON.parse(new TextDecoder().decode(allChunks));

      return data.course_parts;
    } catch (error) {
      console.error("Error while fetching course part options:", error);
      return [];
    }
  }
</script>

<main>
  <h2>Form Section 1</h2>
  <ExerciseForm {courseOptions} {coursePartOptions} />

  <h2>Form Section 2</h2>
  <CorrectionForm />
</main>
