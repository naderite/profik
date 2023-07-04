<script>
  import { afterUpdate } from "svelte";

  let hasTheorem = true;
  let hasMethods = true;
  let comments = 0;

  const THEOREM_CHOICES = [
    { value: true, label: "inclus" },
    { value: false, label: "non inclus" },
  ];

  const METHODS_CHOICES = [
    { value: false, label: "Unique" },
    { value: true, label: "Multiple" },
  ];

  const COMMENT_CHOICES = [
    { value: 0, label: "minimum" },
    { value: 1, label: "moyen" },
    { value: 2, label: "très explicatif" },
  ];

  export let correctionFormData;

  afterUpdate(async () => {
    correctionFormData = {
      hasMethods,
      hasTheorem,
      comments,
    };
  });
</script>

<div>
  <label>
    Théorème
    <select bind:value={hasTheorem}>
      {#each THEOREM_CHOICES as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>

  <label>
    Nombre de méthodes
    <select bind:value={hasMethods}>
      {#each METHODS_CHOICES as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>

  <label>
    Commentaires
    <select bind:value={comments}>
      {#each COMMENT_CHOICES as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>
</div>
