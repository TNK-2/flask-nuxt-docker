<template>
  <section class="container">
    <div v-if="note">
      <h3>{{note.title}}</h3>
      <div>
        {{note.text}}
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex';

export default {};
</script>

<style>
.container {
  min-height: 100vh;
  padding: 16px;
}

h3 {
  margin: 16px 0;
  padding: 8px 0;
  border-bottom: solid 1px #e5e5e5;
}

li + li {
  margin: 16px 0;
}

p {
  margin: 8px 0;
}
</style>
