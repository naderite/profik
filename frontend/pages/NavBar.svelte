<script>
  import GeneratorForm from "./GeneratorPage.svelte";
  import Navlink from "../src/components/nav-bar/NavLink.svelte";
  import ProfilePage from "./ProfilePage.svelte";
  import ResumesPage from "./ResumesPage.svelte";
  import SeriesPage from "./SeriesPage.svelte";

  // Define the navigation options
  let navOptions = [
    { label: "Profile", component: ProfilePage, icon: "account_circle" },
    { label: "Exercises", component: GeneratorForm, icon: "function" },
    { label: "Séries", component: SeriesPage, icon: "library_books" },
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
