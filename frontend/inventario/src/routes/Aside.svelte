
<script>
    import {PlusSquareIcon,ListIcon} from 'svelte-feather-icons'
    import {HomeIcon} from 'svelte-feather-icons'


</script>

<aside class="aside is-placed-left is-expanded">
    <div class="aside-tools">
      <div class="aside-tools-label">
        <span><b>Inventario</b></span>
      </div>
    </div>
    <div class="menu is-menu-main">
      <p class="menu-label">General</p>
      <ul class="menu-list">
        <li>
          <a href="index.html" class="is-active router-link-active has-icon">
            <i class="icon"><HomeIcon /></i>

            <span class="menu-item-label">Dashboard</span>
          </a>
        </li>
      </ul>
      <p class="menu-label">Empresa</p>
      <ul class="menu-list">
        <li>
          <a href="" class="">
            <i class="icon"><PlusSquareIcon /></i>
            <span>Agregar</span>
          </a>
        </li>
        <li>
          <a href="forms.html" class="has-icon">
            <i class="icon"><ListIcon/></i>
            <span class="menu-item-label">Listado</span>
          </a>
        </li>
      
        <li>
      
        
        </li>
      </ul>
      <p class="menu-label">Area</p>
      <ul class="menu-list">
        <li>
          <a href="" target="_blank" class="has-icon">
            <i class="icon"><PlusSquareIcon /></i>

            <span class="menu-item-label">Agregar</span>
          </a>
        </li>
        <li>
          <a href="https://justboil.me/bulma-admin-template/free-html-dashboard/" class="has-icon">
            <i class="icon"><ListIcon/></i>

            <span class="menu-item-label">Listado</span>
          </a>
        </li>
      </ul>

      <p class="menu-label">Articulo</p>
      <ul class="menu-list">
        <li>
          <a href="" target="_blank" class="has-icon">
            <i class="icon"><PlusSquareIcon /></i>

            <span class="menu-item-label">Agregar</span>
          </a>
        </li>
        <li>
          <a href="https://justboil.me/bulma-admin-template/free-html-dashboard/" class="has-icon">
            <i class="icon"><ListIcon/></i>
            <span class="menu-item-label">Listado</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>

  <style>
    aside{
        position: fixed;
        z-index: 40;
        top: 0 ;
        left: 0;
        height: 100vh;
        padding: 15px;
        box-shadow: none;
        background-color: #094067;
    }

    a{
        display: block;
        color: #fffffe;

    }

    .icon{
      display: inline-block;
      vertical-align: middle;

    }
  </style>