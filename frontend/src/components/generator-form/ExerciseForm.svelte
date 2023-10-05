<script>
  import { afterUpdate } from "svelte";
  import DropdownComponent from "../common/Dropdown.svelte";

  export let courseOptions;
  export let coursePartOptions;

  let level = "bac tech";
  let course = null;
  let coursePart = null;
  let length = 0;
  let difficulty = 0;

  const levelChoices = [
    { value: "bac tech", label: "Bac technique" },
    { value: "bac SC", label: "Bac science" },
    { value: "bac math", label: "Bac mathématique" },
  ];

  const lengthChoices = [
    { value: 0, label: "court" },
    { value: 1, label: "long" },
    { value: 2, label: "probleme" },
  ];

  const difficultyChoices = [
    { value: 0, label: "facile" },
    { value: 1, label: "moyen" },
    { value: 2, label: "difficile" },
  ];

  function filterCourseParts(courseParts, courseId) {
    return courseId
      ? courseParts.filter((part) => part.course === courseId)
      : [];
  }

  export let exerciseFormData;

  afterUpdate(() => {
    exerciseFormData = {
      level,
      course,
      coursePart,
      length,
      difficulty,
    };
  });

  import styles from "./form.module.css"; // Import the CSS module
</script>

<div class={styles.formContainer}>
  <p class={styles.indication}>Choisir l'exercice suivant:</p>
  <DropdownComponent
    label="Votre niveau d'étude:"
    options={levelChoices}
    bind:value={level}
  />
  <!--refused to work with dropdown component-->
  <div class={styles.dropDownContainer}>
    <p class={styles.dropDownLabel}>Le cours:</p>

    <select bind:value={course} class={styles.formSelect}>
      {#each courseOptions as option}
        <option value={option.id}>{option.title}</option>
      {/each}
    </select>
  </div>

  <div class={styles.dropDownContainer}>
    <!--refused to work with dropdown component-->
    <p class={styles.dropDownLabel}>La partie de cours:</p>

    <select bind:value={coursePart} class={styles.formSelect}>
      {#if course}
        {#each filterCourseParts(coursePartOptions, course) as option}
          <option value={option.id}>{option.title}</option>
        {/each}
      {:else}
        <option value={null}>Selectionner un cours avant</option>
      {/if}
    </select>
  </div>

  <DropdownComponent
    label="La longueur:"
    options={lengthChoices}
    bind:value={length}
  />

  <DropdownComponent
    label="La difficulté de l'exercice:"
    options={difficultyChoices}
    bind:value={difficulty}
  />
</div>
