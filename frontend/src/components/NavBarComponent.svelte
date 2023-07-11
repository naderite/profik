<!-- NavBarComponent.svelte -->
<script>
  import GeneratorForm from "./GeneratorForm.svelte";
  import ProfilePage from "./ProfilePage.svelte";
  import ResumesPage from "./ResumesPage.svelte";
  import SeriesSelect from "./SeriesSelect.svelte";

  // Define the navigation options
  let navOptions = [
    { label: "Profile", component: ProfilePage },
    { label: "Exercises", component: GeneratorForm },
    { label: "Séries", component: SeriesSelect },
    { label: "Résumes", component: ResumesPage },
  ];

  // Keep track of the selected page object
  let selected = navOptions[0];

  // Change the selected component
  function changeComponent(event) {
    selected = navOptions[event.currentTarget.id];
  }
</script>

<nav>
  <div class="navbar">
    <div class="logo">
      <img src="logo.png" alt="logo" />
    </div>
    <ul class="nav nav-tabs">
      {#each navOptions as option, i}
        <li class="nav-item">
          <button
            class={selected === option ? "nav-link active" : "nav-link"}
            on:click={changeComponent}
            id={i}
          >
            {option.label}
          </button>
        </li>
      {/each}
    </ul>
  </div>
</nav>

<main>
  <svelte:component this={selected.component} />
</main>

<style>
  @import "../css/navBarComponent.css";
</style>
