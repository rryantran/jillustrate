<script>
  import ThresholdSlider from "./lib/ThresholdSlider.svelte";
  import FileUpload from "./lib/FileUpload.svelte";
</script>

<main class="flex flex-col items-center justify-evenly min-h-screen">
  <h1 class="text-3xl">jillustrate</h1>
  <FileUpload />
  <ThresholdSlider />
</main>
