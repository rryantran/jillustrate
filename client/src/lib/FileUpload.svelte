<script>
  let fileInput;

  function openFileBrowser() {
    fileInput.click();
  }

  function handleDragOver(e) {
    e.preventDefault();
  }

  function handleDrop(e) {
    e.preventDefault();
  }
</script>

<button
  class="cursor-pointer border-2 border-dashed rounded-lg p-5 hover:bg-zinc-100"
  on:click={openFileBrowser}
  on:dragover={handleDragOver}
  on:drop={handleDrop}
>
  <p>Drag and drop a file</p>
  <p>or click to select one</p>
  <input type="file" accept="image/png" bind:this={fileInput} hidden />
</button>
