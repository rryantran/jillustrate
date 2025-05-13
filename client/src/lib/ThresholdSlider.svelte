<script>
  let threshold = 0;
</script>

<div class="flex flex-col items-center">
  <label for="slider">Threshold: {threshold}</label>
  <input type="range" min="0" max="255" bind:value={threshold} />
</div>
