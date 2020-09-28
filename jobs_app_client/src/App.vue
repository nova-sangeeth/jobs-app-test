<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>

<template>
  <div id="app" class="container">
    <nav class="navbar navbar-expand-sm bg-light">
      <ul class="navbar-nav">
        <h4>
          <router-link :to="{ name: 'Index' }" class="nav-link"
            >Job-finder</router-link
          >
        </h4>
        <li class="nav-item">
          <router-link :to="{ name: 'Create' }" class="nav-link"
            >Add Item</router-link
          >
        </li>
      </ul>
    </nav>
    <transition name="fade">
      <div class="gap">
        <router-view></router-view>
      </div>
    </transition>
  </div>
</template>


<script>
export default {};
</script>


