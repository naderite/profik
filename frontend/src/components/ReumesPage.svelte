<script>
  export let selectedCourse;
  import { onDestroy, onMount } from "svelte";

  let mathJaxLoaded = null;
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
  <script type="text/javascript">
    MathJax = { tex: { debug: true } };
  </script>

  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script
    id="MathJax-script"
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"
  ></script>
</svelte:head>

<main class="main-container">
  <h1 class="title">{selectedCourse.title}</h1>
  {@html selectedCourse.resume}
</main>

<style>
  @import "../css/app.css";
</style>
