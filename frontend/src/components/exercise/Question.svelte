<script>
  import CorrectionDropdown from "./CorrectionDropdown.svelte";

  export let question;
</script>

<div>
  <p>{question.order}) {question.text}</p>
  {#if question.correction}
    <CorrectionDropdown {question} />
  {/if}
</div>
