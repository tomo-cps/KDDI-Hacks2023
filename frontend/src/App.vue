<template>
  <v-app>
    <v-app-bar
        app
      >
        <v-btn icon @click="$router.push('/')">
          <v-icon>mdi-home</v-icon>
        </v-btn>

        <v-img
        :src="'/images/Chatcloudlogo.png'"
        aspect-ratio="1"
        max-width="80"
        class="mr-2"
        ></v-img>
        <v-toolbar-title>Chat-Cloud</v-toolbar-title>
  
      </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
}
</script>