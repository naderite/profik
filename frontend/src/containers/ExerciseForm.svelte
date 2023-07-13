<script>
  import { afterUpdate } from "svelte";
  import Dropdown from "../components/common/Dropdown.svelte";

  export let courseOptions;
  export let coursePartOptions;

  let level = "bac tech";
  let course = null;
  let coursePart = null;
  let length = 0;
  let reasoning = 0;
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

  const reasoningChoices = [
    { value: 0, label: "normal" },
    { value: 1, label: "récurrence" },
    { value: 2, label: "absurd" },
    { value: 3, label: "aléatoire" },
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
      reasoning,
      difficulty,
    };
  });
</script>

<div class="form-container">
  <Dropdown
    label="la Difficulté de l'exercice:"
    options={levelChoices}
    bind:value={level}
  />
  <!--refused to work with dropdown component-->
  <label>
    Le cours:
    <select bind:value={course}>
      {#each courseOptions as option}
        <option value={option.id}>{option.title}</option>
      {/each}
    </select>
  </label>
  <!--refused to work with dropdown component-->
  <label>
    La partie de cours:
    <select bind:value={coursePart}>
      {#if course}
        {#each filterCourseParts(coursePartOptions, course) as option}
          <option value={option.id}>{option.title}</option>
        {/each}
      {:else}
        <option value={null}>Selectionner un cours avant</option>
      {/if}
    </select>
  </label>

  <Dropdown label="La longueur:" options={lengthChoices} bind:value={length} />

  <Dropdown
    label="Le raisonnement:"
    options={reasoningChoices}
    bind:value={reasoning}
  />

  <Dropdown
    label="La difficulté de l'exercice:"
    options={difficultyChoices}
    bind:value={difficulty}
  />
</div>
