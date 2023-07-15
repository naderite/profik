<script>
  import Dropdown from "../common/Dropdown.svelte";

  let hasTheorem = true;
  let hasMethods = true;
  let comments = 0;

  const theoremChoices = [
    { value: true, label: "inclus" },
    { value: false, label: "non inclus" },
  ];

  const methodsChoices = [
    { value: false, label: "Unique" },
    { value: true, label: "Multiple" },
  ];

  const commentsChoices = [
    { value: 0, label: "minimum" },
    { value: 1, label: "moyen" },
    { value: 2, label: "très explicatif" },
  ];

  export let correctionFormData = {
    hasMethods,
    hasTheorem,
    comments,
  };
</script>

<div class="form-container">
  <Dropdown
    label="Théorème:"
    options={theoremChoices}
    bind:value={correctionFormData.hasTheorem}
  />
  <Dropdown
    label="Nombre de méthodes:"
    options={methodsChoices}
    bind:value={correctionFormData.hasMethods}
  />
  <Dropdown
    label="Commentaires"
    options={commentsChoices}
    bind:value={correctionFormData.comments}
  />
</div>
