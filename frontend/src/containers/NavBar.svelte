<script>
  import GeneratorForm from "../components/GeneratorForm.svelte";
  import Navlink from "../components/NavBar/Navlink.svelte";
  import ProfilePage from "../components/ProfilePage.svelte";
  import ResumesPage from "../components/ResumesSelect.svelte";
  import SeriesSelect from "../components/SeriesSelect.svelte";

  // Define the navigation options
  let navOptions = [
    { label: "Profile", component: ProfilePage, icon: "account_circle" },
    { label: "Exercises", component: GeneratorForm, icon: "function" },
    { label: "Séries", component: SeriesSelect, icon: "library_books" },
    { label: "Résumes", component: ResumesPage, icon: "book" },
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
      {#each navOptions as option, index}
        <li>
          <Navlink {option} {selected} {changeComponent} {index} />
        </li>
      {/each}
    </ul>
  </div>
</nav>

<main>
  <svelte:component this={selected.component} />
</main>
