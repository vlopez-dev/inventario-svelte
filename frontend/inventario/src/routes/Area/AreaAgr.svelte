<script>
import { onMount, onDestroy } from 'svelte';
let nombre = '';

  async function handleSubmit() {
    try {
      const response = await fetch('http://localhost:8001/area/area/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre: nombre }),
      });

      if (response.ok) {
        console.log("El formulario se guardó exitosamente")
        // Puedes realizar alguna acción aquí, como redirigir a una página de éxito
      } else {
        // Ocurrió un error al guardar el formulario
        // Puedes manejar el error de acuerdo a tus necesidades
      }
    } catch (error) {
      // Manejar errores de la solicitud
    }
  }

</script>
<section class="hero is-fullheight custom-component  " >
  <div class="columns is-multiline mx-2 my-6">
    <div class="column"></div>
    <div class="column is-one-quarter">
      <div class="container">
        
        <h4 class="title custom-title">Area</h4>
        <p class="custom-text"></p>
        <div class="custom-message" id="message"></div>

      </div>
      <form class="mt-6" action=""on:submit|preventDefault={handleSubmit}>
      <div class="field">
        <label class="label custom-label">Nombre</label>
        <div class="control has-icons-left has-icons-right">
          <input class="input custom-input " type="name" bind:value={nombre} placeholder="Nombre">
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-exclamation-triangle"></i>
          </span>
        </div>
      </div>
    
     
      <div class="field is-grouped is-justify-content-center">
        <div class="control btn-cv  ">
          <button class="button custom-button  is-normal is-rounded ">
            <span>
          </span>
            Guardar</button>
        </div>

      </div>

    </form>
    <div class="column">
    <div class="container">

  </div>
</div>
    </div>

    <div class="column"></div>

  </div>
</section>
<style></style>