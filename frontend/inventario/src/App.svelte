<script>
 import Nav from "./routes/Nav.svelte";
 import AreaAgr from "./routes/Area/AreaAgr.svelte";
 import ListArea from "./routes/Area/ListArea.svelte";
 import ArticuloAgr from "./routes/Articulos/ArticuloAgr.svelte";
 import ListArt from "./routes/Articulos/ListArt.svelte";
 import Home from "./routes/Home.svelte";
 import Router from 'svelte-spa-router'


 let routes={
   "/": Home,
   "/AreaAgr": AreaAgr,
   "/ArticuloAgr": ArticuloAgr,
   "/ListArt": ListArt,
   "/ListArea":ListArea,
   }
</script>


    <Nav
    item1="Home"
    item2="Agregar"
    item3="Agregar"
    item4 ="Listar Articulos"
    item5= "Listar Areas"
    ></Nav>

    <Router {routes}></Router>





<style>
  
 :global(body) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: white;
	}
  
  
</style>
