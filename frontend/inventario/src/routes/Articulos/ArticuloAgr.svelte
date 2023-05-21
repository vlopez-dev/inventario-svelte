<script>
    import { onMount, onDestroy } from 'svelte';
    let nombre = '';
    let descripcion = '';
    let cantidad = 0;
    let imagen = null;
    let desechable = 0;
    let tipo_articulo = '';
    

  async function handleSubmit() {
    
    try {
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('descripcion', descripcion);
      formData.append('cantidad', cantidad);
      formData.append('imagen', imagen);
      formData.append('desechable', desechable);
      formData.append('tipo_articulo', tipo_articulo);

      const response = await fetch('http://localhost:8001/articulo/articulo/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        console.log("El formulario se guardó exitosamente")
        // Puedes realizar alguna acción aquí, como redirigir a una página de éxito
      } else {
        console.log("Ocurrió un error al guardar el formulario")
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
    
            <h4 class="title custom-title">Articulo</h4>
            <p class="custom-text"></p>
            <div class="custom-message" id="message"></div>
    
          </div>
          <form class="mt-6" action="" on:submit|preventDefault={handleSubmit}>
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
        <div class="field">
          <label class="label custom-label">Descripcion</label>

          <textarea class="textarea" placeholder="Descripcion" bind:value={descripcion}></textarea>
        </div>
        <div class="field">
          <input class="input is-small" type="text" placeholder="Cantidad">
        </div>
        <div class="field">
          <input class="input" type="text" placeholder="Text input"bind:value={tipo_articulo}>

        </div>
      <div class="field">
        <label class="checkbox">
          <input type="checkbox" bind:value={desechable}>
          Remember me
        </label>
      </div>
        <div class="filed">
        <div class="file">
          <label class="file-label">
            <input class="file-input" type="file" name="resume" on:change={(e) => imagen = e.target.files[0]}>
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label">
                Choose a file…
              </span>
            </span>
          </label>
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