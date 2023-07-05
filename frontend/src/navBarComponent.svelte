<script>
  import { onMount } from "svelte";

  import GeneratorForm from "./GeneratorForm.svelte";
  import ProfilePage from "./ProfilePage.svelte";
  import ResumesPage from "./ResumesPage.svelte";

  let activePage = "Generator";

  // Set the active page based on the URL path
  onMount(() => {
    const currentPath = window.location.pathname;
    setActivePageFromPath(currentPath);
  });

  function setActivePage(page) {
    activePage = page;
  }

  function setActivePageFromPath(path) {
    // Extract the page name from the path
    const page = path.substring(1); // Remove leading '/'
    setActivePage(page || "Generator"); // Set the active page or default to 'Generator'
  }
</script>

<nav>
  <ul>
    <li class:active={activePage === "Generator"}>
      <button on:click={() => setActivePage("Generator")}>Generator</button>
    </li>
    <li class:active={activePage === "Profile"}>
      <button on:click={() => setActivePage("Profile")}>Profile</button>
    </li>
    <li class:active={activePage === "Resumes"}>
      <button on:click={() => setActivePage("Resumes")}>Resumes</button>
    </li>
  </ul>
</nav>

<main>
  {#if activePage === "Generator"}
    <GeneratorForm />
  {/if}
  {#if activePage === "Profile"}
    <ProfilePage />
  {/if}
  {#if activePage === "Resumes"}
    <ResumesPage />
  {/if}
</main>

<style>
  .active {
    opacity: 0.7;
  }
</style>
