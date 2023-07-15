<script>
  import { onMount, afterUpdate } from "svelte";
  import { loadMathJax } from "../../utils/mathJaxloader";

  export let latexText;

  let isTypeset = false;

  onMount(async () => {
    await loadMathJax();
    typesetMath();
  });

  afterUpdate(() => {
    if (!isTypeset) {
      typesetMath();
    }
  });

  async function typesetMath() {
    if (typeof MathJax !== "undefined" && MathJax.typesetPromise) {
      try {
        await MathJax.typesetPromise();
        isTypeset = true;
      } catch (error) {
        console.error("MathJax typesetting error:", error);
      }
    }
  }
</script>

<div>
  {@html latexText}
</div>
