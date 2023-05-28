<script>
    import { onMount, onDestroy } from 'svelte';
    import { toasts, ToastContainer, FlatToast }  from "svelte-toasts";

    let nombre = '';
    
    // Funcion para mostrar la notificacion de suceso
    const showToast = () => {
    const toast = toasts.add({
      title: 'Agregado',
      description: 'Agregado con exito",',
      duration: 3000, // 0 or negative to avoid auto-remove
      placement: 'bottom-right',
      type: 'info',
      theme: 'dark',
      placement: 'bottom-right',
			showProgress: true,
      type: 'success',
      theme: 'dark',
      onClick: () => {},
      onRemove: () => {},
      // component: BootstrapToast, // allows to override toast component/template per toast
    });

  };
    

  async function handleSubmit() {
    try {
      const formData = new FormData();
      formData.append('nombre', nombre);
      const response = await fetch('http://localhost:8001/tipo/tipo/', {
        method: 'POST',
        body: formData,
      });
      if (response.ok) {
        console.log("El formulario se guardó exitosamente")
      } else {
        console.log("Ocurrió un error al guardar el formulario")
      }
    } catch (error) {
      console.log(error);
    }
  }





    
    </script>
    <section class="hero is-fullheight custom-component  " >
      <div class="columns is-multiline mx-2 my-6">
        <div class="column"></div>
        <div class="column is-one-quarter">
          <div class="container">
    
            <h4 class="title custom-title">Tipos de articulos</h4>
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
     
    
    
     
          <div class="field is-grouped is-justify-content-center">
            <div class="control btn-cv  ">
              <button class="button custom-button  is-normal is-rounded " on:click={showToast}>
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
      <ToastContainer let:data={data}>
        <FlatToast {data}  />
      </ToastContainer>
    </section>
    <style></style>