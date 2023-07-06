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
  <div class="navbar">
    <div class="logo">
      <img src="../logo.png" alt="logo" />
    </div>
    <ul>
      <li class:active={activePage === "Generator"}>
        <a href="/" on:click={() => setActivePage("Generator")}>Generator</a>
      </li>
      <li class:active={activePage === "Profile"}>
        <a href="/profile" on:click={() => setActivePage("Profile")}>Profile</a>
      </li>
      <li class:active={activePage === "Resumes"}>
        <a href="/resumes" on:click={() => setActivePage("Resumes")}>Resumes</a>
      </li>
    </ul>
  </div>
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
  @import "./navBarComponent.css";
</style>
