<script>
  export let label;
  export let options;
  export let value;
  import styles from "./dropDown.module.css"; // Import the CSS module
</script>

<div class={styles.dropDownContainer}>
  <p class={styles.dropDownLabel}>{label}</p>

  <select bind:value class={styles.formSelect}>
    {#each options as option}
      <option value={option.value}>{option.label}</option>
    {/each}
  </select>
</div>
