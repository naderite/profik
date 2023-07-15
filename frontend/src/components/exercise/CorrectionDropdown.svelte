<script>
  import ButtonComponent from "../common/Button.svelte";
  import MathTextComponent from "../common/MathText.svelte";

  let activeQuestion = null;
  export let question;

  function toggleCorrection(question) {
    if (activeQuestion === question) {
      activeQuestion = null;
    } else {
      activeQuestion = question;
    }
  }
</script>

<div>
  <ButtonComponent
    handleClick={() => toggleCorrection(question)}
    buttonText="Correction"
  />
  {#if activeQuestion}
    <MathTextComponent latexText={question.correction.text} />
  {/if}
</div>
