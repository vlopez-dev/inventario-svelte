<script>
    import { onMount, onDestroy } from 'svelte';
    import { toasts, ToastContainer, FlatToast }  from "svelte-toasts";
    import bulmaCalendar from "bulma-calendar";

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



  // Funcion para traer la lista de los tipos de articulos


  let tipos = [];

onMount(async () => {
fetch("http://localhost:8001/tipo/tipo/")
.then((response) => response.json())
.then((data) => {
  tipos = data;
  console.log(tipos);
})
.catch((error) => {
  console.log(error);
  return [];
});
});







  //Funcion para el componente calendario
    onMount(() => {
       const calendar = bulmaCalendar.attach(".datepicker", {
         startDate: new Date(),
         dateFormat: "yyyy-MM-dd",
         showHeader: false,
         showFooter: false,
         displayMode: "inline",
         isRange: false,
       });
     });


//Variables del formulario

    let nombre = '';
    let descripcion = '';
    let cantidad 
    let imagen = null;
    let desechable = 0;
    let tipo_articulo = '';
    let fecha_compra = null;
    let precio 
    


    
//Funcion para guardar el formulario
  async function handleSubmit() {
    
    try {
      // const tipoSeleccionado = tipos.find(tipo => tipo.id === tipo_articulo);
      // formData.append('tipo_articulo', tipoSeleccionado.id);
      const formData = new FormData();
      formData.append('nombre', nombre);
      formData.append('descripcion', descripcion);
      formData.append('cantidad', cantidad);
      if (imagen){
        formData.append('imagen', imagen);
      }
      formData.append('desechable', desechable);
      formData.append('fecha_compra', fecha_compra);
      formData.append('precio',precio);
      formData.append('tipo_articulo', tipo_articulo);
      formData.forEach(element => {
        console.log(element);
      });

      const response = await fetch('http://localhost:8001/articulo/articulo/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        toast.success('Successfully toasted!')
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
          <input class="input" type="number" placeholder="cantidad" bind:value={cantidad} min="0">
        </div>
        <div class="field">
        <div class="select is-primary">
          <select bind:value={tipo_articulo} >
            
            {#each tipos as tipo}
            <option value="{tipo.id}">{tipo.nombre}</option>
            {/each}
          </select>
        </div>
        </div>
        <div class="field">
          <input type="date" class="datetimepicker" placeholder="Fecha" bind:value={fecha_compra} >
        </div>
      <div class="field">
       

        <label class="checkbox">
          <input type="checkbox" on:change={() => desechable = !desechable}>
          Desechable
        </label>
      </div>
      <div class="field">
        <input class="input" type="number" placeholder="Precio" bind:value={precio} min="0">
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
            <div class="control btn  ">
              <button   class="button custom-button  is-normal is-rounded" on:click={showToast}>Guardar</button>
            </div>
            <ToastContainer let:data={data}>
              <FlatToast {data}  />
            </ToastContainer>
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


.btn{
  margin-top: 20px;
}


    </style>