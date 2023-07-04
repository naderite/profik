<script>
  import { afterUpdate } from "svelte";

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
    { value: 1, label: "aléatoire" },
    { value: 2, label: "récurrence" },
    { value: 3, label: "absurd" },
  ];

  function filterCourseParts(courseParts, courseId) {
    if (!courseId) {
      // If courseId is not provided, return an empty array
      return [];
    }

    // Filter course parts based on the courseId
    return courseParts.filter((part) => part.course === courseId);
  }

  export let exerciseFormData;
  afterUpdate(async () => {
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

<div>
  <label>
    la Difficulté de l'exercice:
    <select bind:value={level}>
      {#each levelChoices as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>

  <label>
    Le cours:
    <select bind:value={course}>
      {#each courseOptions as option}
        <option value={option.id}>{option.title}</option>
      {/each}
    </select>
  </label>

  <label>
    La partie de cours:
    <select bind:value={coursePart}>
      {#if course}
        {#each filterCourseParts(coursePartOptions, course) as option}
          <option value={option.id}>{option.title}</option>
        {/each}
      {:else}
        <option value={null}>Select a course first</option>
      {/if}
    </select>
  </label>

  <label>
    La longueur:
    <select bind:value={length}>
      {#each lengthChoices as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>

  <label>
    Le raisonnement:
    <select bind:value={reasoning}>
      {#each reasoningChoices as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>

  <label>
    Difficulté de l'exercice:
    <select bind:value={difficulty}>
      {#each difficultyChoices as choice}
        <option value={choice.value}>{choice.label}</option>
      {/each}
    </select>
  </label>
</div>
