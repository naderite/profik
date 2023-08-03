<script>
  import NavBar from "../pages/NavBar.svelte";
  import style from "./app.module.css";
</script>

<div id={style.mainapp}>
  <main />
  <NavBar />
</div>

<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;500;700&display=swap"
    rel="stylesheet"
  />
</svelte:head>
