<script>
  import { onMount } from "svelte";
  import ExerciseForm from "../src/components/generator-form/ExerciseForm.svelte";
  import CorrectionForm from "../src/components/generator-form/CorrectionForm.svelte";
  import ExerciseComponent from "../src/components/Exercise/Exercise.svelte";
  import ExerciseNotFoundPopup from "../src/components/generator-form/ExerciseNotFound.svelte";
  import PopupComponent from "../src/components/common/Popup.svelte";
  import WarningComponent from "../src/components/common/Warning.svelte";
  import ButtonComponent from "../src/components/common/Button.svelte";
  import PageHeadComponent from "../src/components/common/PageHead.svelte";
  // initialise modal state and content
  let errorComponent = ExerciseNotFoundPopup;

  // pass in component as parameter and toggle modal state
  function showPopup() {
    errorComponent = ExerciseNotFoundPopup;
    showErrorPopup = !showErrorPopup;
  }

  let showErrorPopup = false;
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
      const response = await fetch(
        "https://5f81-102-157-246-13.ngrok-free.app/api/courses/",
        {
          headers: {
            "ngrok-skip-browser-warning": "true",
          },
        }
      );
      console.log(response);
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
      const response = await fetch(
        "https://5f81-102-157-246-13.ngrok-free.app/api/course-parts/",
        {
          headers: {
            "ngrok-skip-browser-warning": "true",
            // You can add more headers here if needed
          },
        }
      );
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
      queryParams.append("level", exerciseFormData.level);
      queryParams.append("coursePart", exerciseFormData.coursePart);
      queryParams.append("length", exerciseFormData.length);
      queryParams.append("reasoning", exerciseFormData.reasoning);
      queryParams.append("difficulty", exerciseFormData.difficulty);
      queryParams.append("hasTheorem", correctionFormData.hasTheorem);
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
      if (data.error) {
        showErrorPopup = true;
        console.error("Invalid response data structure:", data);
      } else {
        const exercise = data.exercise.exercise;
        const questions = data.exercise.questions || [];

        searchResultData = { exercise, questions };
        formSubmitted = true;
      }
    } catch (error) {
      console.error("Error while submitting the form:", error);
      showErrorPopup = true;
    }
  }

  import styles from "./GeneratorPage.module.css"; // Import the CSS module
  let indication =
    "Cliquer sur les menus pour specifier l'exercice puis cliquer sur le button  <span style='font-weight: bold;'>\"Génerer\"</span> pour voir l'exercice";
</script>

{#if !formSubmitted}
  <main class={styles.mainContainer}>
    <PageHeadComponent title="Génerateur des exercices" {indication} />
    {#if !formFilled}
      <WarningComponent
        warningMessage="Choisir un cours et une partie de cours"
      />
      <hr />
    {/if}
    <div class={styles.formSection}>
      <ExerciseForm {courseOptions} {coursePartOptions} bind:exerciseFormData />
      <div class={styles.correctionForm}>
        <CorrectionForm bind:correctionFormData />
        <ButtonComponent handleClick={handleSubmit} buttonText="Génerer" />
      </div>
    </div>
  </main>
{/if}

{#if searchResultData}
  <main class={styles.mainContainer}>
    <ExerciseComponent
      exercise={searchResultData.exercise}
      questions={searchResultData.questions}
    />
  </main>
{/if}
{#if showErrorPopup}
  <PopupComponent on:click={showPopup} messageComponent={errorComponent} />
{/if}
