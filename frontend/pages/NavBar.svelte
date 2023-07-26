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

  import styles from "./navBar.module.css";
</script>

<nav class={styles.navbar}>
  <div class="">
    <img src="logo.png" alt="logo" class={styles.logo} />
  </div>
  <ul class={styles.navbar}>
    {#each navOptions as option, index}
      <li class="">
        <Navlink {option} {selected} {changeComponent} {index} />
      </li>
    {/each}
  </ul>
</nav>

<svelte:component this={selected.component} />
