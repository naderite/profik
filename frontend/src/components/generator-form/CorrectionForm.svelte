<script>
  import Dropdown from "../common/Dropdown.svelte";

  let hasTheorem = true;
  let hasMethods = true;
  let comments = 0;

  const theoremChoices = [
    { value: true, label: "inclus" },
    { value: false, label: "non inclus" },
  ];

  const commentsChoices = [
    { value: 0, label: "minimum" },
    { value: 1, label: "moyen" },
    { value: 2, label: "très explicatif" },
  ];

  export let correctionFormData = {
    hasTheorem,
    comments,
  };

  import styles from "./form.module.css"; // Import the CSS module
</script>

<p class={styles.indication}>Choisir la correction suivant:</p>

<Dropdown
  label="Théorème:"
  options={theoremChoices}
  bind:value={correctionFormData.hasTheorem}
/>
<Dropdown
  label="Commentaires"
  options={commentsChoices}
  bind:value={correctionFormData.comments}
/>
