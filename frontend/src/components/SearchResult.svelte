<script>
  import { onDestroy, onMount } from "svelte";
  export let exercise;
  export let questions;
  let activeQuestion = null;
  let mathJaxLoaded = null;

  function toggleCorrection(question) {
    if (activeQuestion === question) {
      activeQuestion = null;
    } else {
      activeQuestion = question;
    }
  }

  function loadMathJax() {
    if (!mathJaxLoaded) {
      mathJaxLoaded = new Promise((resolve, reject) => {
        MathJax.startup.promise = MathJax.startup.promise
          .then(() => {
            resolve();
          })
          .catch((error) => {
            mathJaxLoaded = false; // Reset the flag in case of an error
            reject(error);
          });
        MathJax.startup.defaultReady();
      });
    }
    return mathJaxLoaded;
  }

  onMount(async () => {
    await loadMathJax(); // Ensure MathJax is loaded before rendering equations
  });

  onDestroy(() => {
    mathJaxLoaded = false; // Reset the flag
    if (typeof MathJax.startup.defaultShutdown === "function") {
      MathJax.startup.defaultShutdown();
    }
  });
</script>

<svelte:head>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script
    id="MathJax-script"
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"
  ></script>
</svelte:head>
<div class="exercise-container">
  <p>Enoncé:</p>
  <p>{exercise.head}</p>
</div>

<div class="questions-container">
  {#each questions as question}
    <div class="question">
      <p>{question.order}) {question.text}</p>
      {#if question.correction}
        <div class="correction">
          <div class="correction-dropdown">
            <button on:click={() => toggleCorrection(question)}>
              Correction
            </button>
            {#if activeQuestion === question}
              <p>{question.correction.text}</p>
            {/if}
          </div>
        </div>
      {/if}
    </div>
  {/each}
</div>
