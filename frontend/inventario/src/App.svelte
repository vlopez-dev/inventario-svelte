<script>
 import Nav from "./routes/Nav.svelte";
 import AreaAgr from "./routes/Area/AreaAgr.svelte";
 import ArticuloAgr from "./routes/Articulos/ArticuloAgr.svelte";
 import Home from "./routes/Home.svelte";
 import Router from 'svelte-spa-router'


 let routes={
   "/": Home,
   "/AreaAgr": AreaAgr,
   "/ArticuloAgr": ArticuloAgr
 }
</script>


    <Nav
    item1="Home"
    item2="Agregar"
    item3="Agregar"
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
