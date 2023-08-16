<template>
  <body class="min-h-screen pt-20 bg-black">
    <Header />
    <router-view></router-view>
    <main class="h-screen mb-auto"></main>
    <Footer />
  </body>
</template>

<script setup lang="ts">
import Header from './components/Header/header.vue'
import Footer from './components/Footer/footer.vue'

</script>