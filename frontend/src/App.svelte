<script>
  import { SyncLoader } from "svelte-loading-spinners";
  async function fetchImage() {
    loading = true;
    // await fetch("https://api.cryptoclicker.org/getimage")
    await fetch("https://api.jstitt.dev/philosophy/getimage")
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        loading = false;
        image_src = "data:image/jpg;base64," + data.content;
      });
  }
  let image_src = "";

  let loading = false;
</script>

<!-- start html -->
<div class="main">
  <h1>Philosophy Bot</h1>
  <button class="submit" on:click={fetchImage}> Get Image </button>
  {#if loading}
    <SyncLoader />
  {/if}
  {#if image_src.length > 0}
    <img src={image_src} alt="Philosophy Quote" width="512" height="512" />
  {/if}
</div>

<!-- end html -->
<style>
  h1 {
    margin: 0;
  }

  .main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>
