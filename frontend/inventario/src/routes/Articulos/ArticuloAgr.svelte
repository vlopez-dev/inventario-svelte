<script>
    import { onMount, onDestroy } from 'svelte';
    import bulmaCalendar from "bulma-calendar";

    onMount(() => {
       const calendar = bulmaCalendar.attach(".datepicker", {
         startDate: new Date(),
         dateFormat: "yyyy-mm-dd",
         showHeader: false,
         showFooter: false,
         displayMode: "inline",
         isRange: false,
       });
     });



    let nombre = '';
    let descripcion = '';
    let cantidad = 0;
    let imagen = null;
    let desechable = 0;
    let tipo_articulo = '';
    let fecha_compra = '';
    let precio = 0;
    




  async function handleSubmit() {
    
    try {
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('descripcion', descripcion);
      formData.append('cantidad', cantidad);
      formData.append('imagen', imagen);
      formData.append('desechable', desechable);
      formData.append('fecha_compra',fecha_compra)
      formData.append('precio',precio)
      formData.append('tipo_articulo', tipo_articulo);

      const response = await fetch('http://localhost:8001/articulo/articulo/', {
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


  // Funcion para traer la lista de los tipos de articulos


let tipos = [];

onMount(async () => {
fetch("http://localhost:8001/tipo/tipo/")
.then((response) => response.json())
.then((data) => {
  tipos = data;
  console.log(tipos);
  // console.log(data);
})
.catch((error) => {
  console.log(error);
  return [];
});
});






    
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
          <input class="input is-small" type="number" placeholder="Cantidad">
        </div>

        <div class="select is-primary">
          <select>
            <option>Tipos</option>
            {#each tipos as tipo}
            <option>{tipo.nombre}</option>
            {/each}
          </select>
        </div>
        <div class="field">
          <input type="date" class="datetimepicker" placeholder="Fecha">
        </div>
      <div class="field">
        <label class="checkbox">
          <input type="checkbox" bind:value={desechable}>
        </label>
      </div>
      <div class="field">
        <input type="text" placeholder="Precio">
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
                Seleccionar imagen
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
    <style>



    </style>