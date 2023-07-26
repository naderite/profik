<script>
  export let option;
  export let changeComponent;
  export let selected;
  export let index;
  import styles from "./navLink.module.css"; // Import the CSS module
</script>

<div class={styles.navlink}>
  <button
    on:click={changeComponent}
    id={index}
    class={selected === option ? styles.active : styles.nonActive}
  >
    <i class="logo material-symbols-outlined text-xl">{option.icon}</i>
    <span class="">{option.label}</span>
  </button>
</div>
